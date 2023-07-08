

from popcorn.models.Search import Search
from popcorn.api.models.SearchApi import Item


def formatList(items: list[Item]) -> list[Search]:
    def dto(values):
        index, item = values
        return Search(
            id=index,
            title=item['title'],
            imdb=item['imdb_rating'],
            type=item['content_type'],
            release=item['released_on'],
            online=item['sources'],
            slug=item['slug']
        )

    result = map(lambda item: dto(item), enumerate(items))
    return sorted(result, key=lambda item: str(item.release), reverse=True)
