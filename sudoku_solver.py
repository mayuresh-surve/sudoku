from sudoku_create import *
count = 0
stack = []
possibilities = {}
add = 1


def add_num(assign_list, val):
    a = assign_list
    a.append(val)
    return a


def remove_list(empty_list):
    b = empty_list
    b.clear()
    return b


def solver(first, backtrack):
    global stack, count, add, possibilities
    val_assign = 0
    for x in range(1, 82):
        possibilities[x] = []
    while first < 81:
        row = int(first / 9)
        column = first % 9
        if sudoku[row][column] == 0 or backtrack == 1:
            backtrack = 0
            for val_assign in range(1, 11):
                if val_assign > 9:
                    count = count + 1
                    backtrack = 1
                    sudoku[row][column] = 0
                    possibilities[add] = remove_list(possibilities[add])
                    num = stack.pop()
                    first = num - 1
                    add = num
                    break
                assign1 = 1
                for column1 in range(0, 9):  # to check value is present in row
                    if val_assign == sudoku[row][column1]:
                        assign1 = 0
                        break
                if assign1 == 1:
                    for row1 in range(0, 9):  # to check value is present in column
                        if val_assign == sudoku[row1][column]:
                            assign1 = 0
                            break
                if assign1 == 1:
                    for row1 in range(int(int(row / 3) * 3), int((int(row / 3) * 3) + 3)):  # to check value is present in grid
                        for column1 in range(int(int(column / 3) * 3), int((int(column / 3) * 3) + 3)):
                            if val_assign == sudoku[row1][column1]:
                                assign1 = 0
                                break
                if assign1 == 1:
                    if val_assign not in possibilities[add]:
                        sudoku[row][column] = val_assign
                        stack.append(first)
                        possibilities[add] = add_num(possibilities[add], val_assign)
                        break
        # print("Stack: ", stack)
        # print("Value assigned: ", val_assign)

        add += 1
        first += 1
    print("No of backtracks: ", count)
    return
