import math


def is_safe(sudoku, row, col, num):
    # Check if it is used in the same row
    for i in range(len(sudoku)):
        if sudoku[row][i] == num:
            return False

    # Check if it is used in the same column
    for j in range(len(sudoku)):
        if sudoku[j][col] == num:
            return False

    # Check if it is used in the same box
    inner_box_size = int(math.sqrt(len(sudoku)))
    row = row - (row % inner_box_size)
    col = col - (col % inner_box_size)
    for i in range(inner_box_size):
        for j in range(inner_box_size):
            if sudoku[i+row][j+col] == num:
                return False

    return True


def find_empty_location(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            if sudoku[i][j] == 0:
                return i, j


def solve(sudoku):
    empty_pos = find_empty_location(sudoku)
    if empty_pos is None:
        return True
    row, col = empty_pos
    for num in range(1, 10):
        if is_safe(sudoku, row, col, num):
            sudoku[row][col] = num
            if solve(sudoku):
                return True
            sudoku[row][col] = 0

    return False


sudoku = [[3,0,6,5,0,8,4,0,0],
          [5,2,0,0,0,0,0,0,0],
          [0,8,7,0,0,0,0,3,1],
          [0,0,3,0,1,0,0,8,0],
          [9,0,0,8,6,3,0,0,5],
          [0,5,0,0,9,0,6,0,0],
          [1,3,0,0,0,0,2,5,0],
          [0,0,0,0,0,0,0,7,4],
          [0,0,5,2,0,6,3,0,0]]

print solve(sudoku)
print sudoku