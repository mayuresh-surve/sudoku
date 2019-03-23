from sudoku_solver import *
from sudoku_create import *

grid = [[0 for i in range(9)] for j in range(9)]

c = int(input(" 1. For Easy Sudoku\n 2. For Hard Sudoku: "))

if c == 1:
	print("Generating easy mode")
	easy_gen()
elif c == 2:
	print("Generating hard mode")
	hard_gen()

print("----------------------------------")
disp()

print("Solving the sudoku")
solver(0, 0)

disp()
