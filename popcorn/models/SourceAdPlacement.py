from models.Links import Links
from models.Creative import Creative


class SourceAdPlacement:
    placement_type: str
    source_id: str
    source_name: str
    access_type: int
    image_url: str
    title_copy: str
    short_deal_copy: str
    long_deal_copy: str
    additional_copy: None
    button_call_to_action: str
    landing_page_link: None
    use_deeplink: bool
    deeplink: str
    inline_position: str
    min_price: float
    creative: Creative
    links: Links

    def __init__(self, placement_type: str, source_id: str, source_name: str, access_type: int, image_url: None, title_copy: str, short_deal_copy: str, long_deal_copy: str, additional_copy: None, button_call_to_action: str, landing_page_link: None, use_deeplink: bool, deeplink: str, inline_position: str, min_price: float, creative: Creative, links: Links) -> None:
        self.placement_type = placement_type
        self.source_id = source_id
        self.source_name = source_name
        self.access_type = access_type
        self.image_url = image_url
        self.title_copy = title_copy
        self.short_deal_copy = short_deal_copy
        self.long_deal_copy = long_deal_copy
        self.additional_copy = additional_copy
        self.button_call_to_action = button_call_to_action
        self.landing_page_link = landing_page_link
        self.use_deeplink = use_deeplink
        self.deeplink = deeplink
        self.inline_position = inline_position
        self.min_price = min_price
        self.creative = creative
        self.links = links
