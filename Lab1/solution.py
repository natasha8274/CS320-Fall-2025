import sys


def nQueensAll(N):
    board = []
    solution = []
    if N < 4:
        raise ValueError("N must be at least 4")
    colFilled = set()
    diag1Filled = set()  # row - col
    diag2Filled = set()  # row + col

    def checkQueen(i):
        # i is showing the current row
        if i == N:
            solution.append(board[:])  # add the valid board to solution
            return  # stops the function if a solution is found
        for col in range(N):
            if (col not in colFilled
                and (i - col) not in diag1Filled
                    and (i + col) not in diag2Filled):
                board.append((i, col))
                colFilled.add(col)
                diag1Filled.add(i - col)
                diag2Filled.add(i + col)
                checkQueen(i + 1)
                board.remove((i, col))
                colFilled.remove(col)
                diag1Filled.remove(i - col)
                diag2Filled.remove(i + col)
    checkQueen(0)
    return solution  # return all solutions
