class Streamability:
    type: str
    text: str

    def __init__(self, type: str, text: str) -> None:
        self.type = type
        self.text = text