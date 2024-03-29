from popcorn.api.models.Result import Result
from popcorn.api.models.SearchApi import ContentType
from popcorn.controller import (
    filter_by_type,
    filters_args,
    person_reel,
    search_reel,
    transform_item,
)
from popcorn.models.ItemMovie import ItemMovie
from popcorn.models.ItemShow import ItemShow
from popcorn.models.Search import Search

MOVIE = "the-matrix-1999"
SHOW = "lost-2004"


def test_with_empty_search_reel():
    empty = search_reel(query="return_empty_query", year=None, type=None)
    assert empty == []


def test_with_not_empty_search_reel():
    empty = search_reel(query="the matrix", year=None, type=None)
    assert empty.__len__() != 0


def test_transform_item():
    itemSearch = Search(
        id=1,
        title="title",
        release="2000",
        type=ContentType.M.value,
        imdb=10.0,
        online=[""],
        slug=MOVIE,
    )
    result: Result = transform_item(itemSearch.slug, itemSearch.type)
    assert result.value
    assert result.error == None


def test_transform_item_error_movie():
    typeMovie = ContentType.M.value
    itemSearch = Search(
        id=1,
        title="title",
        release="2000",
        type=typeMovie,
        imdb=10.0,
        online=[""],
        slug="slug_missing",
    )
    result: Result = transform_item(itemSearch.slug, itemSearch.type)
    assert result.value == None
    assert isinstance(result.error, Exception)
    assert str(result.error) == "Match not Found..."


def test_transform_item_error_show():
    typeShow = ContentType.S.value
    itemSearch = Search(
        id=1,
        title="title",
        release="2000",
        type=typeShow,
        imdb=10.0,
        online=[""],
        slug="slug_missing",
    )
    result: Result = transform_item(itemSearch.slug, itemSearch.type)
    assert result.value == None
    assert isinstance(result.error, Exception)
    assert str(result.error) == "Match not Found..."


def test_transform_item_success_show():
    typeShow = ContentType.S.value
    itemSearch = Search(
        id=1,
        title="title",
        release="2000",
        type=typeShow,
        imdb=10.0,
        online=[""],
        slug=SHOW,
    )
    result: Result = transform_item(itemSearch.slug, itemSearch.type)
    assert result.error is None
    assert result.value


def test_transform_item_with_type_wrong():
    typeShow = "qwert"
    itemSearch = Search(
        id=1,
        title="title",
        release="2000",
        type=typeShow,
        imdb=10.0,
        online=[""],
        slug=SHOW,
    )
    result: Result = transform_item(itemSearch.slug, itemSearch.type)
    assert result.value == None
    assert isinstance(result.error, Exception)
    assert str(result.error) == "Match not Found..."


def test_get_person_details_ok():
    result = person_reel("rebecca-ferguson-1983")
    assert result.value
    assert result.error is None


def test_get_person_details_error():
    result = person_reel("mirespeita!_nem_existo")
    assert result.value is None
    assert isinstance(result.error, Exception)
    assert "Match not Found..." in str(result.error)


def test_filter_by_type_equals():
    type = "ok"
    item = {"content_type": type}
    result = filter_by_type(item, type)
    assert result


def test_filter_by_type_not_equals():
    type = "qwert"
    item = {"content_type": "asdfg"}
    result = filter_by_type(item, type)
    assert result is False


def test_filter_by_type_none():
    type = None
    item = {"content_type": type}
    result = filter_by_type(item, type)
    assert result


def test_filters_args_year_none_and_type_none():
    item = {"title": "2006", "released_on": "2006-10-26T00:00:00Z"}
    item2 = {"title": "2008", "released_on": "2008-10-26T00:00:00Z"}
    item3 = {"title": "2010", "released_on": "2010-10-26T00:00:00Z"}
    list = [item, item2, item3]
    result = filters_args(list, None, None)
    assert list == result


def test_filters_args_year_and_type_none():
    first = {"title": "2006", "released_on": "2006-10-26T00:00:00Z"}
    item2 = {"title": "2010", "released_on": "2010-10-26T00:00:00Z"}
    item3 = {"title": "2010", "released_on": "2010-10-26T00:00:00Z"}
    list = [first, item2, item3]
    year = 2010
    result = filters_args(list, year, None)
    assert result.__len__() == 2
    assert item2 == result[0]
    assert item3 == result[1]


def test_filters_args_year_none_and_type():
    item1 = {
        "title": "item1",
        "released_on": "2010-10-26T00:00:00Z,",
        "content_type": "s",
    }
    item2 = {
        "title": "item2",
        "released_on": "2008-10-26T00:00:00Z",
        "content_type": "m",
    }
    item3 = {
        "title": "item3",
        "released_on": "2010-10-26T00:00:00Z",
        "content_type": "s",
    }
    item4 = {
        "title": "item4",
        "released_on": "2010-10-26T00:00:00Z",
        "content_type": "m",
    }
    list = [item1, item2, item3, item4]

    result = filters_args(list, None, "m")
    assert item2 == result[0]
    assert item4 == result[1]
    assert result.__len__() == 2
    result = filters_args(list, None, "s")
    assert item1 == result[0]
    assert item3 == result[1]
    assert result.__len__() == 2


def test_filters_args_year_and_type_m():
    year = 2010
    item1 = {"title": year, "released_on": "2010-10-26T00:00:00Z,", "content_type": "s"}
    item2 = {
        "title": "2008",
        "released_on": "2008-10-26T00:00:00Z",
        "content_type": "s",
    }
    item3 = {"title": year, "released_on": "2010-10-26T00:00:00Z", "content_type": "m"}
    list = [item1, item2, item3]

    result = filters_args(list, year, "m")
    assert item3 == result[0]
    assert result.__len__() == 1
    result = filters_args(list, year, "s")
    assert item1 == result[0]
    assert result.__len__() == 1
