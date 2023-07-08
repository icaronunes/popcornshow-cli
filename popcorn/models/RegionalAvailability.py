class RegionalAvailability:
    it: list[int]
    nl: list[int]
    de: list[int]
    fr: list[int]
    es: list[int]
    gb: list[int]
    au: list[int]
    us: list[int]

    def __init__(
        self,
        it: list[int],
        nl: list[int],
        de: list[int],
        fr: list[int],
        es: list[int],
        gb: list[int],
        au: list[int],
        us: list[int],
    ) -> None:
        self.it = it
        self.nl = nl
        self.de = de
        self.fr = fr
        self.es = es
        self.gb = gb
        self.au = au
        self.us = us
