from math import inf
from random import choice
import time
import platform
from os import system
import os
import sys

AI_2 = -1
AI_1 = 1

#define the board as a 3x3 2-D list with a bunchy of empty spots
board = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]


#return the value assigned to a winner, if there is one, else return 0 which continues the game
def check_score(board):
    if check_winner(board, AI_2):
        return -1
    elif check_winner(board, AI_1):
        return 1
    else:
        return 0


#checking for equality for 3 symbols
def equals(a,b,c):
    if (a == b and b == c):
        return True


#check for winner horizontally, vertically, and diagonally
def check_winner(board, player):
    for i in range(3):
        if (equals(board[i][0],board[i][1],board[i][2]) and board[i][0] == player):
            return True
    
    for i in range(3):
        if (equals(board[0][i],board[1][i],board[2][i]) and board[0][i] == player):
            return True
    
    if (equals(board[0][0],board[1][1],board[2][2]) and board[0][0] == player):
        return True

    if (equals(board[0][2],board[1][1],board[2][0]) and board[0][2] == player):
        return True
    
    return False


#if game is finished, return the value of the winner
def finish(board):
    return check_winner(board, AI_2) or check_winner(board, AI_1)


#check for spots that are empty and add them to a list
def available_spots(board):
    spots = []
    for x, row in enumerate(board):
        for y, spot in enumerate(row):
            if spot == ' ':
                spots.append([x,y])
    return spots


#check if the specified square is part of the list returned by the previous function
def valid(x, y):
    if [x,y] in available_spots(board):
        return True
    else:
        return False


#the move is made and the symbol is printed on the board, only if the move is deemed valid
def make_move(x, y, player):
    if valid(x, y):
        board[x][y] = player
        return True
    else:
        return False


#calculates the best move
def best_move(board, depth, player):
    if player == AI_1:
        best = [-1, -1, -inf]
    else:
        best = [-1, -1, inf]


    #if there are no more spaces left or the game is over, return the result
    if depth == 0 or finish(board):
        result = check_score(board)
        return [-1, -1, result]

    #recursively call the function to create all branching possibilites (by checking all the available spots)
    for spot in available_spots(board):
        x, y = spot[0], spot[1]
        board[x][y] = player
        result = best_move(board, depth-1, -player)
        board[x][y] = ' '
        result[0], result[1] = x, y

        #if the result returns a 1, this is the best move
        if player == AI_1:
            if result[2] > best[2]:
                best = result

        #if the result returns a -1, this is the best move
        else:
            if result[2] < best[2]:
                best = result

    #return the move to be made
    return best


#clears the screen after every single move is made
def clear():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


#prints out the board in a fashionable manner
def print_board(board, ai_1, ai_2):
    symbols = {
        -1: ai_2,
         1: ai_1,
         ' ': ' '
    }
    
    line = '---------------'
    print('\n' + line)
    for row in board:
        for spot in row:
            symbol = symbols[spot]
            print (f'| {symbol} |',end='')
        print('\n' + line)


#the AI makes the move by calling in the best_move function when the first turn isn't its own
#if the first turn is its own, it randomly chooses a spot
def ai_turn(ai, aii, player):
    depth = len(available_spots(board))

    if depth == 0 or finish(board):
        return

    clear()

    print_board(board, ai, aii)

    if depth == 9:
        x = choice([0,1,2])
        y = choice([0,1,2])
    else:
        move = best_move(board, depth, player)
        x, y = move[0], move[1]

    make_move(x,y,player)
    time.sleep(2)


#main function that controls the flow of the game
def main():
    clear()
    ai_2 = ''
    ai_1 = ''

    ai_2 = choice(['O','X'])

    if ai_2 == 'O':
        ai_1 = 'X'
    else:
        ai_1 = 'O'

    clear()

    while len(available_spots(board)) > 0 and not finish(board):
        ai_turn(ai_1, ai_2, AI_2)
        ai_turn(ai_1, ai_2, AI_1)

    if check_winner(board, AI_2):
        clear()
        print_board(board, ai_1, ai_2)
        print ("AI_2 WINS!")
    elif check_winner(board, AI_1):
        clear()
        print_board(board, ai_1, ai_2)
        print ("AI_1 WINS!")
    else:
        clear()
        print_board(board, ai_1, ai_2)
        print ("DRAW!")
    exit()

if __name__ == '__main__':
    main()
