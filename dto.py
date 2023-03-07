

from models.itemSearch import ItemSearch


def formatList(items: list[object]) -> list[ItemSearch]:
    def dto(values):
        index, item = values
        return ItemSearch(
            id=index,
            title=item['title'],
            imdb=item['imdb_rating'],
            type=item['content_type'],
            release=item['released_on'],
            online=list(item['sources']),
            slug=item['slug'])

    lista = map(lambda item: dto(item), enumerate(items))
    return sorted(lista, key=lambda item: str(item.release),reverse=True) 
    """
    Criar model para não precisar converter release para fazer o sorted
    """


