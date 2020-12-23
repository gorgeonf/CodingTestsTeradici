from unittest import mock
from src.rockPaperScissors import get_player_choice

"""
Tests of the function src.rockPaperScissors.get_player_choice
"""


# The function receives the proper letters: 'r', 'p' or 's' in lower case
def test_choices():
    for letter in "rps":
        with mock.patch('builtins.input', return_value=letter):
            assert get_player_choice() == letter.lower()


# The function receives the proper letters: 'r', 'p' or 's' in upper case
# It returns the same letter in lower case
def test_choices_upper():
    for letter in "RPS":
        with mock.patch('builtins.input', return_value=letter):
            assert get_player_choice() == letter.lower()


# The function receives more than one letter
def test_multiple_letters():
    with mock.patch('builtins.input', return_value='rp'):
        assert get_player_choice() == -1


# The function does NOT receive a letter - test of the return value
def test_not_letter():
    with mock.patch('builtins.input', return_value='2'):
        assert get_player_choice() == -1


# The function does NOT receive a character in the selection
def test_other_letter():
    with mock.patch('builtins.input', return_value='f'):
        assert get_player_choice() == -1


# The function receives an empty character
def test_empty():
    with mock.patch('builtins.input', return_value=''):
        assert get_player_choice() == -1


# The function does NOT receive a proper character - test of the print
def test_incorrect_input(capsys):
    with mock.patch('builtins.input', return_value='2'):
        get_player_choice()
        captured = capsys.readouterr()
        assert captured.out == "*** Wrong selection, try again. ***\n"


# The function receives the exit character in lower case
def test_exit_x():
    with mock.patch('builtins.input', return_value='x'):
        assert get_player_choice() == 'x'


# The function receives the exit character in upper case
def test_exit_upper():
    with mock.patch('builtins.input', return_value='X'):
        assert get_player_choice() == 'x'
