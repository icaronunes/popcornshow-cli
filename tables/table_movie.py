from rich.console import Console
from rich.table import Table, box
from models.ItemMovie import ItemMovie
from tables.people import people
from tables.sources import source

console = Console()

movieType = [
    ':scroll: Overview',
    ':date: Release',
    ':watch: Time',
    ':100: IMDB',
    ':traffic_light: Classification',
    ':movie_camera: Trailers'
]


table = Table(
    highlight=True,
    show_header=True,
    show_edge=True,
    expand=True,
    show_lines=True,
    box=box.DOUBLE_EDGE
)


def tableMovie(item: ItemMovie) -> Table:
    for title in movieType:
        table.add_column(title)

    __tableItem(
        overview=item.overview,
        release=item.formatDate(),
        time=item.formatTime(),
        imdb=item.imdbStr(),
        classification=f"[b][white]{item.classification}" if item.classification else 'Who knows',
        trailers=item.getListTrailers()
    )
    return table


def __tableItem(
    overview: str,
    release: str,
    time: str,
    imdb: float,
    classification: str,
    trailers: list[str],
):

    table.add_row(
        overview,
        release,
        time,
        imdb,
        classification,
        trailers,
        end_section=True
    )
