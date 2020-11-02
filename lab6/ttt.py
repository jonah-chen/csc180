'''
 X | O | X
---+---+---
 O | O | X
---+---+---
   | X |
'''

import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3)
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")



def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board


# Problem 1
def function(square_num):
    '''Return list coord such that board[coord[0]][coord[1]] = 'X' would put an
    'X' in the square square_num'''
    return [(square_num - 1) // 3, (square_num - 1) % 3]


def inverse_function(coords):
    return coords[0] * 3 + coords[1] + 1


def put_in_board(board, mark, square_num):
    '''Modify the contents on board such that string mark is put in the
    coordinates in board corresponding to square_num'''
    coord = function(square_num)
    if coord in get_free_squares(board):
        board[coord[0]][coord[1]] = mark
        return 0
    print('You are not allowed to make a mark here!')
    return -1


# Problem 2
def get_free_squares(board):
    '''Return list which contains the coordinates of the free squares in the
    board'''
    free_squares = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                free_squares.append([i,j])
    return free_squares


def make_random_move(board, mark):
    '''Make a random legal move'''
    free_squares = get_free_squares(board)
    randint = int(len(free_squares) * random.random())
    put_in_board(board, mark, inverse_function(free_squares[randint]))


# Problem 3

def is_row_all_marks(board, row_i, mark):
    '''Return true iff row with index row_i in board contains 3 marks equal to
    mark'''
    return board[row_i] == [mark] * 3


def is_col_all_marks(board, col_i, mark):
    for i in range(3):
        if board[i][col_i] != mark:
            return False
    return True


def is_win(board, mark):
    '''return true iff the player with mark wins'''
    for i in range(3):
        if is_row_all_marks(board, i, mark):
            return True
        if is_col_all_marks(board, i, mark):
            return True
    return [board[0][0], board[1][1], board[2][2]] == [mark] * 3 or [board[2][0], board[1][1], board[0][2]] == [mark] * 3


# Problem 4
def improved_move(board, mark):
    '''Better computer'''
    free_squares = get_free_squares(board)
    for square in free_squares:
        board[square[0]][square[1]] = mark
        if is_win(board, mark):
            return
        board[square[0]][square[1]] = ' '
    make_random_move(board, mark)


def advanced_move(board, mark):
    player_mark = 'X' if mark == 'O' else 'O'
    free_squares = get_free_squares(board)
            
    # Checks if the computer wins
    for square in free_squares:
        board[square[0]][square[1]] = mark
        if is_win(board, mark):
            return
        board[square[0]][square[1]] = ' '

    # Check if the player can win on the next turn
    for square in free_squares:
        board[square[0]][square[1]] = player_mark
        if is_win(board, player_mark):
            board[square[0]][square[1]] = mark
            return
        board[square[0]][square[1]] = ' '

    if board[1][1] == ' ':
        put_in_board(board, mark, 5)
        return
    make_random_move(board, mark)

if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)

    turns = 0
    input_str = None
    while turns < 9:
        if turns % 2 == 0:
            improved_move(board, 'X')
            # input_str = input('Please specify square to place X\n')
            # if put_in_board(board, 'X', int(input_str)) == 0:
            turns += 1
        else:
            '''play against another player'''
            # input_str = input('Please specify square to place O\n')
            # put_in_board(board, 'O', int(input_str))

            '''make random moves'''
            advanced_move(board, 'O')
            turns += 1

        print_board_and_legend(board)
        if is_win(board, 'O'):
            print('Computer Win')
            break
        elif is_win(board, 'X'):
            print('Player Win')
            break

    if turns == 9:
        print('Draw')
    # print("\n\n")
    #
    # board = [["O", "X", "X"],
    #          [" ", "X", " "],
    #          [" ", "O", " "]]
    #
    # print_board_and_legend(board)