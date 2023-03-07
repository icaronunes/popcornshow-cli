from rich.console import Console
from rich.table import Table
from models.itemSearch import ItemSearch

console = Console()

table = Table(
    title="POPCORN SHOW - SEARCH",
    highlight=True,
    show_header=True,
    show_edge=True,
    expand=True
)
movieType = [
    'Index',
    'Title',
    'Release',
    'Type',
    'IMDB rate',
    'Online',
    'Details'
]


def tableItems(items: list[ItemSearch]):
    for title in movieType:
        table.add_column(title)
    for index, item in enumerate(items):
        __tableItem__(
            id=str(index + 1),
            title=item.title,
            release=item.formatSimpleDateStr(),
            type=item.formatLongType(),
            imdb=item.imdbStr(),
            online=item.formatOnline(),
            url=item.createUrl()
        )
    console.print(table)


def __tableItem__(
    id: int,
    title: str,
    imdb: float,
    type: chr,
    release: str,
    online: str,
    url: str
):

    table.add_row(
        str(id),
        title,
        release,
        type,
        imdb,
        online,
        url
    )
