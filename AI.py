# By Pytel

DEBUG = True

class Player:
	def __init__(self):
		self.bord = None
		self.name = None
		
		self.free_fields = None
		self.last_move = None
		
	def FindFree(self):
		self.free_fields = []
		for y in range(0,9):
			for x in range(0,9):
				#print("Field: None /", self.bord[y][x])
				if self.bord[y][x] == None:
					#if DEBUG:
						#print("Coords:", y, x)
					self.free_fields.append([y,x])
		
	def MakeMove(self):
		move = None 
		for place in self.free_fields:
			y = place[0]
			x = place[1]
			for number in range(0,9):
				self.bord[y][x] = number
				# TODO
				# kontrola validity takoveho tahu
			self.bord[y][x] = None
		
		# [y,x,n]
		return move
		
	def Move(self, bord):
		if self.last_move != None and len(self.last_move) != 0:
			y = self.last_move[0]
			x = self.last_move[1]
			n = self.last_move[2]
			if bord[y][x] == n:
				self.bord[y][x] = n
		else:
			self.bord = bord
			self.FindFree()
			
		
		move = self.MakeMove()
		
		self.Print()
		#print(self.bord)
		return move
		
	def Print(self):
		print(" ---Player---")
		print("Free fields:", self.free_fields)
		print()
		
'''

'''
		
		