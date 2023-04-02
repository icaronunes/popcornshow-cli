from api.api import search, getMovieApi, getTvShowApi
from api.models.Result import Result
from api.models.SearchApi import ContentType
from models.Search import Search
from models.ItemMovie import ItemMovie
from models.ItemShow import ItemShow
from utils import formatDate
from dto import formatList
import json


def searchReel(query: str, year: int | None, type: str | None) -> list[Search]:
    result: Result = search(query=query)
    if result.error is None:
        objJson = json.loads(result.value)
        listSearch = filtersArgs(objJson['items'], year, type)
        return formatList(listSearch)
    else:        
        return []


def transformItem(item: Search) -> Result:
    match item.type:
        case ContentType.M.value:
            movie = getMovieApi(
                item.slug)
            if movie.error is None:
                return Result(value=ItemMovie(**json.loads(movie.value)))
            else:
                return Result(Exception("Match not Found..."))
        case ContentType.S.value:
            tv = getTvShowApi(item.slug)
            if tv.error is None:
                return Result(value=ItemShow(**json.loads(tv.value)))
            else:
                return Result(Exception("Match not Found..."))
        case _:
            return Result(Exception("Match not Found..."))


def filterByYear(item, year) -> bool:
    if item['released_on'] == None:
        return True
    return formatDate(item['released_on']).year == year


def filterByType(item, type) -> bool:
    if item['content_type'] == None:
        return True
    return item['content_type'] == type


def filtersArgs(items: list[any], year: int | None, type: str | None):
    if year == None and type == None:
        return items
    if year != None and type == None:
        return list(filter(lambda x: (filterByYear(x, year)), items))
    if year == None and type != None:
        return list(filter(lambda x: (filterByType(x, type)), items))
    if year != None and type != None:
        return list(filter(lambda x: (filterByType(x, type) and filterByYear(x, year)), items))
