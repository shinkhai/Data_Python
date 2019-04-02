"""
Tests for "Grocery list" program
"""
import copy

from src import grocery_list as interface


_MSG_EXIT = "exit"
_OUTPUT_WELCOME = ("Welcome to Grocery list, "
                   "you can quit by typing 'exit' in the main menu")
_PROMPT_ACTION = "What you wanna do (add/remove/sort/show)?\n"
_PROMPT_ADD_ITEM = "Name of the item to add?\n"
_PROMPT_QUANTITY = "How many?\n"
_OUTPUT_ITEM_NOT_IN_LIST = "{} is not in the list yet..."


def test_base(capsys):
    assert capsys.readouterr().out == "", (
        "Run your program inside the `if __name__ == '__main__'`")


class TestDocstring:

    def test_presence(self):
        assert interface.__doc__ is not None, (
            "You need to write a docstring")

    def test_length(self):
        assert len(interface.__doc__) >= 10, (
            "Your docstring is probably too short.")


# TODO: We're manually mocking `input`
#       We should be using unittest's mock or pytest-mock
class TestBase:

    def setup_method(self, mock_input):
        self._input = input
        self._print = print
        self.prompts = []
        self.output = []

        def mock_input(s):
            self.prompts.append(s)
            return next(self.input_values)

        def mock_output(o):
            self.output.append(copy.deepcopy(o))

        interface.input = mock_input
        interface.print = mock_output

    def teardown_method(self):
        interface.input = self._input
        interface.print = self._print

    def test_welcome_message(self):
        self.input_values = iter(['exit'])

        interface.main()

        assert self.output[0] == _OUTPUT_WELCOME, (
            "Did you print the welcome message?")

    def test_it_prompts(self):
        self.input_values = iter(['exit'])

        interface.main()

        assert len(self.prompts) > 0, "You need to prompt the user to action"

    def test_first_prompt_message(self):
        self.input_values = iter(['exit'])

        interface.main()

        assert self.prompts[0] == _PROMPT_ACTION, (
            "The message of your first prompt is incorrect")

    def test_show_empty(self):
        self.input_values = iter(['show', 'exit'])

        interface.main()

        assert self.output[1] == [], "Check the output for 'show' action"

    def test_add_item(self):
        self.input_values = iter(['add', 'tomatoes', '6', 'exit'])

        interface.main()

        assert self.prompts[1] == _PROMPT_ADD_ITEM, (
            "Check your prompt message for adding an item")

    def test_select_quantity(self):
        self.input_values = iter(['add', 'tomatoes', '6', 'exit'])

        interface.main()

        assert self.prompts[2] == _PROMPT_QUANTITY, (
            "Check your prompt message for selecting quantity")

    def test_show_list_after_adding_an_item(self):
        self.input_values = iter(['add', 'tomatoes', '6', 'exit'])

        interface.main()

        assert len(self.output) >= 1, "After adding an item, show the list"

    def test_list_after_adding_item(self):
        self.input_values = iter(['add', 'tomatoes', '6', 'exit'])

        interface.main()
        expected = [(6, 'tomatoes')]

        assert self.output[1] == expected, "Did you correctly build the list?"

    def test_remove_item(self):
        self.input_values = iter([
            'add', 'tomatoes', '6',
            'remove', 'tomatoes', '2',
            'exit'])

        interface.main()
        expected = [(4, 'tomatoes')]

        assert self.output[2] == expected, (
            "When you remove an existing item, update its quantity")

    def test_remove_non_existing_item(self):
        self.input_values = iter([
            'add', 'tomatoes', '6',
            'remove', 'bananas', '2',
            'exit'])

        interface.main()

        assert self.output[2] == _OUTPUT_ITEM_NOT_IN_LIST.format('bananas'), (
            "Did you correctly build the list?")

    def test_add_second_item(self):
        self.input_values = iter([
            'add', 'tomatoes', '6',
            'add', 'bananas', '8',
            'exit']
        )

        interface.main()

        expected = [(6, 'tomatoes'), (8, 'bananas')]
        assert self.output[2] == expected, (
            "Make sure you append to the list when adding a new element.")

    def test_add_same_item(self):
        self.input_values = iter([
            'add', 'tomatoes', '6',
            'add', 'tomatoes', '2',
            'exit']
        )

        interface.main()

        expected = [(8, 'tomatoes')]

        assert self.output[2] == expected, (
            "When you add an existing item, update its quantity")

    def test_sort_ascending(self):
        self.input_values = iter([
            'add', 'bananas', '8',
            'add', 'tomatoes', '6',
            'sort', 'n',
            'exit']
        )

        interface.main()

        expected = [(6, 'tomatoes'), (8, 'bananas')]
        assert self.output[3] == expected, "Did you correctly sort the list?"

    def test_sort_descending(self):
        self.input_values = iter([
            'add', 'tomatoes', '6',
            'add', 'bananas', '8',
            'sort', 'y',
            'exit']
        )
        interface.main()

        expected = [(8, 'bananas'), (6, 'tomatoes')]

        assert self.output[3] == expected, "Did you correctly sort the list?"

    def test_not_sorted_after_sort(self):
        self.input_values = iter([
            'add', 'tomatoes', '6',
            'add', 'bananas', '8',
            'sort', 'y', 'show',
            'exit']
        )
        interface.main()

        expected = [(6, 'tomatoes'), (8, 'bananas')]
        assert self.output[4] == expected, (
            "When you sort, don't modify the list")
