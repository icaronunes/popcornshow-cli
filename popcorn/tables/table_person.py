from utils import formatDateStr
from rich.table import Table, box
from api.models.PersonApi import PersonApi

topTablePerson = [
    ':scroll: Name',
    ':date: Birth date',
    ':star: Birth place',
    ':date: Death date'
]

def initTable() -> Table:
    table = Table(
        highlight=True,
        show_header=True,
        show_edge=True,
        expand=True,
        show_lines=True,
        box=box.DOUBLE_EDGE) 
    
    for title in topTablePerson:
        table.add_column(title)
    return table        
 

def __tableItemPerson__(
        table: Table,
        name: str,
        birthdate: str,
        birthplace: str,
        deathdate: str
    ) -> Table:
    table.add_row(
        name,
        birthdate,
        birthplace,
        deathdate)
    return table

def table_details_person(item: PersonApi) -> Table:
    table = __tableItemPerson__(
        table =  initTable(),
        name=item.name,
        birthdate="-- -- --" if item.birthdate is None else formatDateStr(item.birthdate),
        birthplace="" if item.birthplace is None else item.birthplace,
        deathdate="-- -- --" if item.deathdate is None else formatDateStr(item.deathdate)
    )
    return table