class Creative:
    id: int
    campaign_name: str
    campaign_id: int
    advertiser_id: int
    ad_creative_type_id: int
    source_id: str
    image_override: None
    external_data: None
    links: None
    on_services: bool

    def __init__(
        self,
        id: int,
        campaign_name: str,
        campaign_id: int,
        advertiser_id: int,
        ad_creative_type_id: int,
        source_id: str,
        image_override: None,
        external_data: None,
        links: None,
        on_services: bool,
    ) -> None:
        self.id = id
        self.campaign_name = campaign_name
        self.campaign_id = campaign_id
        self.advertiser_id = advertiser_id
        self.ad_creative_type_id = ad_creative_type_id
        self.source_id = source_id
        self.image_override = image_override
        self.external_data = external_data
        self.links = links
        self.on_services = on_services
