from queue import *
from Cell import *
from Not import *
from And import *
from Or import *
from Xor import *
from Nand import *
from Nor import *
from Nxor import *
import os

def fileExist(path):
	exists = os.path.isfile(path)
	if exists:
		return True
	else:
		return False

def newMatrix(size):
	(rows,cols) = size
	matrix = [[None] * cols] * rows
	return matrix

#!!!!! ASTA E VARIANTA BUNA
def newLineMatrix(rows):
	matrix = []
	for i in range(rows):
		matrix.append([])
	return matrix

def showMatrix(m):
	for line in m:
		for element in line:
			print(element,end=' ')
		print()
		
def aStar(start):

	frontier = Queue()
	frontier.put(start)	
	start.isVisited = True
	path = []


	while not frontier.empty():
		current = frontier.get()
		for vecin in current.neighbors:
			if not vecin.isVisited:
				frontier.put(vecin)
				vecin.isVisited = True
				path.append(vecin)

def readFromFile(fileName,parentMap):
		name = input("Name of input file with extension:")
		if fileExist(name):
			print("YES")
		else:
			return
		index = 0
		mW = 0
		mH = 0
		lineNumber = 0
		gateNumber = -1
		i = -1
		nextGateX = -1
		nextGateY = -1
		nextGateType = -1
		print("Loading")
		with open(name,"r+") as f:
			for line in f:
				for word in line.split():

					if index == 0:
						mH = int(word)
					elif index == 1:
						mW = int(word)
					elif index > 1 and index <= (mW)*(mH):
						i = index - 2
						
						cX = int(i % mW)

						cY = int(i / mW)
						
						
						if cY < mH and cX < mW:
							if word == "0":
								parentMap.map[cY][cX].isWire = False
								parentMap.map[cY][cX].isJonction = False
								parentMap.map[cY][cX].isInput = False
								parentMap.map[cY][cX].isOutput = False
								parentMap.map[cY][cX].value = 0
								parentMap.map[cY][cX].isOcuppied = False
							elif word == "1":
								parentMap.map[cY][cX].isWire = True
								parentMap.map[cY][cX].isJonction = False
								parentMap.map[cY][cX].isInput = False
								parentMap.map[cY][cX].isOutput = False
								parentMap.map[cY][cX].value = 0
								parentMap.map[cY][cX].isOcuppied = False
							elif word == "2":
								parentMap.map[cY][cX].isWire = True
								parentMap.map[cY][cX].isJonction = False
								parentMap.map[cY][cX].isInput = False
								parentMap.map[cY][cX].isOutput = False
								parentMap.map[cY][cX].value = 1
								parentMap.map[cY][cX].isOcuppied = False
							elif word == "3":
								parentMap.map[cY][cX].isWire = False
								parentMap.map[cY][cX].isJonction = False
								parentMap.map[cY][cX].isInput = True
								parentMap.map[cY][cX].isOutput = False
								parentMap.map[cY][cX].value = 0
								parentMap.map[cY][cX].isOcuppied = False
							elif word == "4":
								parentMap.map[cY][cX].isWire = False
								parentMap.map[cY][cX].isJonction = False
								parentMap.map[cY][cX].isInput = False
								parentMap.map[cY][cX].isOutput = True
								parentMap.map[cY][cX].value = 0
								parentMap.map[cY][cX].isOcuppied = False
							elif word == "5":
								parentMap.map[cY][cX].isWire = True
								parentMap.map[cY][cX].isJonction = True
								parentMap.map[cY][cX].isInput = False
								parentMap.map[cY][cX].isOutput = False
								parentMap.map[cY][cX].value = 0
								parentMap.map[cY][cX].isOcuppied = False
					elif index > (mW)*(mH):
						if gateNumber == -1:
							gateNumber = int(word)
							i = 0
							parentMap.gates.clear()
						else:
							if i == 1:
								nextGateX = int(word)
							elif i == 2:
								nextGateY = int(word)
							elif i == 3:
								nextGateType = int(word)

							if i % 3 == 0:
								print((nextGateX,nextGateY,nextGateType))

								nextGate = None

								if nextGateType == 1:
									nextGate = Not(parentMap,True)
								elif nextGateType == 2:
									nextGate = And(parentMap,True)
								elif nextGateType == 3:
									nextGate = Or(parentMap,True)
								elif nextGateType == 4:
									nextGate = Xor(parentMap,True)
								elif nextGateType == 5:
									nextGate = Nand(parentMap,True)
								elif nextGateType == 6:
									nextGate = Nor(parentMap,True)
								elif nextGateType == 7:
									nextGate = Nxor(parentMap,True)
								nextGate.setPositionFromData(nextGateX,nextGateY)
								nextGate.setAt()

								parentMap.gates.append(nextGate)
								i = 0
						i += 1

					index += 1
				
		

def writeToFile(fileName,map):
	name = input("Name of destination file with extension:")
	file = open(name,"w+")
	file.write(str(map.size[0])+ " " + str(map.size[1])+" \n")
	print("Saving...")
	for line in map.map:
		textLine = ""
		for col in line:
			if not col.isWire and not col.isInput and not col.isOutput:
				textLine += "0 "
			elif col.isInput:
				textLine += "3 "
			elif col.isOutput:
				textLine += "4 "
			else:
				if col.isWire:
					if not col.isJonction:
						if col.value == 0:	
							textLine += "1 "
							
						elif col.value == 1:
							textLine += "2 "
					else:
						textLine += "5 "
		
		textLine +="\n"
			
		file.write(textLine)
	for g in map.gates:
		print(g.cX)
		t = -1
		if g.name == "NOT":
			t = 1
		elif g.name == "AND":
			t = 2
		elif g.name == "OR":
			t = 3
		elif g.name == "XOR":
			t = 4
		elif g.name == "NAND":
			t = 5
		elif g.name == "NOR":
			t = 6
		elif g.name == "NXOR":
			t = 7
		file.write(str(g.cX)+" "+str(g.cY) +" "+str(t)+"\n")
	print("...save completed")
	file.close()
