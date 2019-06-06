from Gate import *
import App as Application
from Color import *
from ImageLoader import *

class Not(Gate):
    

    def __init__(self,parentMap,fromData = False):
        print("NOT")
        Gate.__init__(self,1,parentMap,Color.yellow,"NOT",ImageLoader.NOT,fromData)
        if self.image != None:
            self.image = pygame.transform.scale(self.image,(self.cellSize*3,self.cellSize)) 
        if not fromData:
            self.setAt()
        
    def setAt(self):
        self.inputs.append(self.parentMap.map[self.cY][self.cX])
        self.inputs[0].isWire = True
        self.outputs = self.parentMap.map[self.cY][self.cX+2]
        self.outputs.isWire = True

    def setPosition(self):
        (mX,mY) = pygame.mouse.get_pos()
        self.cX = int((mX - self.parentMap.x) / self.cellSize)
        print(self.cX)
        self.cY = int((mY - self.parentMap.y) / self.cellSize)
        self.x = self.cX * self.cellSize + self.parentMap.x 
        self.y = self.cY * self.cellSize + self.parentMap.y
        self.rect = pygame.Rect(self.x+1,self.y+1,self.cellSize * 2 - 1,self.cellSize - 1)
        for y in range(self.cY,self.cY):
            for x in range(self.cX,self.cX+3):
                self.parentMap.map[y][x].isOcuppied = True

    def setPositionFromData(self,cX,cY):
        self.cX = cX
        self.cY = cY
        self.x = self.cX * self.cellSize + self.parentMap.x 
        self.y = self.cY * self.cellSize + self.parentMap.y
        self.rect = pygame.Rect(self.x+1,self.y+1,self.cellSize * 2 - 1,self.cellSize - 1)
        for y in range(self.cY,self.cY):
            for x in range(self.cX,self.cX+3):
                self.parentMap.map[y][x].isOcuppied = True

    def calculate(self):
        if self.outputs != None:
 #           print(self.inputs[0].value)
            self.outputs.value = 1 - self.inputs[0].value
            self.outputs.propagate()