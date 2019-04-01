"""
Test for demo.py
"""
import inspect

import pytest

try:
    from src import demo as interface
    interface_defined = True
except ImportError:
    interface_defined = False


def test_base(capsys):
    interface.main()
    assert capsys.readouterr().out == "Hello, world!\n", (
        "Print out \"Hello, world!\"")
