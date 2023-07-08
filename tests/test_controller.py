from popcorn.controller import searchReel, transformItem
from popcorn.models.Search import Search
from popcorn.models.ItemMovie import ItemMovie
from popcorn.models.ItemShow import ItemShow
from popcorn.api.models.SearchApi import ContentType
from popcorn.api.models.Result import Result

MOVIE = 'the-matrix-1999'
SHOW = 'lost-2004'


def test_with_empty_searchReel():
    empty = searchReel(query='return_empty_query', year=None, type=None)
    assert empty.__len__() == 0


def test_with_not_empty_searchReel():
    empty = searchReel(query='the matrix', year=None, type=None)
    assert empty.__len__() != 0


def test_transformItem():
    itemSearch = Search(id=1, title='title', release='2000',
                        type=ContentType.M.value, imdb=10.0, online=[""], slug=MOVIE)
    result: Result = transformItem(itemSearch.slug, itemSearch.type)
    assert result.value
    assert result.error == None


def test_transformItem_error_movie():
    typeMovie = ContentType.M.value
    itemSearch = Search(id=1, title='title', release='2000',
                        type=typeMovie, imdb=10.0, online=[""], slug='slug_missing')
    result: Result = transformItem(itemSearch.slug, itemSearch.type)
    assert result.value == None
    assert isinstance(result.error, Exception)
    assert str(result.error) == "Match not Found..."


def test_transformItem_error_show():
    typeShow = ContentType.S.value
    itemSearch = Search(id=1, title='title', release='2000',
                        type=typeShow, imdb=10.0, online=[""], slug='slug_missing')
    result: Result = transformItem(itemSearch.slug, itemSearch.type)
    assert result.value == None
    assert isinstance(result.error, Exception)
    assert str(result.error) == "Match not Found..."


def test_transformItem_success_show():
    typeShow = ContentType.S.value
    itemSearch = Search(id=1, title='title', release='2000',
                        type=typeShow, imdb=10.0, online=[""], slug=SHOW)
    result: Result = transformItem(itemSearch.slug, itemSearch.type)
    assert result.error == None
    assert result.value
