# Game: Rock, Paper, Scissors
In this project you will make a Rock, Paper, Scissors game and play against the computer. The winner is decided by these rules:

  - Rock blunts scissors
  - Paper covers rock
  - Scissors cut paper


  * First, let the player choose Rock, Paper or Scissors by typing the letter ‘r’, ‘p’ or ‘s’;
  * Then computers turn;
  * Decide game win, lose or draw, print choice of both sides

  1. Use python to implement the game play
  2. Write unit tests with pytest "Pytest is a mature full-featured Python testing tool that helps you write better programs" - https://docs.pytest.org/en/latest/

## Docker file
You are required to create a Dockerfile that allows us to build a docker container and execute the tool with docker run without having any dependencies other than docker installed, the following is what a user should do to run the application or tests:

  * docker run -it pytest -v should execute the unit tests
  * docker run -it should execute the app

## How to submit your application
Please use one of the following methods to share your solution with us:

  * The preferred way is to create a repo on github or gitlab and share the link with us
  * Zip all your solution and send it to us via email
  * Share it using google drive or something similar

## What we are looking for
  * Clean, maintainable and working code
  * Comments if/where appropriate
  * Ability to write unit tests and mock external services
  * Ability to use and deploy in containers
  * Readme file describing how to run the application and unit tests
