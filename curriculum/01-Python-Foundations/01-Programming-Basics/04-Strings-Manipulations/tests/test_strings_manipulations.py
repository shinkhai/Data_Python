"""
Tests for "Strings" program
"""
import inspect

import pytest

from src import strings_manipulations as interface


@pytest.fixture(scope="session")
def source():
    yield inspect.getsource(interface.main)


def test_lowercase(source):
    assert "up_string.lower()" in source, (
        "Did you try to lowercase the string")


def test_output_lowercase(capsys):
    interface.main()
    output = capsys.readouterr().out.split('\n')[0]
    expected = "a string with uppercase"
    assert output == expected


def test_length(source):
    assert "len(long_string)" in source, (
        "Did you try to lowercase the string")


def test_output_length(capsys):
    interface.main()
    output = capsys.readouterr().out.split('\n')[1]
    expected = repr(41)
    assert output == expected


def test_output_kinari(capsys):
    interface.main()
    output = capsys.readouterr().out.split('\n')[2]
    expected = ("Kinari accessed the site "
                "http://petshop.com/pets/mammals/cats at 04:50.")
    assert output == expected


def test_print_maria(source):
    assert "print(maria_string.format" in source, (
        "Did you print out `maria_string` using format?")


def test_output_maria(capsys):
    interface.main()
    output = capsys.readouterr().out.split('\n')[3]
    expected = "Maria loves math and statistics."
    assert output == expected
