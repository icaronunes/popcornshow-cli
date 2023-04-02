import sys
import os


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


from cli import app, chooseNumber
from models.Search import Search
from typer.testing import CliRunner


runner = CliRunner()


def test_result_lost_by_show_with_luck():
    result = runner.invoke(app, ["lost", "--year", "2004", "-l"])
    assert result.exit_code == 0
    __details_by_lost(result)


def test_result_lost_by_show_out_luck():
    result = runner.invoke(app, ["lost"], input="7\n")
    assert result.exit_code == 0
    assert 'Title' in result.stdout
    assert 'Index' in result.stdout
    assert 'Title' in result.stdout
    assert 'Release' in result.stdout
    assert 'Type' in result.stdout
    assert 'Online' in result.stdout
    assert '1' in result.stdout
    assert '2' in result.stdout
    assert '3' in result.stdout
    assert '4' in result.stdout
    assert '5' in result.stdout
    assert '6' in result.stdout
    assert '7' in result.stdout
    assert '8' in result.stdout
    __details_by_lost(result)


def test_result_none_name():
    result = runner.invoke(app)
    assert result.exit_code == 2
    assert "Usage:" in result.stdout
    assert "--help" in result.stdout
    assert "Error" in result.stdout
    assert "Missing argument 'NAME'" in result.stdout


def __details_by_lost(result):
    assert "POPCORN SHOW" in result.stdout
    assert "Details" in result.stdout
    assert "Details in Reelgood.com" in result.stdout
    assert "Release" in result.stdout
    assert "Season" in result.stdout
    assert "People" in result.stdout
    assert "Where to Watch" in result.stdout
    assert "Naveen Andrews" in result.stdout
    assert "Sayid Jarrah" in result.stdout


def test_result_lost_by_movie_luck():
    result = runner.invoke(app, ["lost", '-t', 'm', '-l'])
    std = result.stdout
    assert 'Overview' in std
    assert 'Trailers' in std
    assert "Details in Reelgood.com" in result.stdout
    if 'Raiders of the Lost Ark 1981' in std:
        assert 'Steven Spielberg' in std
        assert '1981'

def test_view_foot():
    result = runner.invoke(app, ['lost', '-l', '-t', 's'])
    out = result.stdout
    assert "App Android =>" in out