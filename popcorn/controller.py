import json

from popcorn.api.api import get_person_details, getMovieApi, getTvShowApi, search
from popcorn.api.models.PersonApi import PersonApi
from popcorn.api.models.Result import Result
from popcorn.api.models.SearchApi import ContentType
from popcorn.dto import formatList
from popcorn.models.ItemMovie import ItemMovie
from popcorn.models.ItemShow import ItemShow
from popcorn.models.Search import Search
from popcorn.utils import formatDate


def searchReel(query: str, year: int | None, type: str | None) -> list[Search]:
    result: Result = search(query=query)
    if result.error is None:
        objJson = json.loads(result.value)
        if objJson["items"].__len__() == 0:
            return []
        listSearch = filtersArgs(objJson["items"], year, type)
        return formatList(listSearch)
    else:
        []


def person_reel(id) -> Result:
    result = get_person_details(id)
    if result.error is None:
        return Result(value=PersonApi(**json.loads(result.value)))
    else:
        return Result(Exception("Match not Found..."))


def transformItem(slug: str, type: str) -> Result:
    match type:
        case ContentType.M.value:
            movie = getMovieApi(slug)
            if movie.error is None:
                return Result(value=ItemMovie(**json.loads(movie.value)))
            else:
                return Result(Exception("Match not Found..."))
        case ContentType.S.value:
            tv = getTvShowApi(slug)
            if tv.error is None:
                return Result(value=ItemShow(**json.loads(tv.value)))
            else:
                return Result(Exception("Match not Found..."))
        case _:
            return Result(Exception("Match not Found..."))


def filterByYear(item, year) -> bool:
    if item["released_on"] == None:
        return True
    return formatDate(item["released_on"]).year == year


def filterByType(item, type) -> bool:
    if item["content_type"] == None:
        return True
    return item["content_type"] == type


def filtersArgs(items: list[any], year: int | None, type: str | None):
    if year == None and type == None:
        return items
    if year != None and type == None:
        return list(filter(lambda x: (filterByYear(x, year)), items))
    if year == None and type != None:
        return list(filter(lambda x: (filterByType(x, type)), items))
    if year != None and type != None:
        return list(
            filter(lambda x: (filterByType(x, type) and filterByYear(x, year)), items)
        )
