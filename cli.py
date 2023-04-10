from datetime import datetime
import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.tree import Tree
from controller import transformItem, searchReel, person_reel
from models.ItemMovie import ItemMovie
from models.ItemShow import ItemShow
from models.Search import Search
from tables.table_details import table_details, table_details_person
from tables.tableDetailsShow import table_details_show
from tables.table_search import tableSearch
from tables.people import people, people_biography, person_media

from tables.sources import columns, columnsSeasons
from api.models.Result import Result
from api.models.PersonApi import PersonApi

from utils import BACK, formatDate

app = typer.Typer(help="PopCorn Show")
console = Console()


@app.command(name="search")
def search(name: str,
           year: int = typer.Option(None, '--year', '-y', help="type Year"),
           type: str = typer.Option(None, '--type', '-t', help="'m' or 's'"),
           luck: bool = typer.Option(False, '--luck', '-l')):

    list = searchReel(name, year=year, type=type)
    if list:
        if luck:
            order = sorted(list, key=lambda x: x.imdbStr(), reverse=True)
            result = transformItem(order[0])
            chooseTypes(result)
        else:
            console.print(tableSearch(list))
            chooseNumber(list)
    else:
        typer.echo("Not Found")


@app.command('person')
def testperson():
    result: Result = person_reel('damien-chazelle-1985')
    if result.error is None:
        __showPerson(result.value)
    else:
        console.print(result.error)


def chooseTypes(result: Result):
    if result.error:
        console.print(result.error)
    else:
        fillByType(result)


def fillByType(result: Result):
    if isinstance(result.value, ItemMovie):
        __showMovie(result.value)
    elif isinstance(result.value, ItemShow):
        __showTvshow(result.value)


def __showTvshow(show: ItemShow):

    tree = Tree('')
    tree.add(__rich__())
    details = Tree(
        f":blue_book: [b][blue]Details - {show.title} {formatDate(show.released_on).year}[/b] - :link: [blue][link={show.createUrl()}]Details in Reelgood.com[/link]", expanded=True)
    details.add(table_details_show(show), highlight=False)

    person = Tree(":busts_in_silhouette:[bold][purple] People")
    person.add(people(show.people))

    tree.add(details)
    if person.children.__len__() > 0:
        tree.add(person)
    if show.seasons:
        tv = Tree(
            f':movie_camera: [red][b]Where to Watch: {show.title} [/red]| [yellow]With Season {show.seasons.__len__()}')
        tv.add(columnsSeasons(show.episodes, reversed(show.seasons)),
               expanded=True, highlight=False)
        tree.add(tv)
    tree.add(__footer__(show))
    console.print(tree)


def __showMovie(movie: ItemMovie):
    tree = Tree('')
    tree.add(__rich__())
    details = Tree(
        f":blue_book:[blue][b] Details - {movie.title} {formatDate(movie.released_on).year if formatDate(movie.released_on) != None else '-- --'}[/b] - :link: [blue][link={movie.createUrl()}]Details in Reelgood.com[/link]", expanded=True)
    details.add(table_details(movie), highlight=False)

    person = Tree(":busts_in_silhouette:[bold][purple] People")
    person.add(people(movie.people))

    tree.add(details)
    if person.children.__len__() > 0:
        tree.add(person)
    if movie.availability:
        tv = Tree(f':movie_camera:[red][b] Where to Watch: {movie.title}')
        tv.add(columns(movie.availability),
               expanded=True, highlight=False)
        tree.add(tv)
    tree.add(__footer__(movie))
    console.print(tree)


def __showPerson(person: PersonApi):
    tree = Tree('')
    tree.add(__rich__())
    tree.add(table_details_person(person), highlight=False)
    tree.add(people_biography(person.biography))
    tree.add(person_media(person.initial_credits))
    tree.add(__footer_person__(person))
    console.print(tree)


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
    if item.score_breakdown['content']['text']:
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
        grid.add_row(link,
                     f"[b][link=https://play.google.com/store/apps/details?id=br.com.icaro.filme][yellow]App Android => [/link]",
                     )
    else:
        grid.add_column(justify="right", ratio=1)
        grid.add_row('',
                     f"[b][link=https://play.google.com/store/apps/details?id=br.com.icaro.filme][yellow]App Android => [/link]",
                     )
    return Panel(grid, style="red1 on black")


def chooseNumber(list: list[Search], hasError=False):
    item: None
    number = typer.prompt(
        f"For details, write a number between 1 and {list.__len__()}")
    if (hasError or number == BACK):
        return

    try:
        number = int(number)
        if (number > 0 and number <= list.__len__()):
            item = list[number - 1]
        else:
            print("Number off the list.")
            chooseNumber(list, True)
            return

    except ValueError:
        print("Number Error! - write 'back' to exit ")
        chooseNumber(list, True)
        return

    if item is not None:
        result = transformItem(item)
        fillByType(result)


def init():
    # print("POPCORN SHOW! - CLI") CRIAR TELA DE BOAS VINDAS
    app()


if __name__ == "__main__":
    typer.run(init())
