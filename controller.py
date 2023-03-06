from api import search as SearchApi
from tables import __tableItem__, tableItems
from utils import formatDate
from dto import formatList
import json


def searchReel(query: str, year: int | None, type: str | None):
    result = SearchApi(query=query)
    objJson = json.loads(result)
    listSearch = filtersArgs(objJson['items'], year, type)
    tableItems(formatList(listSearch))


def fillTable(item):
    __tableItem__(
        title=item['title'],
        imdb=item['imdb_rating'],
        type=item['content_type'],
        release=item['released_on'],
        online=item['sources'],
        url=item['slug']
    )


def filterByYear(item, year) -> bool:
    if item['released_on'] == None:
        return True
    return formatDate(item['released_on']).year == year

def filterByType(item, type) -> bool:
    if item['content_type'] == None:
        return True
    return item['content_type'] == type

def filtersArgs(items, year: int | None, type: str | None):
    if year == None and type == None:
        return items
    if year != None and type == None:
        return list(filter(lambda x: (filterByYear(x, year)),items))
    if year == None and type != None:
        return list(filter(lambda x: (filterByType(x, type)), items))