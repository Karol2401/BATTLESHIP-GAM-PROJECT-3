# Battleships Game


Battleships game is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

The player has the opportunity to defeat the computer by finding its ships on the board before the computer finds user ships. Each ship occupies one grid on the board.

A live version of this game can be found at this link:
https://battleships-game1992.herokuapp.com/

![Different devices creenshot](/assets/images/Screenshot%202023-02-02%20at%2011.55.32.png)

## How to play


Battleships game is based on a popular game that required only a piece of paper and a pen. You can read more about it on https://en.wikipedia.org/wiki/Battleship_(game).

This version of the game requires the player's to enter a name and then generates two game boards for the user and the computer.

The player can see where their ships are, indicated by an @ sign, but cannot see where the computer's ships are.

Missed selections are marked with an X and ship hits with a *.

The player and the computer each round guess where the opponent's ship is located to sink it.

The winner is whoever sinks all enemy ships first.

## Features

### Existing Features

* Random board generation:
  -  Ships are randomly placed on both the player and computer boards.
  - The player cannot see where the computer's ships are.

![Computer and player boards](/assets/images/Screenshot%202023-02-02%20at%2011.27.03.png)

* Play against the computer

* Accepts user input

![Computer and player Guess](/assets/images/Screenshot%202023-02-02%20at%2011.37.45.png)


* Input validation and error-checking
  - You cannot enter coordinates outside the size of the grid
  - You must enter numbers
  - You cannot enter the same guess twice

![Coordinates](/assets/images/Screenshot%202023-02-02%20at%2011.43.16.png)

* Date maintained in class instances

## Data Model

I use Board class as my model. The game create two instances of the Borad class to keep the player's and computer's board.

The Board class store the board size, the number of ships, the position of the ships, the guesses against the board, and details such as the board type(player's board or computer) and the player's game.

In addition, this class has the ability to print the current table and the ships on it, as well as a method for guessing and returning results.

## Testing

I have manually tested this project by doing the following:
* Passed code through a PEP8 linter and confirmed there are no problems.
* Tested in my local terminal and the Code Institute Heroku.

### Bugs

* No missing bugs

### Validator Testing

* PEP8
  - No errors were returned from PEP8online.com

## Deployment

This project was deployed using Code Institute's mock terminal for heroku.

* Steps for deployment:
  - Frok or clone repository
  - Create a new Heroku app
  - Set the buildbacks to Python and NodeJS in that order
  - Link the heroku app to the repository
  - Click Deploy

## Credits
* Code Institute for deployment terminal
* Wikipedia for details of the battleships game
* The basic structure of the code is taken from Portfolio Project Scope "ULTIMATE Battleships" 