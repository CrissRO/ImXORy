import pygame
import App as Application
import Color
from Cell import *

class Gate:
    x = 0
    y = 0
    nrInputs = 0
    image = None
    

    def __init__(self,nrInputs,parentMap,color,name,image = None,fromData = False):
        print("GATE ")
        self.nrInputs = nrInputs
        self.parentMap = parentMap
        self.cellSize = Application.App.CELL_SIZE
        self.outputs = Cell(0,0,0)
        self.inputs = []
        self.color = color
        self.name = name
        self.cX =0
        self.cY =0
        if not fromData:
            self.setPosition() 
        self.image = image
        if self.image != None:
            self.image = pygame.transform.scale(image,(self.cellSize*3,self.cellSize*3))
        
    def render(self,screen):
        
        if self.image != None:
            screen.blit(self.image,self.rect)
        
        
        #text = Application.App.FONT.render(self.name, True, Color.black, None)
        #screen.blit(text, self.rect)

    def setPosition(self):
        (mX,mY) = pygame.mouse.get_pos()
        self.cX = int((mX  - self.parentMap.x) / self.cellSize)
        self.cY = int((mY - self.parentMap.y) / self.cellSize)
        self.x = self.cX * self.cellSize + self.parentMap.x
        self.y = self.cY * self.cellSize + self.parentMap.y
        self.rect = pygame.Rect(self.x+1,self.y+1,self.cellSize * 3 - 1,self.cellSize * 3 - 1)
        for y in range(self.cY,self.cY+3):
            for x in range(self.cX,self.cX+3):
                self.parentMap.map[y][x].isOcuppied = True

    def setPositionFromData(self,cX,cY):

        self.cX = cX
        self.cY = cY
        self.x = self.cX * self.cellSize + self.parentMap.x
        self.y = self.cY * self.cellSize + self.parentMap.y
        self.rect = pygame.Rect(self.x+1,self.y+1,self.cellSize * 3 - 1,self.cellSize * 3 - 1)
        for y in range(self.cY,self.cY+3):
            for x in range(self.cX,self.cX+3):
                self.parentMap.map[y][x].isOcuppied = True

    def checkIfOcuppied(parentMap):
        (mX,mY) = pygame.mouse.get_pos()
        if mY < parentMap.y:
            return True
        cellSize = Application.App.CELL_SIZE
        x = int((mX-parentMap.x) / cellSize) 
        y = int((mY-parentMap.y) / cellSize)
        if parentMap.map[y][x] == None:
            return True
        for coordY in range(y,y+3):
            for coordX in range(x,x+3):
                if parentMap.map[coordY][coordX].isOcuppied:
                    return True
        else:
            return False

    def update(self):
        self.calculate()

    def calculate(self):
        pass

    def setAt(self):
        pass

    def deOcupy(self):

        for y in range(self.cY,self.cY+3):
            for x in range(self.cX,self.cX+3):
                self.parentMap.map[y][x].isOcuppied = False
                self.parentMap.map[y][x].isWire = False
                self.parentMap.map[y][x].isJonction = False


    def isClicked(self):
        (mX,mY) = pygame.mouse.get_pos()
        (b1,b2,b3) = pygame.mouse.get_pressed()

        if(mX > self.x and
        mY > self.y and
        mX < self.x + self.cellSize * 3 and
        mY < self.y + self.cellSize * 3 and b1):
            return True
        return False
