from utils import formatDate, formatDateStr
from rich.console import Console
from rich.table import Table, box
from tables.TableInterface import TableInterface
from tables.people import people
from tables.sources import source
from api.models.PersonApi import PersonApi

console = Console()

topTable = [
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


def table_details(item: TableInterface) -> Table:
    for title in topTable:
        table.add_column(title)

    __tableItem(
        overview=item.get_overview(),
        release=item.get_date(),
        time=item.get_time(),
        imdb=item.get_imdb(),
        classification=item.get_classification(),
        trailers=item.get_trailers()
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