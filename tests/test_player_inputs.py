from unittest import mock
from src.rockPaperScissors import decide_game, game
import builtins


# Test wrong inputs from player: characters other than "r", "p", or "s"
def test_not_letter(capsys):
    with mock.patch.object(builtins, "input", lambda player: "1"):
        print("Inside the test")
        assert game(True) == "Wrong selection, try again."
