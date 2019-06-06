from Gate import *
import App as Application
from Color import *
from ImageLoader import *

class Or(Gate):

    def __init__(self,parentMap,fromData = False):
        print("OR")
        Gate.__init__(self,2,parentMap,Color.orange,"OR",ImageLoader.OR,fromData)
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
            if self.inputs[0].value == 1 and self.inputs[1].value == 1:
                self.outputs.value=1
            else:
                self.outputs.value =self.inputs[0].value + self.inputs[1].value
            self.outputs.propagate()
            
     