from datetime import datetime

import typer
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.tree import Tree

from popcorn.api.models.PersonApi import PersonApi
from popcorn.api.models.Result import Result
from popcorn.api.models.SearchApi import Item
from popcorn.controller import person_reel, search_reel, transform_item
from popcorn.models.ItemMovie import ItemMovie
from popcorn.models.ItemShow import ItemShow
from popcorn.models.Person import Person
from popcorn.models.Search import Search
from popcorn.tables.people import people, people_biography, person_media
from popcorn.tables.sources import collumn_seasons, pop_collumns
from popcorn.tables.table_details_movie import table_details
from popcorn.tables.table_person import table_details_person
from popcorn.tables.table_search import table_search
from popcorn.tables.tableDetailsShow import table_details_show
from popcorn.utils import format_date

app = typer.Typer(help="PopCorn Show")
console = Console()


@app.command(name="search")
def search(
    name: str,
    year: int = typer.Option(None, "--year", "-y", help="type Year"),
    type: str = typer.Option(None, "--type", "-t", help="'m' or 's'"),
    luck: bool = typer.Option(False, "--luck", "-l"),
):
    list = search_reel(name, year=year, type=type)
    if list:
        if luck:
            order = sorted(list, key=lambda x: x.imdb_str(), reverse=True)
            result = transform_item(order[0].slug, order[0].type)
            choose_types(result)
        else:
            console.print(table_search(list))
            choose_number(list)
    else:
        typer.echo("Not Found")


def person(name: str):
    result: Result = person_reel(name)
    if result.error is None:
        __show_person(result.value)
    else:
        console.print(result.error)


def choose_types(result: Result):
    if result.error:
        console.print(result.error)
    else:
        fill_by_type(result)


def fill_by_type(result: Result):
    if isinstance(result.value, ItemMovie):
        __show_movie(result.value)
    elif isinstance(result.value, ItemShow):
        __show_tvshow(result.value)


def __show_tvshow(show: ItemShow):
    tree = Tree("")
    tree.add(__rich__())
    details = Tree(
        f":blue_book: [blue][b]Details - {show.title} {format_date(show.released_on).year}[/b] - :link: [blue][link={show.createUrl()}]Details in Reelgood.com[/link]",
        expanded=True,
    )
    details.add(table_details_show(show), highlight=False)

    person = Tree(":busts_in_silhouette:[bold][purple] People")
    person.add(people(show.people))

    tree.add(details)
    if person.children.__len__() > 0:
        tree.add(person)
    if show.seasons.__len__() > 0:
        tv = Tree(
            f":movie_camera: [red][b]Where to Watch: {show.title} [/red]| [yellow]With Season {show.seasons.__len__()}"
        )
        tv.add(
            collumn_seasons(show.episodes, reversed(show.seasons)),
            expanded=True,
            highlight=False,
        )
        tree.add(tv)
    tree.add(__footer__(show))
    console.print(tree)

    if show.people.__len__() > 0:
        __choose_person(show.people)


def __show_movie(movie: ItemMovie):
    tree = Tree("")
    tree.add(__rich__())
    details = Tree(
        f":blue_book:[blue][b] Details - {movie.title} {format_date(movie.released_on).year if format_date(movie.released_on) != None else '-- --'}[/b] - :link: [blue][link={movie.create_url()}]Details in Reelgood.com[/link]",
        expanded=True,
    )
    details.add(table_details(movie), highlight=False)

    person = Tree(":busts_in_silhouette:[bold][purple] People")
    person.add(people(movie.people))

    tree.add(details)
    if person.children.__len__() > 0:
        tree.add(person)
    if movie.availability:
        tv = Tree(f":movie_camera:[red][b] Where to Watch: {movie.title}")
        tv.add(pop_collumns(movie.availability), expanded=True, highlight=False)
        tree.add(tv)
    tree.add(__footer__(movie))
    console.print(tree)
    if movie.people.__len__() > 0:
        __choose_person(movie.people)


def __choose_person(list: list[Person]):
    number = Prompt.ask(
        "[blue]Enter the person's number between 1 to "
        + f"{1 if list.__len__() == 1 else list.__len__()} "
        + "for details - Zero to exit\n"
    )
    try:
        value = int(number)
        if value < 1:
            return
        people = list[value - 1]
        person(people["slug"])
        return
    except (TypeError, ValueError, IndexError):
        __choose_person(list)


def __show_person(person: PersonApi):
    tree = Tree("")
    tree.add(__rich__())
    tree.add(table_details_person(person), highlight=False)
    if person.biography is not None:
        tree.add(people_biography(person.biography))
    if person.initial_credits.__len__() > 0:
        tree.add(person_media(person.initial_credits))
    tree.add(__footer_person__(person))
    console.print(tree)

    if person.initial_credits.__len__() > 0:
        choose_media_by_person(person)


def choose_media_by_person(person: PersonApi):
    length = person.initial_credits.__len__()
    number = Prompt.ask(
        "[red]Enter the media number 1 to "
        + f"{1 if length == 1 else length} "
        + "[red]for details - Zero to exit\n"
    )
    try:
        value = int(number)
        if value < 1:
            return
        item: Item = person.initial_credits[value - 1]
        media: Result = transform_item(item["slug"], item["content_type"])
        choose_types(media)
    except (IndexError, ValueError):
        choose_media_by_person(person)


def __rich__() -> Panel:
    grid = Table.grid(expand=True)
    grid.add_column(justify="center", ratio=1)
    grid.add_column(justify="right")
    grid.add_row(
        ":corn::corn::corn:[b] POPCORN SHOW - CLI[/b]:corn::corn::corn:",
        datetime.now().ctime().replace(":", "[blink]:[/]"),
    )
    return Panel(grid, style="red1 on black")


def __footer__(item: ItemMovie | ItemShow) -> Panel:
    grid = Table.grid(expand=True)
    grid.add_column(justify="left", ratio=3)
    grid.add_column(justify="right", ratio=1)
    if item.score_breakdown["content"]["text"]:
        grid.add_row(
            f"[orange1][b]{item.score_breakdown['content']['text']}",
            f"[b][link=https://play.google.com/store/apps/details?id=br.com.icaro.filme][yellow]App Android => [/link]",
        )
    return Panel(grid, style="red1 on black")


def __footer_person__(item: PersonApi) -> Panel:
    grid = Table.grid(expand=True)
    if item.homepage:
        grid.add_column(justify="left", ratio=3)
        grid.add_column(justify="right", ratio=1)
        link = f"[b][orange1]:link:[link={item.homepage}] Site"
        grid.add_row(
            link,
            f"[b][link=https://play.google.com/store/apps/details?id=br.com.icaro.filme][yellow]App Android => [/link]",
        )
    else:
        grid.add_column(justify="right", ratio=1)
        grid.add_row(
            "",
            f"[b][link=https://play.google.com/store/apps/details?id=br.com.icaro.filme][yellow]App Android => [/link]",
        )
    return Panel(grid, style="red1 on black")


def choose_number(list: list[Search], hasError=False):
    item: None
    number = Prompt.ask(
        f"[red]For details, write a number between 1 and {list.__len__()}. Zero to exit\n"
    )
    if hasError or number == "0":
        return

    try:
        number = int(number)
        if number > 0 and number <= list.__len__():
            item = list[number - 1]
        else:
            print("Number off the list.")
            choose_number(list, True)
            return

    except ValueError:
        print("Number Error! - write '0' to exit ")
        choose_number(list, True)
        return

    if item is not None:
        result = transform_item(item.slug, item.type)
        fill_by_type(result)
