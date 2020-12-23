from src.rockPaperScissors import CHOICES, print_choices

"""
Tests of the function src.rockPaperScissors.get_player_choice
"""


# The function prints the same item for the player and the computer: Rock
def test_print_rock(capsys):
    print_choices("r", "r")
    captured = capsys.readouterr()
    assert captured.out == "You choose         : Rock\n" \
                           "The computer choose: Rock\n"

# The function prints the same item for the player and the computer: Paper
def test_print_paper(capsys):
    print_choices("p", "p")
    captured = capsys.readouterr()
    assert captured.out == "You choose         : Paper\n" \
                           "The computer choose: Paper\n"

# The function prints the same item for the player and the computer: Scissors
def test_print_scissors(capsys):
    print_choices("s", "s")
    captured = capsys.readouterr()
    assert captured.out == "You choose         : Scissors\n" \
                           "The computer choose: Scissors\n"


# The function prints different items for the player and the computer: Rock and Scissors
def test_print_different_items(capsys):
    print_choices("r", "s")
    captured = capsys.readouterr()
    assert captured.out == "You choose         : Rock\n" \
                           "The computer choose: Scissors\n"
