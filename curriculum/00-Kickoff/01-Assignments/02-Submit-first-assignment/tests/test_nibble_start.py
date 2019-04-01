"""demo_spec.py

"""
import inspect
from urllib import request

import pytest

from src import nibble_start as interface


_BASE_GITHUB_URL = "https://github.com/"



def test_base(capsys):
    interface.main()
    try:
        output = capsys.readouterr().out.split('\n')[0]
    except IndexError:
        pytest.fail("Did you print out all the required print statements?")

    assert output == "That's how it starts", "Follow the instructions."


def test_github_username(capsys):
    interface.main()
    try:
        username = capsys.readouterr().out.split('\n')[1]
    except IndexError:
        pytest.fail("Did you print out all the required print statements?")

    assert (username is not None and username != ""), (
        "Print out the github username of your teammate")

    # Checking user exists on github
    github_url = "{}{}".format(_BASE_GITHUB_URL, username)
    try:
        request.urlopen(github_url)
    except Exception:
        pytest.fail(f"The github username '{username}' you printed out is not "
                    "a valid github username (check case)")
