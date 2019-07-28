# Kinght's Tour problem
# Solved using backtracking
# This is not optimal solution. We may want to use Warnsdorffs algorithm for better running time

def is_safe(board, x, y):
    if (x >= 0 and x < len(board)) and (y >= 0 and y < len(board)) and board[x][y] == -1:
        return True
    return False


def knights_tour(board, x_moves, y_moves, x_move, y_move, current_pos):
    if current_pos == len(board) * len(board):
        return True
    for move in range(len(x_moves)):
        next_x = x_move + x_moves[move]
        next_y = y_move + y_moves[move]
        if is_safe(board, next_x, next_y):
            board[next_x][next_y] = current_pos
            if knights_tour(board, x_moves, y_moves, next_x, next_y, current_pos+1):
                return True

            board[next_x][next_y] = -1

    return False


N = int(raw_input())
board = [[-1 for i in range(N)] for j in range(N)]

# Set the starting point
board[0][0] = 0

# There are 8 possible moves for knight to move
x_moves = [2, 1, -1, -2, -2, -1,  1,  2]
y_moves = [1, 2,  2,  1, -1, -2, -2, -1]

print knights_tour(board, x_moves, y_moves, 0, 0, 1)

print board
