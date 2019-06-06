from Color import *
import pygame

class Input:

    def __init__(self,parentMap,line,column,cellSize):
        self.line = line
        self.column = column
        self.value = 0
        self.cellSize = cellSize
        self.x = self.column * self.cellSize + parentMap.x
        self.y = self.line * self.cellSize + parentMap.y
        self.rect(self.x,self.y,self.cellSize,self.cellSize)

    def render(self,screen):
        

        if self.value == 1:
                screen.fill(Color.green,self.rect)    
        else:
                screen.fill(Color.red,self.rect)    
        pygame.draw.rect(screen, Color.black, self.rect, width=1)

    def update(self):
        pass

    def propagate(self):
		if self.canPropagate:
			self.canPropagate = False
			for i in range(0,len(self.neighbors)):
				if self.neighbors[i] != None and self.neighbors[i].isWire:
					if self.neighbors[i].isJonction:
						if self.neighbors[i].neighbors[i] != None and self.neighbors[i].neighbors[i].isWire:
							self.neighbors[i].neighbors[i].value=self.value
							self.neighbors[i].neighbors[i].propagate()
					else:
						self.neighbors[i].value = self.value
						self.neighbors[i].propagate()