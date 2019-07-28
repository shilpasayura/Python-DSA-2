# N-Queen problem


def is_safe(board, row, col):

    # Checking for the left side of the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check for the upper diagonal on left side
    for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check for lower diagonal on right side
    for i,j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve(board, col+1):
                return True

            board[i][col] = 0
    return False


N = int(raw_input("Enter the boars size: "))

board = [[0 for i in range(N)] for j in range(N)]

solve(board, 0)

print '\n'.join(map(str, board))