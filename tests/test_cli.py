import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


from typer.testing import CliRunner

from popcorn.cli import app
from popcorn.models.Search import Search

runner = CliRunner()
APP_CURRENT_RUNNER = 1


def test_result_lost_by_show_with_luck():
    result = runner.invoke(app, ["lost", "--year", "2004", "-l"])
    __details_by_lost(result)


def test_result_breaking_bad_by_show_out_luck():
    result = runner.invoke(app, ["breaking bad", "-t", "s"], input="1\n")
    assert result.exit_code == APP_CURRENT_RUNNER
    assert "Title" in result.stdout
    assert "Index" in result.stdout
    assert "Title" in result.stdout
    assert "Release" in result.stdout
    assert "Type" in result.stdout
    assert "Online" in result.stdout
    assert "1" in result.stdout
    assert "2" in result.stdout
    assert "3" in result.stdout
    assert "4" in result.stdout
    assert "5" in result.stdout
    assert "6" in result.stdout
    assert "7" in result.stdout
    assert "8" in result.stdout
    assert "POPCORN SHOW" in result.stdout
    assert "Details" in result.stdout
    assert "Details in Reelgood.com" in result.stdout
    assert "Release" in result.stdout
    assert "Season" in result.stdout
    assert "People" in result.stdout
    assert "Where to Watch" in result.stdout
    assert "Bryan Cranston" in result.stdout
    assert "Aaron Paul" in result.stdout


def test_result_breaking_bad_by_show_out_luck_choose_out_number():
    result = runner.invoke(app, ["breaking bad", "-t", "s"], input="51\n")
    assert (
        "Number off the list.\nFor details, write a number between 1 and"
        in result.output
    )
    assert "Zero to exit" in result.stdout


def test_result_none_name():
    result = runner.invoke(app)
    assert result.exit_code == 2
    assert "Usage:" in result.stdout
    assert "help" in result.stdout
    assert "Error" in result.stdout
    assert "Missing argument 'NAME'" in result.stdout


def test_result_lost_by_movie_luck():
    result = runner.invoke(app, ["lost", "-t", "m", "-l"])
    std = result.stdout
    assert "Overview" in std
    assert "Trailers" in std
    assert "Time" in std
    assert "IMDB" in std
    assert "Trailers" in std
    assert "Details" in std
    if "Raiders of the Lost Ark 1981" in std:
        assert "Steven Spielberg" in std
        assert "Harrison Ford" in std
        assert "1981"


def test_view_foot():
    result = runner.invoke(app, ["lost", "-l", "-t", "s"])
    out = result.stdout
    assert "App Android =>" in out


def __details_by_lost(result):
    assert result.exit_code == APP_CURRENT_RUNNER
    assert "POPCORN SHOW" in result.stdout
    assert "Details" in result.stdout
    assert "Details in Reelgood.com" in result.stdout
    assert "Release" in result.stdout
    assert "Season" in result.stdout
    assert "People" in result.stdout
    assert "Where to Watch" in result.stdout
    assert "Naveen Andrews" in result.stdout
    assert "Sayid Jarrah" in result.stdout
