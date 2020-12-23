from unittest import mock

from src.rockPaperScissors import game

"""
Tests of the function src.rockPaperScissors.game
"""


# The player does NOT enters a character in the selection - return True
@mock.patch("src.rockPaperScissors.get_player_choice")
def test_wrong_selection(mock_get_player_choice):
    mock_get_player_choice.return_value = -1
    assert game() == True


# The player enters the exit character 'x'
@mock.patch("src.rockPaperScissors.get_player_choice")
def test_x_game(mock_get_player_choice):
    mock_get_player_choice.return_value = "x"
    assert game() == False


# The player enters a correct character in "rps"
@mock.patch("src.rockPaperScissors.get_player_choice")
def test_game_ok(mock_get_player_choice):
    mock_get_player_choice.return_value = "r"
    assert game() == True
