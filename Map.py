from Utils import *
from Cell import *
from Not import *
from And import *
from Or import *
from Xor import *
from Nand import *
from Nor import *
from Nxor import *

class Map:
	#dimensiunea hartii
	size = ()
	#celulele
	map  = []
	#dimensiunea celulelor
	canAddGate = True
	
	def __init__(self,x,y,size,cellSize):
		self.cellSize = cellSize
		(r,c) = size
		self.map = newLineMatrix(r)
		self.size = size
		self.gates = []
		self.x = x
		self.y = y

		for y in range(0,r):
			for x in range(0,c):
				self.map[y].append(Cell(self.x + x * self.cellSize,self.y + y * self.cellSize,self.cellSize))
	
		#VECINI
		for y in range(1,r-1):
			for x in range(1,c-1):
				self.map[y][x].neighbors = (self.map[y-1][x],self.map[y+1][x],self.map[y][x+1],self.map[y][x-1])
		
		for i in range(1,c-1):
			self.map[0][i].neighbors=(None,self.map[1][i],self.map[0][i+1],self.map[0][i-1])
			self.map[r-1][i].neighbors=(self.map[r-2][i],None,self.map[r-1][i+1],self.map[r-1][i-1])
		
		for i in range(1,r-1):
			self.map[i][0].neighbors=(self.map[i-1][0],self.map[i+1][0],self.map[i][1],None)
			self.map[i][c-1].neighbors=(self.map[i-1][c-1],self.map[i+1][c-1],None,self.map[i][c-2])

		self.map[0][0].neighbors=(None,self.map[1][0],self.map[0][1],None)
		self.map[0][c-1].neighbors=(None,self.map[1][c-1],None,self.map[0][c-2])
		self.map[r-1][0].neighbors=(self.map[r-2][0],None,self.map[r-1][1],None)
		self.map[r-1][c-1].neighbors=(self.map[r-2][c-1],None,None,self.map[r-1][c-2])
		

	def render(self,screen):
		
		for y in range(0,self.size[0]):
			for x in range(0,self.size[1]):
				self.map[y][x].render(screen)
				self.map[y][x].update()
		
		for g in self.gates:
			g.render(screen)

	def update(self):
		(b1,b2,b3) = pygame.mouse.get_pressed()

		if b1 and Application.App.editMode == 1:
			if Gate.checkIfOcuppied(self) == False and self.canAddGate:
				if Application.App.option == 1:
					self.gates.append(Not(self))	
				elif Application.App.option == 2:
					self.gates.append(And(self))
				elif Application.App.option == 3:
					self.gates.append(Or(self))
				elif Application.App.option == 4:
					self.gates.append(Xor(self))
				elif Application.App.option == 5:
					self.gates.append(Nand(self))
				elif Application.App.option == 6:
					self.gates.append(Nor(self))
				elif Application.App.option == 7:
					self.gates.append(Nxor(self))
				self.canAddGate = False
			#self.gates.append(Not(self))
		else:
			self.canAddGate = True


		for g in self.gates:
			g.update()
			if g.isClicked():
				if Application.App.editMode == 1 and Application.App.option == 8:
					g.deOcupy()
					self.gates.remove(g)