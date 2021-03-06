'''Debugger and Helper functions for the Project'''

import numpy as np
# from gomoku import print_board


def random_board(shape, bad=False):
    board = np.random.randint(-1,2,size=shape)
    if bad:
        return convert_good_to_bad_board(board)
    return board


def convert_good_to_bad_board(good_board):
    bad_board = good_board.tolist()
    for i in range(len(bad_board)):
        for j in range(len(bad_board[0])):
            if bad_board[i][j] == 0:
                bad_board[i][j] = ' '
            elif bad_board[i][j] == 1:
                bad_board[i][j] = 'b'
            elif bad_board[i][j] == -1:
                bad_board[i][j] = 'w'
    return bad_board

if __name__=='__main__':
    pass