from popcorn.utils import (
    __hasBr,
    format_date,
    format_date_str,
    format_full_date,
    formatType,
)


def test_format_data_str_none():
    text = None
    result = format_date_str(text)
    assert "--" == result


def test_format_date_str_except():
    text = "what!"
    result = format_date_str(text)
    assert "-- -- --" == result


def test_format_date_str_ok():
    text = "2006-10-26T00:00:00Z"
    result = format_date_str(text)
    result == "2006-10-26"


def test_format_date_exception():
    result = format_date("exception")
    result is None


def test_format_date_none():
    result = format_date(None)
    result is None


def test_format_full_date_none():
    result = format_full_date(None)
    result = "- -"


def test_format_full_date_ok():
    full_date = "2006-10-26T00:00:00Z"
    result = format_full_date(full_date)
    result = "oqueeh"


def test_has_br_more_15_char():
    text = "qwertyuiopasdfghjklzxcvbnm"
    result = __hasBr(text.__len__())
    result == "\n"


def test_fortmat_type_m():
    result = formatType("m")
    result == "Movie"


def test_format_type_s():
    result = formatType("s")
    result == "Show"


def test_format_type_not():
    result = formatType("qwert")
    result == "- -"
