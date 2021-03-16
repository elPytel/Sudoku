# By Pytel

import Sudoku


sudoku = Sudoku.Game()
sudoku.Print()
sudoku.FillWithNumbers()
sudoku.Print()
valid = sudoku.ValidBord()
print("Valid =", valid)