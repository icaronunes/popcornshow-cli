class TVShowEpisode:
    def __init__(self, data):
        self.id = data["id"]
        self.season_id = data["season_id"]
        self.title = data["title"]
        self.overview = data["overview"]
        self.number = data["number"]
        self.sequence_number = data["sequence_number"]
        self.watched = data["watched"]
        self.has_screenshot = data["has_screenshot"]
        self.aired_at = data["aired_at"]
        self.availability = []
        for a in data["availability"]:
            av = Availability(
                a["rental_cost_hd"],
                a["rental_cost_sd"],
                a["purchase_cost_hd"],
                a["purchase_cost_sd"],
                a["source_id"],
                a["source_name"],
                a["access_type"],
                SourceData(
                    a["source_data"]["links"]["web"],
                    a["source_data"]["links"]["ios"],
                    a["source_data"]["links"]["android"],
                    References(
                        a["source_data"]["references"]["web"]["episode_id"],
                        a["source_data"]["references"]["web"]["show_id"],
                        a["source_data"]["references"]["ios"]["episode_id"],
                        a["source_data"]["references"]["ios"]["show_id"],
                        a["source_data"]["references"]["android"]["episode_id"],
                        a["source_data"]["references"]["android"]["show_id"],
                    ),
                    a["source_data"]["web_link"],
                ),
            )
            self.availability.append(av)


class Availability:
    def __init__(
        self,
        rental_cost_hd,
        rental_cost_sd,
        purchase_cost_hd,
        purchase_cost_sd,
        source_id,
        source_name,
        access_type,
        source_data,
    ):
        self.rental_cost_hd = rental_cost_hd
        self.rental_cost_sd = rental_cost_sd
        self.purchase_cost_hd = purchase_cost_hd
        self.purchase_cost_sd = purchase_cost_sd
        self.source_id = source_id
        self.source_name = source_name
        self.access_type = access_type
        self.source_data = source_data


class SourceData:
    def __init__(self, web, ios, android, references, web_link):
        self.links = Links(web, ios, android)
        self.references = references
        self.web_link = web_link


class Links:
    def __init__(self, web, ios, android):
        self.web = web
        self.ios = ios
        self.android = android


class References:
    def __init__(
        self,
        web_episode_id,
        web_show_id,
        ios_episode_id,
        ios_show_id,
        android_episode_id,
        android_show_id,
    ):
        self.web = WebReferences(web_episode_id, web_show_id)
        self.ios = IOSReferences(ios_episode_id, ios_show_id)
        self.android = AndroidReferences(android_episode_id, android_show_id)


class WebReferences:
    def __init__(self, episode_id, show_id):
        self.episode_id = episode_id
        self.show_id = show_id


class IOSReferences:
    def __init__(self, episode_id, show_id):
        self.episode_id = episode_id
        self.show_id = show_id


class AndroidReferences:
    def __init__(self, episode_id, show_id):
        self.episode_id = episode_id
        self.show_id = show_id
