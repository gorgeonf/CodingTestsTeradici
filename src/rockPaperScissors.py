# Rock, Paper, Scissors game and play against the computer.
# The winner is decided by these rules:
#   - Rock blunts scissors
#   - Paper covers rock
#   - Scissors cut paper
#
# First, let the player choose Rock, Paper or Scissors by typing the letter ‘r’, ‘p’ or ‘s’;
# Then computers turn;
# Decide game win, lose or draw, print choice of both sides

from random import randint

# Choices proposed to the player
# The first three elements are the letters used for the items (in lower case then upper case)
# The last two elements are used to exit the game (in lower case then upper case)
CHOICES = "rpsRPSxX"

# Matches with the letter selected and word of the item
PRINT_CHOICES = {"p": "Paper", "r": "Rock", "s": "Scissors"}


def print_choices(player, computer):
    """

    :param player: choice of the player
    :param computer: choice of the computer (created with random)
    :return:
    """
    print("You choose         :", PRINT_CHOICES[player])
    print("The computer choose:", PRINT_CHOICES[computer])


def decide_game(player, computer):
    """
    Evaluates both choices from the player and the computer
    and decide the results
    :param player: choice of the player between r, p or s.
    :param computer: choice of the computer (created with random)
    :return:
    """
    # Same pick for both players leads to a tie
    if player == computer:
        print("\tDRAW!")

    # If player picks Rock
    if player == CHOICES[0]:
        if computer == "s":
            print("\tRock blunts scissors", end=" ")
            print("YOU WIN!")
        elif computer == "p":
            print("\tPaper covers rock", end=" ")
            print("YOU LOSE!")

    # If player picks Paper
    if player == CHOICES[1]:
        if computer == "r":
            print("\tPaper covers rock", end=" ")
            print("YOU WIN!")
        elif computer == "s":
            print("\tScissors cut paper", end=" ")
            print("YOU LOSE!")

    # If player picks Scissors
    if player == CHOICES[2]:
        if computer == "p":
            print("\tScissors cut paper", end=" ")
            print("YOU WIN!")
        elif computer == "r":
            print("\tRock blunts scissors", end=" ")
            print("YOU LOSE!")


def game(game_on):
    """

    :param game_on: parameter for the while loop, set to True
    :return:
    """
    while game_on:

        # We ask the user for a choice
        player = input("\nMake your selection\nr: Rock p: Paper s: Scissors\t(x) Exit\n")

        # If the player enters a character not in the proposed choices
        if player not in CHOICES:
            print("Wrong selection, try again.")
            continue

        # If the player enter the exit key the while loop and the game end
        if player in CHOICES[-2:]:
            print("Leaving the game...")
            break

        # The computer picks a random integer between 0 and 2
        # We then select a letter using the number as the index in CHOICES
        computer = CHOICES[randint(0, 2)]

        # Display the two picks
        print_choices(player.lower(), computer)

        # Call to decide_game to print the result
        decide_game(player.lower(), computer)
