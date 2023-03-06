from typing import Optional
from controller import searchReel
import typer

app = typer.Typer(help="PopCorn Show")


@app.command(name="search")
def search(name: str,
           year: int = None,
           type: str = typer.Option(None, help="'m' or 's'")):
    print(f"Search for {name} {year}")
    searchReel(name, year=year, type=type)


@app.command()
def init():
    print("POPCORN SHOW!")


if __name__ == "__main__":
    app()
