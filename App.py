import sys,pygame
from Cell import *
from Map import *
from Color import *
from Panel import *
from Button import *
from ImageLoader import *
from Utils import *


class App:


	

	
	windowSize = None
	size = None
	screen = None
	running = False
	cellMap = []
	editMode = 0
	option = 1
	buttonDown = False
	FONT = None

	GUIROOT = None

	MODES = None

	WIRE_OPTIONS = None
	GATE_OPTIONS = None
	FILE_OPTIONS = None

	#mode buttons
	wireMode = None
	gateMode = None
	fileMode = None

	#wire mode button
	drawOption = None
	jonctionOption = None
	inputOption = None
	outputOption = None
	clickOption = None
	

	#gate mode button
	notOption = None
	andOption = None
	orOption = None
	xorOption = None
	nandOption = None
	norOption = None
	nxorOption = None
	deleteOption = None
	
	#file mode button
	saveFileOption = None
	loadFileOption = None


	CELL_SIZE = 20
	ROWS = None
	COLS = None
	
	def init(self):
		ImageLoader.loadImages()

		#refactoring needed
		self.windowSize = [1000,700]
		self.size = [1000,640]
		self.running = True
		GUISize = (self.windowSize[0],self.windowSize[1]-self.size[1])

		#CELLMAP
		App.ROWS = int(self.size[1] / self.CELL_SIZE)
		App.COLS = int(self.size[0] / self.CELL_SIZE)
		cellMap = Map(0,GUISize[1],(App.ROWS,App.COLS),App.CELL_SIZE)
		self.cellMap = cellMap
		#writeToFile("hello.txt",cellMap)
		#readFromFile("hello.txt")


		#GUI
		App.GUIROOT = Panel(0,0,GUISize[0],GUISize[1],Color.yellow)

		App.MODES = Panel(0,0,200,GUISize[1],Color.darkGray)

		def setWireMode():
			App.editMode = 0
			App.option = 1
			App.gateMode.dePush()
			App.fileMode.dePush()
			if len(App.GUIROOT.children) >= 2:
				App.GUIROOT.removeChild(1)
			App.GUIROOT.addChild(App.WIRE_OPTIONS)


		App.wireMode = Button(10,5,50,50,Color.green,Color.red,setWireMode,ImageLoader.WIRE)
		App.MODES.addChild(App.wireMode)

		def setGateMode():
			App.editMode = 1
			App.option = 1
			App.wireMode.dePush()
			App.fileMode.dePush()
			if len(App.GUIROOT.children) >= 2:
				App.GUIROOT.removeChild(1)
			App.GUIROOT.addChild(App.GATE_OPTIONS)

		App.gateMode = Button(70,5,50,50,Color.green,Color.red,setGateMode,ImageLoader.GATE)
		App.MODES.addChild(App.gateMode)

		def setFileMode():
			App.editMode = 2
			App.option = 1
			App.wireMode.dePush()
			App.gateMode.dePush()
			if len(App.GUIROOT.children) >= 2:
				App.GUIROOT.removeChild(1)
			App.GUIROOT.addChild(App.FILE_OPTIONS)

		App.fileMode = Button(130,5,50,50,Color.green,Color.red,setFileMode,ImageLoader.FILE)
		App.MODES.addChild(App.fileMode)



		App.WIRE_OPTIONS =  Panel(200,0,800,GUISize[1],Color.blue)


		def setDrawOption():
			App.option = 1
			App.jonctionOption.dePush()
			App.inputOption.dePush()
			App.outputOption.dePush()
			App.clickOption.dePush()
		
		App.drawOption = Button(10 ,5,50,50,Color.green,Color.red,setDrawOption,ImageLoader.DRAW)

		def setJonctionOption():
			App.option = 2
			App.drawOption.dePush()
			App.inputOption.dePush()
			App.outputOption.dePush()
			App.clickOption.dePush()

		App.jonctionOption = Button(20 + 50,5,50,50,Color.green,Color.red,setJonctionOption,ImageLoader.JONCTION)

		def setInputOption():
			App.option = 3
			App.jonctionOption.dePush()
			App.drawOption.dePush()
			App.outputOption.dePush()
			App.clickOption.dePush()

		App.inputOption = Button(30 + 100,5,50,50,Color.green,Color.red,setInputOption,ImageLoader.INPUT)

		def setOutputOption():
			App.option = 4
			App.jonctionOption.dePush()
			App.inputOption.dePush()
			App.drawOption.dePush()
			App.clickOption.dePush()

		App.outputOption = Button(40 + 150,5,50,50,Color.green,Color.red,setOutputOption,ImageLoader.OUTPUT)

		def setClickOption():
			App.option = 5
			App.jonctionOption.dePush()
			App.inputOption.dePush()
			App.outputOption.dePush()
			App.drawOption.dePush()

		App.clickOption = Button(50 + 200,5,50,50,Color.green,Color.red,setClickOption,ImageLoader.CLICK)

		#add button
		App.WIRE_OPTIONS.addChild(App.drawOption)
		App.WIRE_OPTIONS.addChild(App.jonctionOption)
		App.WIRE_OPTIONS.addChild(App.inputOption)
		App.WIRE_OPTIONS.addChild(App.outputOption)
		App.WIRE_OPTIONS.addChild(App.clickOption)

		App.GATE_OPTIONS =  Panel(200,0,800,GUISize[1],Color.lightGray)

		def setNotOption():
			App.option = 1
			App.andOption.dePush()
			App.orOption.dePush()
			App.xorOption.dePush()
			App.nandOption.dePush()
			App.norOption.dePush()
			App.nxorOption.dePush()
			App.deleteOption.dePush()

		App.notOption = Button(10,5,50,50,Color.green,Color.red,setNotOption,ImageLoader.NOT)

		def setAndOption():
			App.option = 2
			App.notOption.dePush()
			App.orOption.dePush()
			App.xorOption.dePush()
			App.nandOption.dePush()
			App.norOption.dePush()
			App.nxorOption.dePush()
			App.deleteOption.dePush()


		App.andOption = Button(20+50,5,50,50,Color.green,Color.red,setAndOption,ImageLoader.AND)

		def setOrOption():
			App.option = 3
			App.notOption.dePush()
			App.andOption.dePush()
			App.xorOption.dePush()
			App.nandOption.dePush()
			App.norOption.dePush()
			App.nxorOption.dePush()
			App.deleteOption.dePush()

		App.orOption = Button(30+100,5,50,50,Color.green,Color.red,setOrOption,ImageLoader.OR)

		def setXorOption():
			App.option = 4
			App.notOption.dePush()
			App.andOption.dePush()
			App.orOption.dePush()
			App.nandOption.dePush()
			App.norOption.dePush()
			App.nxorOption.dePush()
			App.deleteOption.dePush()

		App.xorOption = Button(40+150,5,50,50,Color.green,Color.red,setXorOption,ImageLoader.XOR)

		def setNandOption():
			App.option = 5
			App.notOption.dePush()
			App.andOption.dePush()
			App.orOption.dePush()
			App.xorOption.dePush()
			App.norOption.dePush()
			App.nxorOption.dePush()
			App.deleteOption.dePush()

		App.nandOption = Button(50+200,5,50,50,Color.green,Color.red,setNandOption,ImageLoader.NAND)

		def setNorOption():
			App.option = 6
			App.notOption.dePush()
			App.andOption.dePush()
			App.orOption.dePush()
			App.xorOption.dePush()
			App.nandOption.dePush()
			App.nxorOption.dePush()
			App.deleteOption.dePush()

		App.norOption = Button(60+250,5,50,50,Color.green,Color.red,setNorOption,ImageLoader.NOR)

		def setNxorOption():
			App.option = 7
			App.notOption.dePush()
			App.andOption.dePush()
			App.orOption.dePush()
			App.xorOption.dePush()
			App.nandOption.dePush()
			App.norOption.dePush()
			App.deleteOption.dePush()
			

		App.nxorOption = Button(70+300,5,50,50,Color.green,Color.red,setNxorOption,ImageLoader.NXOR)

		def setDeleteOption():
			App.option = 8
			App.notOption.dePush()
			App.andOption.dePush()
			App.orOption.dePush()
			App.xorOption.dePush()
			App.nandOption.dePush()
			App.norOption.dePush()
			
			

		App.deleteOption = Button(70+300,5,50,50,Color.green,Color.red,setDeleteOption,ImageLoader.DELETE)

		App.GATE_OPTIONS.addChild(App.notOption)
		App.GATE_OPTIONS.addChild(App.andOption)
		App.GATE_OPTIONS.addChild(App.orOption)
		App.GATE_OPTIONS.addChild(App.xorOption)
		App.GATE_OPTIONS.addChild(App.nandOption)
		App.GATE_OPTIONS.addChild(App.norOption)
		App.GATE_OPTIONS.addChild(App.nxorOption)
		App.GATE_OPTIONS.addChild(App.deleteOption)




		App.FILE_OPTIONS =  Panel(200,0,800,GUISize[1],Color.lightGray)

		def setSaveFileOption():
			writeToFile("hello.txt",self.cellMap)
			App.saveFileOption.dePush()
			
		App.saveFileOption = Button(10,5,50,50,Color.green,Color.red,setSaveFileOption,ImageLoader.SAVE)


		def setLoadFileOption():
			readFromFile("hello.txt",self.cellMap)
			App.loadFileOption.dePush()
			
		App.loadFileOption = Button(20+50,5,50,50,Color.green,Color.red,setLoadFileOption,ImageLoader.LOAD)

		App.FILE_OPTIONS.addChild(App.saveFileOption)
		App.FILE_OPTIONS.addChild(App.loadFileOption)

		App.GUIROOT.addChild(App.MODES)

		
   
		#App.GUIROOT.addChild(OPTIONS)

		#PYGAME
		pygame.init()
		pygame.font.init()

		
		App.FONT = pygame.font.SysFont("arial", 16, bold=False, italic=False)

		self.screen = pygame.display.set_mode(self.windowSize)
		
		
		
		
	def render(self):
		#background
		self.screen.fill(Color.black)

		#GUI
		App.GUIROOT.render(self.screen)

		#cellMap
		self.cellMap.render(self.screen)
		
		#refresh
		pygame.display.flip()
	
	def update(self):
		#GUI
		App.GUIROOT.update()

		if pygame.key.get_pressed()[pygame.K_w]:
			App.editMode = 0
		if pygame.key.get_pressed()[pygame.K_g]:
			App.editMode = 1

		if pygame.key.get_pressed()[pygame.K_1]:
			App.option = 1

		if pygame.key.get_pressed()[pygame.K_2]:
			App.option = 2

		if pygame.key.get_pressed()[pygame.K_3]:
			App.option = 3

		if pygame.key.get_pressed()[pygame.K_4]:
			App.option = 4
		
		if pygame.key.get_pressed()[pygame.K_5]:
			App.option = 5
		
		if pygame.key.get_pressed()[pygame.K_6]:
			App.option = 6

		if pygame.key.get_pressed()[pygame.K_7]:
			App.option = 7

		if pygame.key.get_pressed()[pygame.K_8]:
			App.option = 8
		self.cellMap.update()
		#print(pygame.mouse.get_pos())
		
	def run(self):
		self.init()
		print("running...")
		while self.running:
			for e in pygame.event.get():	
				if e.type == pygame.QUIT:
					self.running = False
				if e.type == pygame.MOUSEBUTTONUP:
					buttonDown = True
				if e.type == pygame.MOUSEBUTTONUP:
					buttonDown = False
			self.render()
			self.update()
		sys.exit()
		print("App closed")
