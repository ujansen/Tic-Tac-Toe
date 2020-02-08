from math import inf
from random import choice
import time
import platform
from os import system
import os
import sys

AI_2 = -1
AI_1 = 1
board = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]

def check_score(board):
    if check_winner(board, AI_2):
        return -1
    elif check_winner(board, AI_1):
        return 1
    else:
        return 0

def equals(a,b,c):
    if (a == b and b == c):
        return True

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

def finish(board):
    return check_winner(board, AI_2) or check_winner(board, AI_1)

def available_spots(board):
    spots = []
    for x, row in enumerate(board):
        for y, spot in enumerate(row):
            if spot == ' ':
                spots.append([x,y])
    return spots

def valid(x, y):
    if [x,y] in available_spots(board):
        return True
    else:
        return False

def make_move(x, y, player):
    if valid(x, y):
        board[x][y] = player
        return True
    else:
        return False

def best_move(board, depth, player):
    if player == AI_1:
        best = [-1, -1, -inf]
    else:
        best = [-1, -1, inf]

    if depth == 0 or finish(board):
        result = check_score(board)
        return [-1, -1, result]

    for spot in available_spots(board):
        x, y = spot[0], spot[1]
        board[x][y] = player
        result = best_move(board, depth-1, -player)
        board[x][y] = ' '
        result[0], result[1] = x, y

        if player == AI_1:
            if result[2] > best[2]:
                best = result
        else:
            if result[2] < best[2]:
                best = result

    return best

def clear():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

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