from math import inf
from random import choice
import time
import platform
from os import system

HUMAN = -1
AI = 1
board = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]

def check_score(board):
    if check_winner(board, HUMAN):
        return -1
    elif check_winner(board, AI):
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
    return check_winner(board, HUMAN) or check_winner(board, AI)

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
    if player == AI:
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

        if player == AI:
            if result[2] > best[2]:
                best = result
        else:
            if result[2] < best[2]:
                best = result

    return best

def clear_screen():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

def print_board(board, ai, human):
    symbols = {
        -1: human,
         1: ai,
         ' ': ' '
    }
    
    line = '---------------'
    print('\n' + line)
    for row in board:
        for spot in row:
            symbol = symbols[spot]
            print (f'| {symbol} |',end='')
        print('\n' + line)

def ai_turn(ai, human):
    depth = len(available_spots(board))

    if depth == 0 or finish(board):
        return

    clear_screen()

    print(f'AI Turn [{ai}]')
    print_board(board, ai, human)

    if depth == 9:
        x = choice([0,1,2])
        y = choice([0,1,2])
    else:
        move = best_move(board, depth, AI)
        x, y = move[0], move[1]

    make_move(x,y,AI)
    time.sleep(1)

def human_turn(ai, human):
    depth = len(available_spots(board))

    if depth == 0 or finish(board):
        return

    move = -1
    available_moves = {
        1:[0,0],2:[0,1],3:[0,2],
        4:[1,0],5:[1,1],6:[1,2],
        7:[2,0],8:[2,1],9:[2,2]
    }
    clear_screen()
    print (f'Human Turn [{human}]')
    print_board(board, ai, human)

    while move < 1 or move > 9:
        try:
            move = int(input('Choose the spot to move to (1-9): '))
            spot = available_moves[move]
            can_move = make_move(spot[0],spot[1],HUMAN)

            if not can_move:
                print('Incorrect move. ')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye. ')
            exit()
        except (KeyError, ValueError):
            print('Incorrect choice. ')

def main():
    play_game = "Y"
    while play_game.upper() == "Y":
        clear_screen()
        human = ''
        ai = ''
        first_move = ''

        while human != 'O' and human != 'X':
            try:
                print('')
                human = input('Choose X or O\nChosen: ').upper()
            except (EOFError, KeyboardInterrupt):
                print('Bye. ')
                exit()
            except (KeyError, ValueError):
                print('Incorrect choice. ')

        if human == 'O':
            ai = 'X'
        else:
            ai = 'O'

        clear_screen()
        while first_move != 'Y' and first_move != 'N':
            try:
                first_move = input('Do you wanna start first? [y/n]: ').upper()
            except (EOFError, KeyboardInterrupt):
                print('Bye. ')
                exit()
            except (KeyError, ValueError):
                print('Incorrect choice. ')

        while len(available_spots(board)) > 0 and not finish(board):
            if first_move == 'N':
                ai_turn(ai, human)
                first_move = ''

            human_turn(ai, human)
            ai_turn(ai, human)

        if check_winner(board, HUMAN):
            clear_screen()
            print (f'Human Turn [{human}]')
            print_board(board, ai, human)
            print ("YOU WIN!")
        elif check_winner(board, AI):
            clear_screen()
            print (f'AI Turn [{ai}]')
            print_board(board, ai, human)
            print ("AI WINS!")
        else:
            clear_screen()
            print_board(board, ai, human)
            print ("DRAW!")

        exit()

if __name__ == '__main__':
    main()
