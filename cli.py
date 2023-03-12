from datetime import datetime
import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
from rich.panel import Panel
from rich.tree import Tree
from controller import getMovie, searchReel
from models.ItemMovie import ItemMovie
from models.Search import Search
from tables.table_movie import tableMovie
from tables.table_search import tableSearch
from tables.people import people
from tables.sources import columns, source

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
            movie = getMovie(order[0])
            showMovie(movie)
        else:
            console.print(tableSearch(list))
            chooseNumber(list)
    else:
        typer.echo("Not Found")


def showMovie(movie: ItemMovie):
    tree = Tree(':corn:')
    tree.add(__rich__())
    details = Tree(
        f":blue_book: Details - [b]{movie.title} {formatDate(movie.released_on).year}[/b] - :link: [blue][link={movie.createUrl()}] Details in Reelgood.com[/link]", expanded=True)
    details.add(tableMovie(movie), highlight=False)

    person = Tree(":busts_in_silhouette: People")
    person.add(people(movie.people))

    tree.add(details)
    if person.children.__len__() > 0:
        tree.add(person)
    if movie.availability:
        tv = Tree(f':movie_camera: Where to Watch: {movie.title}')
        tv.add(columns(movie.availability),
               expanded=True, highlight=False)
        tree.add(tv)
    tree.add(__footer__(movie))
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


def __footer__(movie: ItemMovie) -> Panel:
    grid = Table.grid(expand=True)
    grid.add_column(justify="left", ratio=3)
    grid.add_column(justify="right", ratio=1)
    if movie.score_breakdown['content']['text']:
        grid.add_row(
            f"[orange1][b]{movie.score_breakdown['content']['text']}",
            f"[b][link=https://play.google.com/store/apps/details?id=br.com.icaro.filme][yellow]App Android => [/link]",
        )
    return Panel(grid, style="red1 on black")


def chooseNumber(list: list[Search], hasError=False):
    item: None
    number = typer.prompt(
        f"For details, write a number between 1 and {list.__len__()}")
    if (hasError and number == BACK):
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
        movie = getMovie(item)
        showMovie(movie)


def init():
    # print("POPCORN SHOW! - CLI") CRIAR TELA DE BOAS VINDAS
    app()


if __name__ == "__main__":
    typer.run(init())
