from controller import searchReel, getMovie
from tables.table_movie import tableMovie
from tables.table_search import tableSearch
from models.Search import Search
import typer
from utils import BACK

app = typer.Typer(help="PopCorn Show")


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
            tableMovie(movie)
        else:
            tableSearch(list)
            chooseNumber(list)
    else:
        typer.echo("Not Found")


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
        tableMovie(movie)


def init():
    # print("POPCORN SHOW! - CLI") CRIAR TELA DE BOAS VINDAS
    app()


if __name__ == "__main__":
    typer.run(init())
