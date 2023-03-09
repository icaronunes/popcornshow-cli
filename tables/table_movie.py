from rich.console import Console
from rich.table import Table
from models.ItemMovie import ItemMovie
from utils import createUrl as fullUrl, formatSource, formatType, formatDate

console = Console()

movieType = [
    'Title',
    "Overview",
    'Release',
    'Time',
    'IMDB Rate',
    'Online',
    'Trailers',
    'Details',    
    'Url'
]


table = Table(
    title="POPCORN SHOW - MOVIE",
    highlight=True,
    show_header=True,
    show_edge=True,
    expand=True
)


def tableMovie(item: ItemMovie):
    for title in movieType:
        table.add_column(title)

    __tableItem(
        title=item.title,
        overview=item.overview,
        release=item.released_on,
        time=str(item.runtime),
        imdb=str(item.imdb_rating),
        online=formatSource(item.sources),
        trailers=str('item.trailers'),
        url=item.slug        

    )
    console.print(table, highlight=True)


def __tableItem(
    title: str,
    overview: str,
    release: str,
    time: str,
    imdb: float,
    online: str,
    trailers: list[str],
    url: str,    
):

    table.add_row(
        title,
        overview,
        release,
        time,
        imdb,
        online,
        trailers,
        url
    ) 
