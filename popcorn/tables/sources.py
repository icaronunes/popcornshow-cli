from rich.columns import Columns
from rich.panel import Panel
from rich.tree import Tree

from popcorn.models.ItemMovie import Availability
from popcorn.models.Seasons import Availability as AvailabilityShow
from popcorn.models.Seasons import Season
from popcorn.models.TVShowEpisode import TVShowEpisode
from popcorn.utils import format_source


def pop_collumns(availabilitys: list[Availability]) -> Columns:
    return Columns(
        [Panel(panel, expand=True, safe_box=True) for panel in source(availabilitys)]
    )


def collumn_seasons(episodes: list[TVShowEpisode], season: list[Season]) -> Columns:
    return Columns(
        [
            Panel(panel, expand=True, safe_box=True)
            for panel in sourceSeason(episodes, season)
        ]
    )


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


def sourceSeason(episodes: list[TVShowEpisode], seasons: list[Season]) -> list[Tree]:
    result = []
    for season in seasons:
        ep = first_ep_for_season(episodes, season)
        source = Tree(
            __getListSourceForSeason(ep, season["number"], season["availability"])
        )
        result.append(source)
    return result


def first_ep_for_season(
    episodes: list[TVShowEpisode], season: Season
) -> TVShowEpisode | None:
    for eps in season["episodes"]:
        if eps:
            try:
                ep = episodes[eps]
                if ep["number"] == 1:
                    return ep
            except:
                return None
        else:
            return None


def __getTitle(availability: Availability) -> str:
    if (
        "source_data" in availability
        and "web_link" in availability["source_data"]
        and "source_name" in availability
    ):
        return f"[b]{format_source(availability['source_name'])}[/b] {__minAndMax(availability)} :link: [i][blue]{availability['source_data']['web_link']}[/i]"
    else:
        return f"[b]{availability['source_name']}[/b]"


def __getListSourceForSeason(
    ep: TVShowEpisode, numberSeason: int, availability: AvailabilityShow
) -> str:
    result = f"Season {numberSeason} Availability | "
    for source in availability["sources"]:
        link = __fistLink(ep, source["source_name"])
        result = result + __createLinkForSeason(source["source_name"], link) + " "
    return result


def __fistLink(ep: TVShowEpisode, source_name: str) -> str:
    try:
        for av in ep["availability"]:
            if av["source_name"] == source_name:
                return av["source_data"]["web_link"]
        return ""
    except:
        return ""


def __createLinkForSeason(source_name: str, link: str) -> str:
    return f":link: [bold blue][link={link}]{format_source(source_name)}[/link][/bold blue]"


def __minAndMax(availability: Availability) -> str:
    values = []
    if "rental_cost_sd" in availability and availability["rental_cost_sd"] is not None:
        values.append(availability["rental_cost_sd"])
    if "rental_cost_hd" in availability and availability["rental_cost_hd"] is not None:
        values.append(availability["rental_cost_hd"])
    if (
        "purchase_cost_sd" in availability
        and availability["purchase_cost_sd"] is not None
    ):
        values.append(availability["purchase_cost_sd"])
    if (
        "purchase_cost_hd" in availability
        and availability["purchase_cost_hd"] is not None
    ):
        values.append(availability["purchase_cost_hd"])
    if values.__len__() == 0:
        return ""
    return f" | :dollar: {min(values)} :moneybag: {max(values)} |"


def __getRentalTree(availability: Availability) -> Tree:
    rental = Tree("Rental")
    if (
        "rental_cost_hd" in availability
        and "rental_cost_hd" in availability
        and availability["rental_cost_sd"] == availability["rental_cost_hd"]
    ):
        rental.add(f":moneybag: {availability['rental_cost_sd']} SD - HD")
    else:
        if "rental_cost_sd" in availability:
            rental.add(f":dollar: {availability['rental_cost_sd']} SD")
        if "rental_cost_hd" in availability:
            rental.add(f":moneybag: {availability['rental_cost_hd']} HD")
    return rental


def __getPurchaseTree(availability: Availability) -> Tree:
    purchase = Tree("Purchase")
    if (
        "purchase_cost_sd" in availability
        and "purchase_cost_hd" in availability
        and availability["purchase_cost_sd"] == availability["purchase_cost_hd"]
    ):
        purchase.add(f":moneybag: {availability['purchase_cost_hd']} SD - HD")
    else:
        if "purchase_cost_sd" in availability:
            purchase.add(f":dollar: {availability['purchase_cost_sd']} SD")
        if "purchase_cost_hd" in availability:
            purchase.add(f":moneybag: {availability['purchase_cost_hd']} HD")
    return purchase
