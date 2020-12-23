from unittest import mock
from src.rockPaperScissors import game

"""
Tests of the function src.rockPaperScissors.game
"""


# The player does NOT enter a character in the selection - game returns True
@mock.patch("src.rockPaperScissors.get_player_choice")
def test_wrong_selection(mock_get_player_choice):
    mock_get_player_choice.return_value = -1
    assert game()


# The player enters the exit character 'x' - game returns False
@mock.patch("src.rockPaperScissors.get_player_choice")
def test_x_game(mock_get_player_choice):
    mock_get_player_choice.return_value = "x"
    assert not game()


# The player enters the exit character 'x' - game prints a message
@mock.patch("src.rockPaperScissors.get_player_choice")
def test_x_game_print(mock_get_player_choice, capsys):
    mock_get_player_choice.return_value = "x"
    game()
    captured = capsys.readouterr()
    assert captured.out == "Leaving the game...\n"


# The player enters a correct character in "rps" - game returns True
@mock.patch("src.rockPaperScissors.get_player_choice")
def test_game_played(mock_get_player_choice):
    mock_get_player_choice.return_value = "r"
    assert game()
