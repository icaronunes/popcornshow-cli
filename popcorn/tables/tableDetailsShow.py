from rich.console import Console
from rich.table import Table, box

from popcorn.tables.people import people
from popcorn.tables.sources import source
from popcorn.tables.TableInterface import TableInterface

console = Console()

topTable = [
    ":scroll: Overview",
    ":date: Release",
    ":watch: Season",
    ":100: IMDB",
    ":traffic_light: Classification",
    ":movie_camera: Trailers",
]


table = Table(
    highlight=True,
    show_header=True,
    show_edge=True,
    expand=True,
    show_lines=True,
    box=box.DOUBLE_EDGE,
)


def table_details_show(item: TableInterface) -> Table:
    for title in topTable:
        table.add_column(title)

    __tableItem(
        overview=item.get_overview(),
        release=item.get_date(),
        seasons=item.get_number_seasons(),
        imdb=item.get_imdb(),
        classification=item.get_classification(),
        trailers=item.get_trailers(),
    )
    return table


def __tableItem(
    overview: str,
    release: str,
    seasons: str,
    imdb: float,
    classification: str,
    trailers: list[str],
):
    table.add_row(
        overview, release, seasons, imdb, classification, trailers, end_section=True
    )
