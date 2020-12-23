from src.rockPaperScissors import game

"""
    Main function: prints the instructions of the game and launches it.
    The parameter game_on is used to keep the game going until the player
    decides to quit it.
"""
if __name__ == '__main__':
    print("Game of Rock, Paper, Scissors against the computer.\n"
          "The winner is decided by these rules:\n"
          "\t- Rock blunts scissors\n"
          "\t- Paper covers rock\n"
          "\t- Scissors cut paper")

    # Control variable used to continue or stop the game
    game_on = True
    # Loop with the function game() until game_on returns False
    while game_on:
        game_on = game()
