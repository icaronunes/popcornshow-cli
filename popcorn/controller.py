import json

from popcorn.api.api import get_movie_api, get_person_details, get_tvshow_api, search
from popcorn.api.models.PersonApi import PersonApi
from popcorn.api.models.Result import Result
from popcorn.api.models.SearchApi import ContentType
from popcorn.dto import format_list
from popcorn.models.ItemMovie import ItemMovie
from popcorn.models.ItemShow import ItemShow
from popcorn.models.Search import Search
from popcorn.utils import format_date


def search_reel(query: str, year: int | None, type: str | None) -> list[Search]:
    result: Result = search(query=query)
    if result.error is None:
        objJson = json.loads(result.value)
        if objJson["items"].__len__() == 0:
            return []
        listSearch = filters_args(objJson["items"], year, type)
        return format_list(listSearch)
    else:
        []


def person_reel(id) -> Result:
    result = get_person_details(id)
    if result.error is None:
        return Result(value=PersonApi(**json.loads(result.value)))
    else:
        return Result(Exception("Match not Found..."))


def transform_item(slug: str, type: str) -> Result:
    match type:
        case ContentType.M.value:
            movie = get_movie_api(slug)
            if movie.error is None:
                return Result(value=ItemMovie(**json.loads(movie.value)))
            else:
                return Result(Exception("Match not Found..."))
        case ContentType.S.value:
            tv = get_tvshow_api(slug)
            if tv.error is None:
                return Result(value=ItemShow(**json.loads(tv.value)))
            else:
                return Result(Exception("Match not Found..."))
        case _:
            return Result(Exception("Match not Found..."))


def filter_by_year(item, year) -> bool:
    if item["released_on"] == None:
        return True
    return format_date(item["released_on"]).year == year


def filter_by_type(item, type) -> bool:
    if item["content_type"] == None:
        return True
    return item["content_type"] == type


def filters_args(items: list[any], year: int | None, type: str | None):
    if year == None and type == None:
        return items
    if year != None and type == None:
        return list(filter(lambda x: (filter_by_year(x, year)), items))
    if year == None and type != None:
        return list(filter(lambda x: (filter_by_type(x, type)), items))
    if year != None and type != None:
        return list(
            filter(
                lambda x: (filter_by_type(x, type) and filter_by_year(x, year)), items
            )
        )
