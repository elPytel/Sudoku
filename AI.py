# By Pytel

import Sudoku

DEBUG = True

class Player:
	def __init__(self):
		self.bord = Sudoku.Sudokubord()
		self.name = None
		
		self.free_fields = None
		self.last_move = None
		
	def FindFree(self):
		self.free_fields = []
		bord = self.bord.sudokubord
		for y in range(0,9):
			for x in range(0,9):
				#print("Field: None /", self.bord[y][x])
				if bord[y][x] == None:
					#if DEBUG:
						#print("Coords:", y, x)
					self.free_fields.append([y,x])
		
	def MakeMove(self):
			# [y,x,n]
		move = None 
		bord = self.bord.sudokubord
		sudokubord = self.bord
		
		# hleda vsechny potencionalni tahy
		for place in self.free_fields:
			y = place[0]
			x = place[1]
			place.append([])
			for number in range(1,10):
				bord[y][x] = number
				# TODO
				# kontrola validity takoveho tahu
				n = sudokubord.StartIndexToSquare(y, x)
				if sudokubord.ValidCol(x) and sudokubord.ValidRow(y) and sudokubord.ValidSquare(n):
					place[2].append(number)
				
			bord[y][x] = None
		
		# vybere tah
		for place in self.free_fields:
			if len(place[2]) == 1:
				y = place[0]
				x = place[1]
				n = place[2][0]
				move = [y,x,n]
				break
				
		# neni zadny vhodny tah s jednim moznym cislem
		if move == None or len(move) != 3:
			least = 9
			for place in self.free_fields:
				if len(place[2]) < least:
					least = len(place[2])
			
			for place in self.free_fields:
				if len(place[2]) == least:
					y = place[0]
					x = place[1]
					n = place[2][0]
					move = [y,x,n]
					input("guess!")
					break
		
		print("Move:",move)
		#TUDO
		# ulozit tah jako posledni
		return move
		
	def Move(self, bord):
		if self.last_move != None and len(self.last_move) != 0:
			y = self.last_move[0]
			x = self.last_move[1]
			n = self.last_move[2]
			if bord.sudokubord[y][x] == n:
				self.bord.sudokubord[y][x] = n
				#TODO
				# odstranit dane volne pole 
				# odstranit nemozne tahy z databaze
		else:
			self.bord = bord
			self.FindFree()
			# najit mozne tahy
			
		
		move = self.MakeMove()
		
		self.Print()
		return move
		
	def Print(self):
		print(" ---Player---")
		print("Free fields:", self.free_fields)
		print()
		
'''

'''
		
		