from src.rockPaperScissors import decide_game, game


# Tests of the function decide_game

# Tests of the player choosing rock
def test_rock_rock(capsys):
    decide_game("r", "r")
    captured = capsys.readouterr()
    assert captured.out == "\tDRAW!\n"


def test_rock_paper(capsys):
    decide_game("r", "p")
    captured = capsys.readouterr()
    assert captured.out == "\tPaper covers rock YOU LOSE!\n"


def test_rock_scissors(capsys):
    decide_game("r", "s")
    captured = capsys.readouterr()
    assert captured.out == "\tRock blunts scissors YOU WIN!\n"


# Test of the player choosing paper
def test_paper_paper(capsys):
    decide_game("p", "p")
    captured = capsys.readouterr()
    assert captured.out == "\tDRAW!\n"


def test_paper_rock(capsys):
    decide_game("p", "r")
    captured = capsys.readouterr()
    assert captured.out == "\tPaper covers rock YOU WIN!\n"


def test_paper_scissors(capsys):
    decide_game("p", "s")
    captured = capsys.readouterr()
    assert captured.out == "\tScissors cut paper YOU LOSE!\n"


# Test of the player choosing scissors
def test_scissors_scissors(capsys):
    decide_game("s", "s")
    captured = capsys.readouterr()
    assert captured.out == "\tDRAW!\n"


def test_scissors_rock(capsys):
    decide_game("s", "r")
    captured = capsys.readouterr()
    assert captured.out == "\tRock blunts scissors YOU LOSE!\n"


def test_scissors_paper(capsys):
    decide_game("s", "p")
    captured = capsys.readouterr()
    assert captured.out == "\tScissors cut paper YOU WIN!\n"
