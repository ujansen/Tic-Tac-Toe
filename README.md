# Tic-Tac-Toe
A tic-tac-toe game with an unbeatable AI, making use of the minimax algorithm from Game Theory

The program first defines a typical 3 x 3 tic-tac-toe board in the form of a 2-D list with each square being assigned a number from 1 to 9
This is followed by the creation of functions that check whether any of the players are in a victorious state or not.

The main work being done in the program is defined in the best_move(board, depth, player) function where the program is using the Minimax Algorithm from Game Theory to maximize its own chances of winning and minimizing the user's chances, based on the current state of the board.

More on Minimax Algorithm can be found here: https://www.javatpoint.com/mini-max-algorithm-in-ai

The second program is 2 AI's playing against each other with one trying to maximize its own and trying to minimize the other's and vice versa.
