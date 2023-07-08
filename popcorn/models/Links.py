from typing import Optional


class Links:
    web: str
    ios: Optional[str]
    android: Optional[str]

    def __init__(self, web: str, ios: Optional[str], android: Optional[str]) -> None:
        self.web = web
        self.ios = ios
        self.android = android
