"""
Tests for "Density" program
"""
import inspect

from src import density as interface


def test_source():
    source = inspect.getsource(interface.main)
    assert "print" in source, "Did you print out the result?"


def test_output(capsys):
    interface.main()
    output = capsys.readouterr().out.split('\n')[0]
    assert output == repr(False)
