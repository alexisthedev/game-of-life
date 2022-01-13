"""Conway\'s Game of Life."""

from math import isqrt
from time import sleep

def board(n): # Creates the game board
    board = {}
    for i in range(n):
        for j in range(n):
            board[(i, j)] = False
    return board

def is_alive(board, p): # Checks if given coordinates (tuple p) point to an alive board cell
    return board[p]

def set_alive(board, p, alive): # Creates or kills an alive cell in given coordinates (tuple p)
    board[p] = alive
    
def get_size(board): # Returns game board's side length
    return isqrt(len(board))

def copy_board(board): # Returns a copy of the game board
    return board.copy()

def get_iterator(board): # Returns a list of tuples of coordinates and the state of the cell they point to
    ls = []
    n = get_size(board)
    for i in range(n):
        for j in range(n):
            ls.append(((i, j), board[(i,j)]))
    return ls

def print_board(board): # Prints the game board
    n = get_size(board)
    row = ''
    for cell in get_iterator(board):
        if cell[1]:
            row += chr(11035)
        else:
            row += chr(11036)

        if cell[0][1] == n-1:
            print(row)
            row = ''

def neighbors(p): # Returns set of neighbor coordinates (does not check if they exist in board)
    return {(p[0]-1, p[1]), (p[0]+1, p[1]), (p[0], p[1]+1), (p[0], p[1]-1), (p[0]-1, p[1]+1), (p[0]+1, p[1]+1), (p[0]+1, p[1]-1), (p[0]-1, p[1]-1)}

def place_blinker(board, p = (0,0)): # Places blinker formation in board coordinates (default 0,0)
    if p in board:
        board[p]=True

    if (p[0]+1, p[1]) in board:
        board[(p[0]+1, p[1])] = True

    if (p[0]+2, p[1]) in board:
        board[(p[0]+2, p[1])] = True

def place_glider(board, p = (0,0)): # Places glider formation in board coordinates (default 0,0)
    a = (p[0]+1, p[1])
    b = (p[0]+1, p[1]+2)
    c = (p[0]+2, p[1]+1)
    d = (p[0]+2, p[1]+2)
    e = (p[0], p[1]+2)

    if a in board:
        board[a] = True
    if b in board:
        board[b] = True
    if c in board:
        board[c] = True
    if d in board:
        board[d] = True
    if e in board:
        board[e] = True

def tick(board): # Simulates one generation according to game rules
    temp = copy_board(board)
    near = []
    alive_count = 0
    for cell in get_iterator(temp):
        near = list(filter(lambda x: x in board, neighbors(cell[0])))
        alive_count = 0

        for neighbor in near:
            if is_alive(temp, neighbor):
                alive_count += 1

        if is_alive(temp, cell[0]) and alive_count<=1:
            set_alive(board, cell[0], False)
        elif is_alive(temp, cell[0]) and alive_count>=4:
            set_alive(board, cell[0], False)
        elif not is_alive(temp, cell[0]) and alive_count==3:
            set_alive(board, cell[0], True)

if __name__ == '__main__': # Simulates 100 generation in a 10x10 board for a glider/blinker formation
    game = board(10)
    place_blinker(game, (1,2))
    place_glider(game, (2,4))

    for i in range(1,101):
        print(f'Generation {i}')
        tick(game)
        print_board(game)
        print('\n\n')
        sleep(1)

