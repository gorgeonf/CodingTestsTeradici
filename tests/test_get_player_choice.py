from unittest import mock
from src.rockPaperScissors import get_player_choice, CHOICES

"""
Tests of the function src.rockPaperScissors.get_player_choice
"""


# The function does NOT receives a letter
def test_not_letter():
    with mock.patch('builtins.input', return_value='12'):
        assert get_player_choice() == -1


# The function does NOT receives a character in the selection
def test_other_letter():
    with mock.patch('builtins.input', return_value='f'):
        assert get_player_choice() == -1


# The function receives an empty character
def test_exit():
    with mock.patch('builtins.input', return_value=''):
        assert get_player_choice() == -1


# The function receives the exit character
def test_exit():
    with mock.patch('builtins.input', return_value='x'):
        assert get_player_choice() == 'x'


# The function receives the proper letters
def test_choices():
    for letter in CHOICES:
        with mock.patch('builtins.input', return_value=letter):
            assert get_player_choice() == letter
