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


def __tableItemPerson(
        name: str,
        birthdate: str,
        birthplace: str,
        deathdate: str
) -> Table:

    table.add_row(
        name,
        birthdate,
        birthplace,
        deathdate        
    )
    return table


topTablePerson = [
    ':scroll: Name',
    ':date: Birth date',
    ':star: Birth place',
    ':date: Death date'
]

def table_details_person(item: PersonApi) -> Table:
    for title in topTablePerson:
        table.add_column(title)
    __tableItemPerson(
        name=item.name,
        birthdate="-- -- --" if item.birthdate is None else formatDateStr(item.birthdate),
        birthplace="" if item.birthplace is None else item.birthplace,
        deathdate="-- -- --" if item.deathdate is None else formatDateStr(item.deathdate)
    )
    return table