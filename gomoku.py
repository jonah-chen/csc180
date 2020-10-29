"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 26, 2020
"""

class Gomoku:
    def __init__(self):
        pass

    def is_empty(self, board): 
        '''Return True iff the board is empty
        '''
        for i in board:
            for j in i:
                if ' ' != j:
                    return False
        return True
        
  
    # The tuple (d_y, d_x) represent
    # (1,0) direction from left to right (horizontal)
    # (0,1) direction from top to bottom (vertical)
    # (1,1) direction from upper-left to lower-right 
    # #
    #   #
    #     #
    # (1,-1) direction from upper-right to lower left
    #     #
    #   #
    # #


    def is_bounded(self, board, y_end, x_end, length, d_y, d_x):
        '''Return 'OPEN' for open sequences, 'SEMIOPEN' for semiopen sequences 
        and 'CLOSED' for closed sequences. Open, Semipoen, and Closed are 
        defined in ESC180H1F
        '''
        # Check (y_end + d_y, x_end + d_x) is empty 
        # or (y_end - length++ * d_y, x_end - length++ * d_x) is empty
        y1, x1, y2, x2 = y_end + d_y, x_end + d_x, y_end - (length + 1) * d_y, x_end - (length + 1) * d_x
        length = len(board)
        state = 1

        # If one end exceeds the border, no stones can be placed, or if the square is occupied
        # The or short circuits, thus, no index error should be thrown
        if (y1 < 0 or  x1 < 0 or y1 >= length or x1 >= length or board[y1, x1] != ' '):
            state -= 1
        if (y2 < 0 or x2 < 0 or y2 >= length or x2 >= length or board[y2, x2] != ' '):
            state -= 1

        # hAhA nO SwitCH StATeMenT iN pYThoN
        if state == 1:
            return 'OPEN'
        if state == 0:
            return 'SEMIOPEN'
        if state == -1:
            return 'CLOSED'

        return 'ERROR!'


    def detect_row(self, board, col, y_start, x_start, length, d_y, d_x):
        '''
        '''
        open_seq_count, semi_open_seq_count = 0, 0
        
        # starts at (y_start, x_start) and goes in the direciton (d_y, d_x)
        
        dir = -1
        if (x_start == 0 or y_start == 0):
            dir = 1
        
         

        return open_seq_count, semi_open_seq_count

    def detect_rows(self, board, col, length):
        ####CHANGE ME
        open_seq_count, semi_open_seq_count = 0, 0
        return open_seq_count, semi_open_seq_count
        
    def search_max(self, board):
        return move_y, move_x
        
    def score(self, board): # return int
        MAX_SCORE = 100000
        
        open_b = {}
        semi_open_b = {}
        open_w = {}
        semi_open_w = {}
        
        for i in range(2, 6):
            open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
            open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
            
        
        if open_b[5] >= 1 or semi_open_b[5] >= 1:
            return MAX_SCORE
        
        elif open_w[5] >= 1 or semi_open_w[5] >= 1:
            return -MAX_SCORE
            
        return (-10000 * (open_w[4] + semi_open_w[4])+ 
                500  * open_b[4]                     + 
                50   * semi_open_b[4]                + 
                -100  * open_w[3]                    + 
                -30   * semi_open_w[3]               + 
                50   * open_b[3]                     + 
                10   * semi_open_b[3]                +  
                open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

        
    def is_win(self, board):
        pass


    def print_board(self, board): # return void
        
        s = "*"
        for i in range(len(board[0])-1):
            s += str(i%10) + "|"
        s += str((len(board[0])-1)%10)
        s += "*\n"
        
        for i in range(len(board)):
            s += str(i%10)
            for j in range(len(board[0])-1):
                s += str(board[i][j]) + "|"
            s += str(board[i][len(board[0])-1]) 
        
            s += "*\n"
        s += (len(board[0])*2 + 1)*"*"
        
        print(s)
        

    def make_empty_board(self, sz):
        board = []
        for i in range(sz):
            board.append([" "]*sz)
        return board
                    


    def analysis(self, board):
        for c, full_name in [["b", "Black"], ["w", "White"]]:
            print("%s stones" % (full_name))
            for i in range(2, 6):
                open, semi_open = detect_rows(board, c, i)
                print("Open rows of length %d: %d" % (i, open))
                print("Semi-open rows of length %d: %d" % (i, semi_open))
            
        
        

            
        
    def play_gomoku(self, board_size):
        board = make_empty_board(board_size)
        board_height = len(board)
        board_width = len(board[0])
        
        while True:
            print_board(board)
            if is_empty(board):
                move_y = board_height // 2
                move_x = board_width // 2
            else:
                move_y, move_x = search_max(board)
                
            print("Computer move: (%d, %d)" % (move_y, move_x))
            board[move_y][move_x] = "b"
            print_board(board)
            analysis(board)
            
            game_res = is_win(board)
            if game_res in ["White won", "Black won", "Draw"]:
                return game_res
                
                
            
            
            
            print("Your move:")
            move_y = int(input("y coord: "))
            move_x = int(input("x coord: "))
            board[move_y][move_x] = "w"
            print_board(board)
            analysis(board)
            
            game_res = is_win(board)
            if game_res in ["White won", "Black won", "Draw"]:
                return game_res
            
                
                
    def put_seq_on_board(self, board, y, x, d_y, d_x, length, col):
        for i in range(length):
            board[y][x] = col        
            y += d_y
            x += d_x


    def test_is_empty(self):
        board  = make_empty_board(8)
        if is_empty(board):
            print("TEST CASE for is_empty PASSED")
        else:
            print("TEST CASE for is_empty FAILED")

    def test_is_bounded(self):
        board = make_empty_board(8)
        x = 5; y = 1; d_x = 0; d_y = 1; length = 3
        put_seq_on_board(board, y, x, d_y, d_x, length, "w")
        print_board(board)
        
        y_end = 3
        x_end = 5

        if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
            print("TEST CASE for is_bounded PASSED")
        else:
            print("TEST CASE for is_bounded FAILED")


    def test_detect_row(self):
        board = make_empty_board(8)
        x = 5; y = 1; d_x = 0; d_y = 1; length = 3
        put_seq_on_board(board, y, x, d_y, d_x, length, "w")
        print_board(board)
        if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
            print("TEST CASE for detect_row PASSED")
        else:
            print("TEST CASE for detect_row FAILED")

    def test_detect_rows(self):
        board = make_empty_board(8)
        x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
        put_seq_on_board(board, y, x, d_y, d_x, length, "w")
        print_board(board)
        if detect_rows(board, col,length) == (1,0):
            print("TEST CASE for detect_rows PASSED")
        else:
            print("TEST CASE for detect_rows FAILED")

    def test_search_max(self):
        board = make_empty_board(8)
        x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
        put_seq_on_board(board, y, x, d_y, d_x, length, col)
        x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
        put_seq_on_board(board, y, x, d_y, d_x, length, col)
        print_board(board)
        if search_max(board) == (4,6):
            print("TEST CASE for search_max PASSED")
        else:
            print("TEST CASE for search_max FAILED")

    def easy_testset_for_main_functions(self):
        test_is_empty()
        test_is_bounded()
        test_detect_row()
        test_detect_rows()
        test_search_max()

    def some_tests(self):
        board = make_empty_board(8)

        board[0][5] = "w"
        board[0][6] = "b"
        y = 5; x = 2; d_x = 0; d_y = 1; length = 3
        put_seq_on_board(board, y, x, d_y, d_x, length, "w")
        print_board(board)
        analysis(board)
        
        # Expected output:
        #       *0|1|2|3|4|5|6|7*
        #       0 | | | | |w|b| *
        #       1 | | | | | | | *
        #       2 | | | | | | | *
        #       3 | | | | | | | *
        #       4 | | | | | | | *
        #       5 | |w| | | | | *
        #       6 | |w| | | | | *
        #       7 | |w| | | | | *
        #       *****************
        #       Black stones:
        #       Open rows of length 2: 0
        #       Semi-open rows of length 2: 0
        #       Open rows of length 3: 0
        #       Semi-open rows of length 3: 0
        #       Open rows of length 4: 0
        #       Semi-open rows of length 4: 0
        #       Open rows of length 5: 0
        #       Semi-open rows of length 5: 0
        #       White stones:
        #       Open rows of length 2: 0
        #       Semi-open rows of length 2: 0
        #       Open rows of length 3: 0
        #       Semi-open rows of length 3: 1
        #       Open rows of length 4: 0
        #       Semi-open rows of length 4: 0
        #       Open rows of length 5: 0
        #       Semi-open rows of length 5: 0
        
        y = 3; x = 5; d_x = -1; d_y = 1; length = 2
        
        put_seq_on_board(board, y, x, d_y, d_x, length, "b")
        print_board(board)
        analysis(board)
        
        # Expected output:
        #        *0|1|2|3|4|5|6|7*
        #        0 | | | | |w|b| *
        #        1 | | | | | | | *
        #        2 | | | | | | | *
        #        3 | | | | |b| | *
        #        4 | | | |b| | | *
        #        5 | |w| | | | | *
        #        6 | |w| | | | | *
        #        7 | |w| | | | | *
        #        *****************
        #
        #         Black stones:
        #         Open rows of length 2: 1
        #         Semi-open rows of length 2: 0
        #         Open rows of length 3: 0
        #         Semi-open rows of length 3: 0
        #         Open rows of length 4: 0
        #         Semi-open rows of length 4: 0
        #         Open rows of length 5: 0
        #         Semi-open rows of length 5: 0
        #         White stones:
        #         Open rows of length 2: 0
        #         Semi-open rows of length 2: 0
        #         Open rows of length 3: 0
        #         Semi-open rows of length 3: 1
        #         Open rows of length 4: 0
        #         Semi-open rows of length 4: 0
        #         Open rows of length 5: 0
        #         Semi-open rows of length 5: 0
        #     
        
        y = 5; x = 3; d_x = -1; d_y = 1; length = 1
        put_seq_on_board(board, y, x, d_y, d_x, length, "b")
        print_board(board)
        analysis(board);   #WHY ARE THERE SEMISCOLONS!!!!!!!!!!!!!!!!!!!!!!!!
        
        #        Expected output:
        #           *0|1|2|3|4|5|6|7*
        #           0 | | | | |w|b| *
        #           1 | | | | | | | *
        #           2 | | | | | | | *
        #           3 | | | | |b| | *
        #           4 | | | |b| | | *
        #           5 | |w|b| | | | *
        #           6 | |w| | | | | *
        #           7 | |w| | | | | *
        #           *****************
        #        
        #        
        #        Black stones:
        #        Open rows of length 2: 0
        #        Semi-open rows of length 2: 0
        #        Open rows of length 3: 0
        #        Semi-open rows of length 3: 1
        #        Open rows of length 4: 0
        #        Semi-open rows of length 4: 0
        #        Open rows of length 5: 0
        #        Semi-open rows of length 5: 0
        #        White stones:
        #        Open rows of length 2: 0
        #        Semi-open rows of length 2: 0
        #        Open rows of length 3: 0
        #        Semi-open rows of length 3: 1
        #        Open rows of length 4: 0
        #        Semi-open rows of length 4: 0
        #        Open rows of length 5: 0
        #        Semi-open rows of length 5: 0


  
            
if __name__ == '__main__':
    g = Gomoku()
    g.play_gomoku(8)
    