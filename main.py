# By Pytel

'''
Oddelit class Bord a Game
 Budu tak moci volat funkce pro Bord i v AI.

'''

import Sudoku
import AI

sudoku = Sudoku.Game()
sudoku.player = AI.Player()
sudoku.FillWithNumbers()
sudoku.Print()
valid = sudoku.bord.ValidBord()
print("Valid =", valid)

sudoku.MakeNewGame()
sudoku.Print()

#'''
while not sudoku.filled:
	bord = sudoku.bord.sudokubord
	move = sudoku.player.Move(bord)
	if sudoku.ValidMove(move):
		sudoku.ExecuteMove(move)
	else:
		print("Invalid move!")
		break
	sudoku.Print()
	sudoku.IsFilled()

print("  ---Final Bord---")
sudoku.Print()

#'''