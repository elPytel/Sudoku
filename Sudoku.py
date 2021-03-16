# By Pytel

import random

DEBUG = False
MISSING = 40

Numbers = []
for number in range(1,10):
	Numbers.append(number)
if DEBUG:
	print(" ---Numbers---")
	print(Numbers)
	print()

class Sudokubord:
	def __init__(self):
		self.sudokubord = self.MakeBord()
		
	def MakeBord(self):
		bord = []
		for y in range(9):
			row = []
			for x in range(9):
				#field = []
				row.append(None)
			bord.append(row)
		return bord
		
	def ValidCol(self, n):
		numbers = []
		bord = self.sudokubord
		for y in range(9):
			field = bord[y][n]
			if field == None:
				continue
			elif field in numbers:
				return False
			else: 
				numbers.append(field)
		return True
		
	def ValidRow(self, n):
		numbers = []
		bord = self.sudokubord
		for x in range(9):
			field = bord[n][x]
			if field == None:
				continue
			elif field in numbers:
				return False
			else: 
				numbers.append(field)
		return True
		
	def SquareToStartIndex(self, n):
		if n == 0:
			y0 = 0
			x0 = 0
		elif n == 1:
			y0 = 0
			x0 = 3
		elif n == 2:
			y0 = 0
			x0 = 6
		elif n == 3:
			y0 = 3
			x0 = 0
		elif n == 4:
			y0 = 3
			x0 = 3
		elif n == 5:
			y0 = 3
			x0 = 6
		elif n == 6:
			y0 = 6
			x0 = 0
		elif n == 7:
			y0 = 6
			x0 = 3
		elif n == 8:
			y0 = 6
			x0 = 6
		coord = [y0, x0]
		return coord
		
	def StartIndexToSquare(self, y, x):
		if y < 3 and x < 3:
			n = 0
		elif y < 3 and x > 2 and x < 6:
			n = 1
		elif y < 3 and x > 5:
			n = 2
		elif y > 2 and y < 6 and x < 3:
			n = 3
		elif y > 2 and y < 6 and x > 2 and x < 6:
			n = 4
		elif y > 2 and y < 6 and x > 5:
			n = 5
		elif y > 5 and x < 3:
			n = 6
		elif y > 5 and x > 2 and x < 6:
			n = 7
		elif y > 5 and x > 5:
			n = 8
		return n
		
	def ValidSquare(self, n):
		numbers = []
		
		bord = self.sudokubord
		coord = self.SquareToStartIndex(n)
		y0 = coord[0]
		x0 = coord[1]
		
		for y in range(3):
			for x in range(3):
				field = bord[y0+y][x0+x]
				if field == None:
					continue
				elif field in numbers:
					return False
				else: 
					numbers.append(field)
		return True
	
	def ValidBord(self):
		for n in range(9):
			if self.ValidRow(n) != True:
				return False
			if self.ValidCol(n) != True:
				return False
			if self.ValidSquare(n) != True:
				return False
		return True
		
	def Print(self):
		bord = self.sudokubord
		print(" ---Bord---")
		for y in range(0,9):
			#print(y, "% 3 =", y % 3)
			if (y % 3 == 0):
				print("-"*13)
			
			for x in range(0,9):
				if (x % 3 == 0):
					print("|", end='')
				if bord[y][x] == None:
					print(" ", end='')
				else:
					print(bord[y][x], end='')
					
			print("|")
		print("-"*13)
		
