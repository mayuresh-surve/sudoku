import random


sudoku = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
          [4, 5, 6, 7, 8, 9, 1, 2, 3],
          [7, 8, 9, 1, 2, 3, 4, 5, 6],
          [2, 3, 4, 5, 6, 7, 8, 9, 1],
          [5, 6, 7, 8, 9, 1, 2, 3, 4],
          [8, 9, 1, 2, 3, 4, 5, 6, 7],
          [3, 4, 5, 6, 7, 8, 9, 1, 2],
          [6, 7, 8, 9, 1, 2, 3, 4, 5],
          [9, 1, 2, 3, 4, 5, 6, 7, 8]]


def disp():
    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku[i][j] != 0:
                print("|", sudoku[i][j], end="")
            else:
                print("|  ", end="")
            if j == 2 or j == 5 or j == 8:
                print("|*", end="")
        print("|\n----------------------------------")
        if i == 2 or i == 5 or i == 8:
            print("**********************************")


def swap():  # swapping columns
    count = 5
    while count > 1:
        sub = random.randrange(1, 3, 1)
        count = count - sub
        j1 = random.randrange(0, 3, 1)
        j2 = random.randrange(0, 3, 1)
        for i in range(0, 9):
            sudoku[i][j1], sudoku[i][j2] = sudoku[i][j2], sudoku[i][j1]
    count = 5
    while count > 1:
        sub = random.randrange(1, 3, 1)
        count = count - sub
        j1 = random.randrange(3, 6, 1)
        j2 = random.randrange(3, 6, 1)
        for i in range(0, 9):
            sudoku[i][j1], sudoku[i][j2] = sudoku[i][j2], sudoku[i][j1]
    count = 5
    while count > 1:
        sub = random.randrange(1, 3, 1)
        count = count - sub
        j1 = random.randrange(6, 9, 1)
        j2 = random.randrange(6, 9, 1)
        for i in range(0, 9):
            sudoku[i][j1], sudoku[i][j2] = sudoku[i][j2], sudoku[i][j1]


def easy_gen():
    k = 0
    while k < 40:
        for i in range(0, 9):  # deleting random elements from row(max 20)
            count = 3
            while count > 1:
                sub = random.randrange(1, 3, 1)
                j = random.randrange(0, 9, 1)
                count = count - sub
                sudoku[i][j] = 0
                k += 1
        for i in range(0, 9):  # deleting random elements from column(max 20)
            count = 7
            while count > 1:
                sub = random.randrange(1, 3, 1)
                j = random.randrange(0, 9, 1)
                if sudoku[j][i] != 0:
                    k += 1
                    sudoku[j][i] = 0
                    count = count - sub
                else:
                    count = count - 1
            if k > 40:
                break
    swap()


def hard_gen():
    k = 0
    while k < 65:
        for i in range(0, 9):  # deleting random elements from row(max 20)
            count = 3
            while count > 1:
                sub = random.randrange(1, 3, 1)
                j = random.randrange(0, 9, 1)
                count = count - sub
                sudoku[i][j] = 0
                k += 1
        for i in range(0, 9):  # deleting random elements from column(max 20)
            count = 7
            while count > 1:
                sub = random.randrange(1, 3, 1)
                j = random.randrange(0, 9, 1)
                if sudoku[j][i] != 0:
                    k += 1
                    sudoku[j][i] = 0
                    count = count - sub
                else:
                    count = count - 1
            if k > 65:
                break
    swap()
