from rich.columns import Columns
from rich import print
from rich.console import Group
from rich.panel import Panel
from rich.table import Table
from rich.tree import Tree
from models.ItemMovie import Person
from api.models.SearchApi import Item
from rich.console import Console

works = {
    0: 'Director',
    1: 'Person',
    2: 'Producer',
    3: 'Executive Producer',
    4: 'Writer',
    5: 'Composer',
    6: 'Creator',
    7: '-- -',
    8: '-- -',
    9: '-- -',
    10: '-- -'
}


def people(peoples: list[Person]) -> Columns:
    def chooseType(person: Person) -> str:
        return createProduction(
            person) if person['role_type'] != 1 else createActor(person)

    directory = [Panel(chooseType(people), expand=True) for people in peoples]
    return Columns(directory)


def createProduction(person: Person) -> str:
    return f"[b][green]{person['name']}[/b]\n[red1][i]{works[person['role_type']]}[/i]\n:link: {__create_link(person)}"


def createActor(person: Person) -> str:
    return f"[b][purple]{person['name']}[/b]\n[red1][i]{person['role']}[/i]\n:link: {__create_link(person)}"


def __create_link(person: Person) -> str:
    return f"[blue1][link=https://reelgood.com/person/{person['slug']}]For Details[/link]"


def people_biography(biography: str) -> Panel:
    return Panel(biography)


def person_media(list: list[Item]) -> Columns:
    def chooseType(item) -> str:
        return f"{item['title']} \n{item['released_on']}\n{item['imdb_rating']}"
    directory = [Panel(chooseType(item), expand=True) for item in list]
    return Columns(directory)
