from controller import searchReel, getMovie
from tables.table_movie import tableMovie
from tables.table_search import tableSearch
from models.Search import Search
import typer
from utils import BACK

app = typer.Typer(help="PopCorn Show")


@app.command(name="search")
def search(name: str,
           year: int = None,
           type: str = typer.Option(None, '--type', '-t', help="'m' or 's'")):
    list = searchReel(name, year=year, type=type)
    if list:
        tableSearch(list)
        chooseNumber(list)


def chooseNumber(list: list[Search], hasError=False):
    number = input(
        f"For details, write a number between 1 and {list.__len__()} : ")
    item: None
    if (hasError and number == BACK):
        return
    try:
        number = int(number)
        if (number > 0 and number <= list.__len__()):
            item = list[number - 1]
            print(item)
        else:
            print("Number off the list.")
    except ValueError:
        print("Number Error! - write 'back' to exit ")
        chooseNumber(list, True)

    movie = getMovie(item)
    tableMovie(movie)


def init():
    # print("POPCORN SHOW! - CLI") CRIAR TELA DE BOAS VINDAS
    app()


if __name__ == "__main__":
    typer.run(init())
