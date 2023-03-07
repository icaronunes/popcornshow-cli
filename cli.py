from controller import searchReel
from models.itemSearch import ItemSearch
import typer

app = typer.Typer(help="PopCorn Show")


@app.command(name="search")
def search(name: str,
           year: int = None,
           type: str = typer.Option(None, help="'m' or 's'")):
    print(f"Search for {name} {year}")
    list = searchReel(name, year=year, type=type)
    number = input("For details, type number: ")
    chooseNumber(list, number)


def chooseNumber(list: list[ItemSearch], number: int):
    try:
        item = list[int(number, 10) - 1]
        print(item)
    except ValueError:
        print("Number Error!")


@app.command()
def init():
    print("POPCORN SHOW!")


if __name__ == "__main__":
    app()
