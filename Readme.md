# An Unbeatable TIC TAC TOE Bot


## Overview
This documentation provides information about the implementation and structure of the Tic Tac Toe game using the Tkinter library in Python. The game allows a player to compete against an AI opponent that makes moves using the minimax algorithm.

## Playing the Game
Download the python file  `ttt.py` and run it in your desired code editor or terminal using the command `python ttt.py`. (If your not aldready in the directory where the python file is stored use instead `python PATH/ttt.py` while replacing PATH with the Path where you downloaded the file)

## Code Explaination

### Introduction
This Tic Tac Toe game is implemented in Python using the Tkinter library for the graphical user interface. The game supports a player-vs-AI mode, where the AI opponent employs the minimax algorithm to make strategic moves.

### Global Variables
* `WIDTH`: Width of each grid box.
* `BOX_LINE_COLOUR`: Color of the lines separating grid boxes.
* `LINE_COLOUR`: Color of X and O lines.
* `POSITIONS_OCCUPIED`: Dictionary to keep track of occupied positions on the board.
* `FULL_BOARD`: Flag indicating whether the board is full.
* `BOARD`: 2D list representing the game board.
* `canvas`: Tkinter Canvas widget for drawing the game board.
* `AI`: Symbol representing the AI player (X or O).
* `HUMAN`: Symbol representing the human player (X or O).

### GUI Setup
`window`: Main Tkinter window configuration.
`setupboard()`: Function to set up the game board with lines and grid.
`drawmove(move, row, col)`: Function to draw X or O on the canvas at a specified position.

### Functions
* `setupboard()` 
Description: Sets up the initial game board with lines and grid.
Parameters: None.
Returns: None.
* `drawmove(move, row, col)` 
Description: Draws either an X or O on the canvas at the specified position.
Parameters:
move: X or O, indicating the player's move.
row: Row index of the move.
col: Column index of the move.
Returns: None.
* `Playerturn() `
Description: Handles the player's turn by binding the canvas to mouse clicks.
Parameters: None.
Returns: None.
* `check_for_full_board()` 
Description: Checks whether the game board is full.
Parameters: None.
Returns: None.
* `equals(a, b, c)`
Description: Checks if three positions on the board have the same symbol (X or O).
Parameters:
a, b, c: Symbols to be compared.
Returns: True if all three symbols are the same, False otherwise.
* `check_for_winner(board)` 
Description: Checks if there is a winner on the current game board.
Parameters:
board: 2D list representing the current game board.
Returns: Symbol of the winner (X or O), or '-' if it's a tie.
* `computerturn()` 
Description: Implements the AI's turn using the minimax algorithm.
Parameters: None.
Returns: None.
* `minimax(board, depth, maximizingPlayer)` 
Description: Implements the minimax algorithm to find the best move for the AI.
Parameters:
board: 2D list representing the current game board.
depth: Current depth in the recursion.
maximizingPlayer: Boolean indicating whether the player is maximizing or minimizing.
Returns: The score of the best move.
* `print_winner(winner)` 
Description: Prints the winner or a tie message on the GUI.
Parameters:
winner: Symbol of the winner (X, O, or '-').
Returns: None.
* `who_goes_first()` 
Description: Randomly selects whether the AI or the human player goes first.
Parameters: None.
Returns: None.