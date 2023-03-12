from rich.tree import Tree
from rich.columns import Columns
from rich.panel import Panel
from utils import formatSource

from models.ItemMovie import Availability


def columns(availabilitys: list[Availability]) -> Columns:
    return Columns([Panel(panel, expand=True, safe_box=True) for panel in source(availabilitys)])


def source(availabilitys: list[Availability]) -> list[Tree]:
    result = []
    for availability in availabilitys:


        source = Tree(__getTitle(availability=availability))

        # removido node com valores - adicionado na linha de titulo
        # rental = __getRentalTree(availability=availability)
        # purchase = __getPurchaseTree(availability=availability)

        # if purchase.children.__len__() > 0:
        #     source.add(purchase)
        # if rental.children.__len__() > 0:
        #     source.add(rental)

        result.append(source)
    return result


def __getTitle(availability: Availability) -> str:
    if 'source_data' in availability and 'web_link' in availability['source_data'] and 'source_name' in availability:
        return f"[b]{formatSource(availability['source_name'])}[/b] {__minAndMax(availability)} :link: [i][blue]{availability['source_data']['web_link']}[/i]"
    else:
        return f"[b]{availability['source_name']}[/b]"


def __minAndMax(availability: Availability) -> str:
    values = []
    if "rental_cost_sd" in availability and availability['rental_cost_sd'] is not None:
        values.append(availability['rental_cost_sd'])
    if "rental_cost_hd" in availability and availability['rental_cost_hd'] is not None:
        values.append(availability['rental_cost_hd'])
    if "purchase_cost_sd" in availability and availability['purchase_cost_sd'] is not None:
        values.append(availability['purchase_cost_sd'])
    if "purchase_cost_hd" in availability and availability['purchase_cost_hd'] is not None:
        values.append(availability['purchase_cost_hd'])
    if values.__len__() == 0:
        return ''
    return f" | :dollar: {min(values)} :moneybag: {max(values)} |"


def __getRentalTree(availability: Availability) -> Tree:
    rental = Tree("Rental")
    if "rental_cost_hd" in availability and "rental_cost_hd" in availability and availability['rental_cost_sd'] == availability['rental_cost_hd']:
        rental.add(f":moneybag: {availability['rental_cost_sd']} SD - HD")
    else:
        if "rental_cost_sd" in availability:
            rental.add(f":dollar: {availability['rental_cost_sd']} SD")
        if "rental_cost_hd" in availability:
            rental.add(f":moneybag: {availability['rental_cost_hd']} HD")
    return rental


def __getPurchaseTree(availability: Availability) -> Tree:
    purchase = Tree("Purchase")
    if "purchase_cost_sd" in availability and "purchase_cost_hd" in availability and availability['purchase_cost_sd'] == availability['purchase_cost_hd']:
        purchase.add(f":moneybag: {availability['purchase_cost_hd']} SD - HD")
    else:
        if "purchase_cost_sd" in availability:
            purchase.add(f":dollar: {availability['purchase_cost_sd']} SD")
        if "purchase_cost_hd" in availability:
            purchase.add(f":moneybag: {availability['purchase_cost_hd']} HD")
    return purchase
