from rich.console import Console
from rich.table import Table, box

from popcorn.api.models.PersonApi import PersonApi
from popcorn.tables.people import people
from popcorn.tables.sources import source
from popcorn.tables.TableInterface import TableInterface
from popcorn.utils import formatDate, formatDateStr

topTable = [
    ":scroll: Overview",
    ":date: Release",
    ":watch: Time",
    ":100: IMDB",
    ":traffic_light: Classification",
    ":movie_camera: Trailers",
]


def __initTable__() -> Table:
    table = Table(
        highlight=True,
        show_header=True,
        show_edge=True,
        expand=True,
        show_lines=True,
        box=box.DOUBLE_EDGE,
    )
    for title in topTable:
        table.add_column(title)

    return table


def table_details(item: TableInterface) -> Table:
    table = __tableItem__(
        table=__initTable__(),
        overview=item.get_overview(),
        release=item.get_date(),
        time=item.get_time(),
        imdb=item.get_imdb(),
        classification=item.get_classification(),
        trailers=item.get_trailers(),
    )
    return table


def __tableItem__(
    table: Table,
    overview: str,
    release: str,
    time: str,
    imdb: float,
    classification: str,
    trailers: list[str],
) -> Table:
    table.add_row(
        overview, release, time, imdb, classification, trailers, end_section=True
    )
    return table
