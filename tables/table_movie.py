from rich.console import Console
from rich.table import Table
from models.ItemMovie import ItemMovie

console = Console()

movieType = [
    'Title',
    ':scroll: Overview',
    ':date: Release',
    ':watch: Time',
    ':100: IMDB Rate',
    ':globe_with_meridians: Online',
    ':movie_camera: Trailers',
    ':link: Details'
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
        title=f"[white]{item.title}[/white]",
        overview=item.overview,
        release=item.formatDate(),
        time=item.formatTime(),
        imdb=item.imdbStr(),
        online=item.formatSources(),
        trailers=item.getListTrailers(),
        url=item.createUrl()
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
        url,
        end_section=True
    )
