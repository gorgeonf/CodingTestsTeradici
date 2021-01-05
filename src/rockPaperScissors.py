from random import randint

from src.constants import CHOICES, PRINT_CHOICES


def get_player_choice():
    """
    Asks the user for a choice and checks its validity
    within the proposed choices (cf. CHOICES)
    The character will be compared and returned using the lower case

    Returns:
        The text entered by the player if the choice is valid
        or -1 if the choice is incorrect
    """
    # Get the player input
    player = input(
        "\nMake your selection\nRock: 'r'  Paper: 'p'  Scissors: 's'\t'x' Exit\n")
    # If the player enters a character in the selection we return it (and we put it in lower case)
    if player.lower() in list(CHOICES):
        return player.lower()
    # If the character is not in the proposed choice
    else:
        print("*** Wrong selection, try again. ***")
        # We return a control value to be interpreted in the while loop of game()
        return -1


def print_choices(player, computer):
    """
    Prints the items picked by the player and the computer in plain letters using PRINT_CHOICES

    Parameters:
        player: choice of the player
        computer: choice of the computer (created with random)
    """
    print("You choose         :", PRINT_CHOICES[player])
    print("The computer choose:", PRINT_CHOICES[computer])


def decide_game(player, computer):
    """
    Evaluates both choices from the player and the computer,
    and decides and prints the results.

    Parameters
        player: choice of the player between r, p or s.
        computer: choice of the computer (created with random)
    """
    # The player and computer picks the same item: it is a tie
    if player == computer:
        print("\tSame item picked ---> DRAW!")

    # The player picks Rock
    if player == CHOICES[0]:
        # Computer picks Scissors
        if computer == "s":
            print("\tRock blunts scissors", end=" ")
            print("---> YOU WIN!")
        # Computer picks Paper
        elif computer == "p":
            print("\tPaper covers rock", end=" ")
            print("---> YOU LOSE!")

    # The player picks Paper
    if player == CHOICES[1]:
        # Computer picks Rock
        if computer == "r":
            print("\tPaper covers rock", end=" ")
            print("---> YOU WIN!")
        # Computer picks Scissors
        elif computer == "s":
            print("\tScissors cut paper", end=" ")
            print("---> YOU LOSE!")

    # The player picks Scissors
    if player == CHOICES[2]:
        # Computer picks Paper
        if computer == "p":
            print("\tScissors cut paper", end=" ")
            print("---> YOU WIN!")
        # Computer picks Rock
        elif computer == "r":
            print("\tRock blunts scissors", end=" ")
            print("---> YOU LOSE!")


def game():
    """
    Prompts the player to pick an item ('r', 'p' or 's').
    The computer then randomly picks an item and both choices are displayed.
    The winner is decided and the results are displayed.
    Finally a boolean is returned to determine if the game continues or not.

    Returns:
        True to ask the user for another input
        or False if the user entered the exit character x or X
    """
    # Get input form the player and check its validity
    player = get_player_choice()

    # If the player enters a character is not in the proposed choices
    if player == -1:
        # Wrong selection, the game will restart
        return True

    # If the player enter the exit key the while loop and the game end
    if player == CHOICES[-1]:
        print("Leaving the game...")
        return False

    # The computer picks a random integer between 0 and 2
    # We then select a letter using the number as the index in CHOICES
    computer = CHOICES[randint(0, 2)]

    # Display of the two picks
    print_choices(player, computer)

    # Pick of the winner and print of the result
    decide_game(player, computer)

    # The game can continue
    return True