class Game:
	def __init__(self):
		self.bord = Sudokubord()
		self.generated_bord = Sudokubord()
		self.number_of_free_fields = 9*9
		self.filled = False
		self.player_name = None
		
	def MakeRandomPermutation(self):
		numbers = []
		for number in range(1,10):
			repeat = True
			while repeat == True:
				number = random.randrange(1, 10)
				if not number in numbers:
					 numbers.append(number)
					 repeat = False
		return numbers
	
	def FillWithNumbers(self):
		reset = True
		while reset == True:
			reset = False
			sudokubord = self.bord
			self.bord.sudokubord = sudokubord.MakeBord()
			bord = self.bord.sudokubord
			
			# projde vsechny radky
			for y in range(0,9):
				# vygeneruje permutaci vsech cisel pro dany radek
				numbers = self.MakeRandomPermutation()
				if DEBUG:
					print(numbers)
					print("Row:", y)
					#input()
				# rozmisti je na radku
				for x in range(0,9):
					# umisteni cisla
					valid = False
					index = 0
					while index < len(numbers):
						bord[y][x] = numbers[index]
						# test validity
						n = sudokubord.StartIndexToSquare(y, x)
						if sudokubord.ValidCol(x) and sudokubord.ValidSquare(n):
							break
						if DEBUG:
							print("Number:", numbers[index], "Faigled!")
						# aktualizace
						index = index +1
					
					# pokud se nedari umistit z dane permutace cislo, tak si jej vymeni s jinym jiz umistenym	
					if index >= len(numbers):
						index = index -1	# korekce
						cursor = x
						if DEBUG:
							print("Placing number:", numbers[index], "to position:", x)
						# dokud nenajde vhodneho kandidata
						while cursor > 0:
							bord[y][x] = None
							cursor = cursor -1
							number = bord[y][cursor]
							bord[y][cursor] = numbers[index]
							bord[y][x] = number
							if DEBUG:
								print("Cursor:", cursor, "| number:", number)
								#self.Print()
							# test validity
							n = sudokubord.StartIndexToSquare(y, cursor)
							z = sudokubord.StartIndexToSquare(y, x)
							if sudokubord.ValidCol(x) and sudokubord.ValidCol(cursor) and sudokubord.ValidSquare(z) and sudokubord.ValidSquare(n):
								if DEBUG:
									sudokubord.Print()
									print(" Match!")
								break
							if DEBUG:
								if not sudokubord.ValidCol(cursor) or not sudokubord.ValidCol(x):
									print("Invalid column!")
								if not sudokubord.ValidSquare(z) and not sudokubord.ValidSquare(n):
									print("Invalid square!")
							bord[y][cursor] = number
							if cursor == 0:
								print(" ERROR: Cursor reached 0! -> Reset")
								reset = True
								break
							
					numbers.pop(index)
					
					# vytiskne po umisteni cisla
					if DEBUG:
						print(index, "/", len(numbers))
						sudokubord.Print()
						
					if reset == True:
						break
					
				if reset == True:
					break
		
	def ValidMove(self, move):
		bord = self.bord.sudokubord
		if move == None or len(move) != 3:
			if DEBUG:
				print("Invalid lenght!")
			return False	
		
		y = move[0]
		x = move[1]
		n = move[2]
		# validni souradnice
		if y > 9 or y < 0 or x > 9 or x < 0:
			if DEBUG:
				print("Invalid coord!")
			return False
		
		# validni cislo
		if not n in Numbers:
			if DEBUG:
				print("Invalid number:", n)
			return False
		
		# volne pole
		if bord[y][x] != None:
			if DEBUG:
				print("Overvrite!")
			return False
		
		# validni tah
		bord[y][x] = n
		if not self.bord.ValidBord():
			bord[y][x] = None
			if DEBUG:
				print("Invalid play!")
			return False
		
		return True
	
	def ExecuteMove(self, move):
		bord = self.bord.sudokubord
		y = move[0]
		x = move[1]
		n = move[2]
		print("Coords: Y:", y,"X:", x, "Number:", n)
		bord[y][x] = n
				
	def IsFilled(self):
		free_fields = 0
		bord = self.bord.sudokubord
		for y in range(0,9):
			for x in range(0,9):
				if bord[y][x] == None:
					free_fields = free_fields +1
		
		if free_fields == 0:
			self.filled = True
		self.number_of_free_fields = free_fields
		
	def MakeNewGame(self):
		#TODO prepsat na deepcop
		self.generated_bord = self.bord
		bord = self.bord.sudokubord
		n = 0
		while n < MISSING:
			y = random.randrange(0, 9)
			x = random.randrange(0, 9)
			if bord[y][x] != None:
				bord[y][x] = None
				n = n +1
		
	def Print(self):
		bord = self.bord.sudokubord
		print(" ---Game---")
		print("  Player name:", self.player_name)
		print("  Filled:", self.filled)
		print("  Bord:")
		for y in range(0,9):
			#print(y, "% 3 =", y % 3)
			if (y % 3 == 0):
				print("-"*13)
			
			for x in range(0,9):
				if (x % 3 == 0):
					print("|", end='')
				if bord[y][x] == None:
					print(" ", end='')
				else:
					print(bord[y][x], end='')
					
			print("|")
		print("-"*13)
			
				
'''
	


'''