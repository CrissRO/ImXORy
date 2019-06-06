import pygame 
from Color import *
import App as Application

class Cell:
	x = 0
	y = 0
	size = 20
	screen = None
	neighbors = ()
	isWire = False
	canUpdate = True
	canPropagate = True
	isOcuppied = False
	isJonction=False
	isHovered = True
	value = 0

	isInput = False
	isOutput = False

	#for pF
	isVisited = False

	def __init__(self,x,y,size):
		self.x = x
		self.y = y
		self.size = size
		
	def render(self,screen):
		#dreptunghiul complet
		rect = pygame.Rect(self.x,self.y,self.size,self.size)
		#asa se modifica culoarea la celula
		
		#error color
		fillColor = (255,0,255)
		wireColor = (0,0,0)

		
		if self.isWire:
			if self.isHovered:
				fillColor = Color.darkGray
			else:
				fillColor = Color.gray
			if not self.isJonction:
				if self.value == 0:
					wireColor = Color.red
				else:
					wireColor = Color.green
			else:
				wireColor = Color.blue
		else:
			if self.isHovered:
				fillColor = Color.lightGray
			else:
				fillColor = Color.white
			
		inputColor = (255,0,255)
		if self.isInput or self.isOutput:
			if self.value == 1:
				inputColor = Color.green
			else:
				inputColor = Color.red
		#se deseneaza celula si borderul
		screen.fill(fillColor,pygame.Rect(self.x+1,self.y+1,self.size-1,self.size-1))

		#N
		if self.isWire or self.isInput or self.isOutput:
			half = self.size/2
			cX = self.x + half
			cY = self.y + half
			if self.isWire:
				pygame.draw.ellipse(screen, wireColor, pygame.Rect(cX-2,cY-2,4,4))
			elif self.isInput:
				wireColor = inputColor

				screen.fill(inputColor,pygame.Rect(self.x+1,self.y+1,self.size-1,self.size-1))
			elif self.isOutput:
				wireColor = inputColor

				pygame.draw.ellipse(screen, inputColor, pygame.Rect(self.x,self.y,self.size,self.size))
				
			if self.neighbors[0] != None and (self.neighbors[0].isWire or self.neighbors[0].isInput or self.neighbors[0].isOutput):
				pygame.draw.line(screen, wireColor, (cX,cY), (cX,cY-half), 5)
			if self.neighbors[1] != None and (self.neighbors[1].isWire or self.neighbors[1].isInput or self.neighbors[1].isOutput):
				pygame.draw.line(screen, wireColor, (cX,cY), (cX,cY+half), 5)
			if self.neighbors[2] != None and (self.neighbors[2].isWire or self.neighbors[2].isInput or self.neighbors[2].isOutput):
				pygame.draw.line(screen, wireColor, (cX,cY), (cX+half,cY), 5)
			if self.neighbors[3] != None and (self.neighbors[3].isWire or self.neighbors[3].isInput or self.neighbors[3].isOutput):
				pygame.draw.line(screen, wireColor, (cX,cY), (cX-half,cY), 5)
			if self.isInput or self.isOutput:
				text = Application.App.FONT.render(str(self.value), True, Color.black, None)
				screen.blit(text, pygame.Rect(cX-2,self.y,self.size-1,self.size-1))
			
		#pygame.draw.rect(screen,Color.black,rect,1)

	def update(self):
		(mX,mY) = pygame.mouse.get_pos()
		(b1,b2,b3) = pygame.mouse.get_pressed()

		if self.isInput:
			self.propagate()

		if(mX > self.x and
			mY > self.y and
			mX < self.x + self.size and
			mY < self.y + self.size):
			self.isHovered = True
			if Application.App.editMode == 0:
				if Application.App.option == 1:
					if b1 and self.canUpdate:
						self.isWire = not self.isWire
						self.value = 0
						self.isJonction = False
						self.canUpdate = False
				if Application.App.option == 2:
					if b1 and self.canUpdate:
						self.isWire=True
						self.isJonction = not self.isJonction
						self.canUpdate = False
				if Application.App.option == 3:
					if b1 and self.canUpdate:
						self.isInput = not self.isInput
						self.canUpdate = False
				if Application.App.option == 4:
					if b1 and self.canUpdate:
						self.isOutput = not self.isOutput
						self.canUpdate = False
				if Application.App.option == 5:
					if b1 and self.canUpdate:
						if self.value == 1:
							self.value = 0
						else:
							self.value = 1
						self.canUpdate = False
						self.canPropagate = True
						self.propagate()
		else:
			self.canUpdate = True
			self.canPropagate = True
			self.isHovered = False
			
		
		
		
	def propagate(self):
		if self.canPropagate:
			self.canPropagate = False
			for i in range(0,len(self.neighbors)):
				if self.neighbors[i] != None and (self.neighbors[i].isWire or self.neighbors[i].isOutput):
					if self.neighbors[i].isJonction:
						if self.neighbors[i].neighbors[i] != None and self.neighbors[i].neighbors[i].isWire:
							self.neighbors[i].neighbors[i].value=self.value
							self.neighbors[i].neighbors[i].propagate()
					else:
						self.neighbors[i].value = self.value
						self.neighbors[i].propagate()

					

			
		