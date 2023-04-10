from rich.console import Console
from rich.table import Table, box
from tables.TableInterface import TableInterface
from tables.people import people
from tables.sources import source

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
        name='Kiefer Sutherland',
        birthdate='1966-12-21',
        birthplace='Paddington, London, England, UK',
        deathdate='1966-12-21'
) -> Table:

    table.add_row(
        name,
        birthdate,
        birthplace,
        deathdate        
    )
    return table


topTablePerson = [
    'Name',
    'Birth date',
    'Birth place',
    'Death date'
]


def table_details_person(item) -> Table:
    for title in topTablePerson:
        table.add_column(title)

    __tableItemPerson(
        name=item.name,
        birthdate=item.birthdate,
        birthplace=item.birthplace,
        deathdate=item.deathdate    
    )
    return table
