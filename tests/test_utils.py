from popcorn.utils import format_date, format_date_str, format_type, has_br


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
    assert result == "2006-10-26"


def test_format_date_exception():
    result = format_date("exception")
    assert result is None


def test_format_date_none():
    result = format_date(None)
    assert result is None


def test_has_br_more_15_char():
    text = "qwertyuiopasdfghjklzxcvbnm"
    result = has_br(text.__len__())
    assert result == "\n"


def test_fortmat_type_m():
    result = format_type("m")
    assert result == "Movie"


def test_format_type_s():
    result = format_type("s")
    assert result == "Show"


def test_format_type_not():
    result = format_type("qwert")
    assert result == "- -"
