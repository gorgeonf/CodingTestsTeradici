from src.rockPaperScissors import game

if __name__ == '__main__':
    print("Game of Rock, Paper, Scissors against the computer.\n"
          "The winner is decided by these rules:\n"
          "\t- Rock blunts scissors\n"
          "\t- Paper covers rock\n"
          "\t- Scissors cut paper")

    # Control variable used to continue or stop the game
    game_on = True
    # Loop with the function game until game_on returns False
    while game_on:
        game_on = game()
