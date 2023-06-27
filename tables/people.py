from rich.columns import Columns
from rich import print
from rich.console import Group
from rich.panel import Panel
from rich.table import Table
from rich.tree import Tree
from models.ItemMovie import Person
from api.models.SearchApi import Item
from utils import formatDate

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
    def chooseType(idx: int,person: Person) -> str:
        return createProduction(idx,person) if person['role_type'] != 1 else createActor(idx,person)
    directory = [Panel(chooseType(idx,people), expand=True) for idx, people in enumerate(peoples)]
    return Columns(directory)


def createProduction(idx:int,person: Person) -> str:
    return f"#{idx + 1}\n[b][green]{person['name']}[/b]\n[red1][i]{works[person['role_type']]}[/i]\n:link: {__create_link(person)}"


def createActor(idx:int, person: Person) -> str:
    return f"#{idx+ 1 }\n[b][purple]{person['name']}[/b]\n[red1][i]{person['role']}[/i]\n:link: {__create_link(person)}"


def __create_link(person: Person) -> str:
    return f"[blue1][link=https://reelgood.com/person/{person['slug']}]For Details[/link]"


def people_biography(biography: str|None) -> Panel:
    return Panel(biography)


def person_media(list: list[Item]) -> Columns:
    def chooseType(idx: int, item: Item) -> str:
        return f"#{idx + 1}\n[red]{item['title']} \n[green]{formatDate(item['released_on']).date()}\n[yellow]{item['imdb_rating']}"
    directory = [Panel(chooseType(idx,item), expand=True) for idx, item in enumerate(list)]
    return Columns(directory)
