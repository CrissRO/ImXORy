from Gate import *
import App as Application
from Color import *
from ImageLoader import *

class Nand(Gate):

    def __init__(self,parentMap,fromData = False):
        print("NAND")
        Gate.__init__(self,2,parentMap,Color.teal,"NAND",ImageLoader.NAND,fromData)
        if not fromData:
            self.setAt()
        
        
    def setAt(self):
        
        self.inputs.append(self.parentMap.map[self.cY][self.cX])
        self.inputs.append(self.parentMap.map[self.cY+2][self.cX])

        for i in self.inputs:
            i.isWire=True

        self.outputs = self.parentMap.map[self.cY+1][self.cX+2]
        self.outputs.isWire = True

    def calculate(self):
        if self.outputs != None:
            #print(self.inputs[0].value)
            self.outputs.value = 1 - self.inputs[0].value * self.inputs[1].value
            self.outputs.propagate()
     