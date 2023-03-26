class Season:
    def __init__(self, id, number, has_poster, aired_at, completed_at, episodes_unwatched, availability, episodes):
        self.id = id
        self.number = number
        self.has_poster = has_poster
        self.aired_at = aired_at
        self.completed_at = completed_at
        self.episodes_unwatched = episodes_unwatched
        self.availability = availability
        self.episodes = episodes

class Availability:
    def __init__(self, purchase_available, sources):
        self.purchase_available = purchase_available
        self.sources = sources

class Source:
    def __init__(self, source_name, access_type):
        self.source_name = source_name
        self.access_type = access_type
