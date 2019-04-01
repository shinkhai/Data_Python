"""
Tests for "Hello world" program
"""
import inspect

from src import hello_world as interface


def test_source():
    source = inspect.getsource(interface.main)
    assert "print(\"Hello, world!\")" in source, (
        "Did you use `print`?")


def test_myoutput(capsys):
    interface.main()
    output = capsys.readouterr().out.split('\n')[0]

    assert output == "Hello, world!"

