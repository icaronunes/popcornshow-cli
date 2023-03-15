from rich.console import Console
from rich.table import Table
from models.Search import Search
from rich.table import Column

console = Console()

searchType = [
    ':id: Index',
    'Title',
    ':date: Release',
    'Type',
    ':100: IMDB rate',
    ':movie_camera: Online',
    ':link: Details'
]


table = Table(
    title="POPCORN SHOW - SEARCH",
    highlight=True,
    show_header=True,
    show_edge=True,
    expand=True
)


def tableSearch(items: list[Search]) -> Table:
    for title in searchType:
        table.add_column(title)
    for index, item in enumerate(items):
        __tableItem(
            id=str(index + 1),
            title=f"[white]{item.title}[/white]",
            release=item.formatSimpleDateStr(),
            type=item.formatLongType(),
            imdb=item.imdbStr(),
            online=item.formatOnline(),
            url=item.createUrl()
        )
    return table


def __tableItem(
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
