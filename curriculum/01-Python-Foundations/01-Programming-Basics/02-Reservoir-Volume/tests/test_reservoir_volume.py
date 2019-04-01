"""
Tests for "Reservoir Volume" program
"""
import inspect

from src import reservoir_volume as interface


def test_source():
    source = inspect.getsource(interface.main)
    assert "print(reservoir_volume)" in source, (
        "Did you print out the value of reservoir?")


def test_output(capsys):
    interface.main()
    output = capsys.readouterr().out.split('\n')[0]

    try:
        res = float(output)
    except Exception:
        res = None
    assert res == 447627500.0, "Wrong value for reservoir"
