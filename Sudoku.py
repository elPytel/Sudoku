# By Pytel

import random

DEBUG = False

Numbers = []
for number in range(1,10):
	Numbers.append(number)
if DEBUG:
	print(" ---Numbers---")
	print(Numbers)
	print()

class Game:
	def __init__(self):
		self.bord = self.MakeBord()
		self.number_of_free_fields = 9*9
		
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
		for y in range(9):
			field = self.bord[y][n]
			if field == None:
				continue
			elif field in numbers:
				return False
			else: 
				numbers.append(field)
		return True
		
	def ValidRow(self, n):
		numbers = []
		for x in range(9):
			field = self.bord[n][x]
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
		
		coord = self.SquareToStartIndex(n)
		y0 = coord[0]
		x0 = coord[1]
		
		for y in range(3):
			for x in range(3):
				field = self.bord[y0+y][x0+x]
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
		# projde vsechny radky
		for y in range(9):
			# vygeneruje permutaci vsech cisel pro dany radek
			numbers = self.MakeRandomPermutation()
			if DEBUG:
				print(numbers)
				input()
			# rozmisti je na radku
			for x in range(9):
				# umisteni cisla
				valid = False
				index = 0
				while index < len(numbers):
					self.bord[y][x] = numbers[index]
					# test validity
					n = self.StartIndexToSquare(y, x)
					if self.ValidCol(x) and self.ValidSquare(n):
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
						self.bord[y][x] = None
						cursor = cursor -1
						number = self.bord[y][cursor]
						self.bord[y][cursor] = numbers[index]
						self.bord[y][x] = number
						if DEBUG:
							print("Cursor:", cursor, "| number:", number)
							#self.Print()
						# test validity
						n = self.StartIndexToSquare(y, cursor)
						z = self.StartIndexToSquare(y, x)
						if self.ValidCol(x) and self.ValidCol(cursor) and self.ValidSquare(z) and self.ValidSquare(n):
							if DEBUG:
								self.Print()
								input(" Match!")
							break
						if DEBUG:
							if not self.ValidCol(cursor) or not self.ValidCol(x):
								print("Invalid column!")
							if not self.ValidSquare(z) and not self.ValidSquare(n):
								print("Invalid square!")
						self.bord[y][cursor] = number
						if cursor == 0:
							input(" Cursor reached: 0")
				print(index, "/", len(numbers))
				numbers.pop(index)
				
				# vytiskne po umisteni cisla
				if DEBUG:
					self.Print()
		
	def Print(self):
		print(" ---Bord---")
		for y in range(0,9):
			#print(y, "% 3 =", y % 3)
			if (y % 3 == 0):
				print("-"*13)
			
			for x in range(0,9):
				if (x % 3 == 0):
					print("|", end='')
				if self.bord[y][x] == None:
					print(" ", end='')
				else:
					print(self.bord[y][x], end='')
					
			print("|")
		print("-"*13)
			
			
			
		
	

