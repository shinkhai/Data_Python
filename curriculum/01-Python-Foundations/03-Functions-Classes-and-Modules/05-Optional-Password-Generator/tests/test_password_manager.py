"""
Tests for generate_password
"""
import pytest

from src.password_manager import PasswordManager, PasswordRecord


@pytest.fixture(params=[PasswordManager, PasswordRecord])
def cls(request):
    return request.param


def test_docstrings(cls):
    assert cls.__doc__ is not None, (
        f"{cls.__name__} doesn't have a docstring")


def test_it_should_implement_init(cls):
    assert cls.__init__ is not object.__init__, (
        f"{cls.__name__} does not implement the __init__ method")


class TestPasswordRecord:

    def test_init(self):
        PasswordRecord("nibble.ai", password="huzheazebzae"), (
            "There is a problem with your implementation, check that "
            "you implemented the right arguments"
        )

    def test_init_with_default(self):
        PasswordRecord("nibble.ai"), (
            "password should be an optional parameter")

    def test_password_should_be_different(self):
        pw_1 = PasswordRecord("nibble.ai")
        pw_2 = PasswordRecord("another_website.com")
        assert pw_1.password != pw_2.password, (
            "New password should be randomly generated")


class TestPasswordManager:

    def test_empty_passwords_list_on_init(self):
        pw_manager = PasswordManager()
        assert (isinstance(pw_manager.passwords, list) and
                len(pw_manager.passwords) == 0), (
                    "Your password manager should start with an empty list of "
                    "passwords.")

    def test_has_add_password_method(self):
        assert hasattr(PasswordManager, "add_password"), (
            f"{cls.__name__} should implement a `add_password` method")

    def test_add_password_should_add_a_password_to_the_list(self):
        pw_manager = PasswordManager()
        pw_manager.add_password("nibble.ai")
        assert len(pw_manager.passwords) == 1

    @pytest.mark.parametrize("record", [
        ('nibble.ai',),
        (PasswordRecord('nibble.ai', password='PASSWORD'),)
    ])
    def test_added_password_should_be_a_password_record(self, record):
        pw_manager = PasswordManager()
        pw_manager.add_password(*record)
        assert isinstance(pw_manager.passwords[0], PasswordRecord), (
            f"You should store passwords as PasswordRecord")
