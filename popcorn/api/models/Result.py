
class Result:
    error: Exception = None
    value: any

    def __init__(self, error = None, value:any = None) -> None:
        self.error = error
        self.value = value
