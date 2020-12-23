from src.rockPaperScissors import decide_game

"""
Tests of the function src.rockPaperScissors.decide_game
"""


# Player picks Rock - Computer picks Rock
def test_rock_rock(capsys):
    decide_game("r", "r")
    captured = capsys.readouterr()
    assert captured.out == "\tSame item picked ---> DRAW!\n"


# Player picks Rock - Computer picks Paper
def test_rock_paper(capsys):
    decide_game("r", "p")
    captured = capsys.readouterr()
    assert captured.out == "\tPaper covers rock ---> YOU LOSE!\n"


# Player picks Rock - Computer picks Scissors
def test_rock_scissors(capsys):
    decide_game("r", "s")
    captured = capsys.readouterr()
    assert captured.out == "\tRock blunts scissors ---> YOU WIN!\n"


# Player picks Paper - Computer picks Paper
def test_paper_paper(capsys):
    decide_game("p", "p")
    captured = capsys.readouterr()
    assert captured.out == "\tSame item picked ---> DRAW!\n"


# Player picks paper - Computer picks Rock
def test_paper_rock(capsys):
    decide_game("p", "r")
    captured = capsys.readouterr()
    assert captured.out == "\tPaper covers rock ---> YOU WIN!\n"


# Player picks Paper - Computer picks Scissors
def test_paper_scissors(capsys):
    decide_game("p", "s")
    captured = capsys.readouterr()
    assert captured.out == "\tScissors cut paper ---> YOU LOSE!\n"


# Player picks Scissors - Computer picks Scissors
def test_scissors_scissors(capsys):
    decide_game("s", "s")
    captured = capsys.readouterr()
    assert captured.out == "\tSame item picked ---> DRAW!\n"


# Player picks Scissors - Computer picks Rock
def test_scissors_rock(capsys):
    decide_game("s", "r")
    captured = capsys.readouterr()
    assert captured.out == "\tRock blunts scissors ---> YOU LOSE!\n"


# Player picks Scissors - Computer picks Paper
def test_scissors_paper(capsys):
    decide_game("s", "p")
    captured = capsys.readouterr()
    assert captured.out == "\tScissors cut paper ---> YOU WIN!\n"
