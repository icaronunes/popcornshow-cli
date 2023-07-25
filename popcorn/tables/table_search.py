from rich.console import Console
from rich.table import Table

from popcorn.models.Search import Search

console = Console()

searchType = [
    ":id: Index",
    ":blue_book: Title",
    ":date: Release",
    ":flags: Type",
    ":100: IMDB rate",
    ":movie_camera: Online",
    ":link: Details",
]


def __init_table__() -> Table:
    table = Table(
        title="POPCORN SHOW - SEARCH",
        highlight=True,
        show_header=True,
        show_edge=True,
        expand=True,
    )
    for title in searchType:
        table.add_column(title)
    return table


def table_search(items: list[Search]) -> Table:
    table = __init_table__()
    for index, item in enumerate(items):
        __tableItem__(
            table=table,
            id=str(index + 1),
            title=f"[white]{item.title}[/white]",
            release=item.format_simple_date_str(),
            type=item.format_long_type(),
            imdb=item.imdb_str(),
            online=item.format_online(),
            url=item.create_url(),
        )
    return table


def __tableItem__(
    table: Table,
    id: int,
    title: str,
    imdb: float,
    type: chr,
    release: str,
    online: str,
    url: str,
):
    table.add_row(str(id), title, release, type, imdb, online, url)
