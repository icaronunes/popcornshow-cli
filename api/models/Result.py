
class Result:
    error: Exception = None
    value: str

    def __init__(self, error = None, value:any = None) -> None:
        self.error = error
        self.value = value
