import pygame

class ImageLoader:

    #GATES
    AND = None
    OR = None
    XOR = None

    NAND = None
    NOR = None
    NXOR = None

    NOT = None
    DELETE = None

    #MODES
    WIRE = None
    FILE = None
    GATE = None

    #WIRE
    DRAW  = None
    JONCTION = None
    INPUT = None
    OUTPUT = None
    CLICK = None

    #FILE
    LOAD = None
    SAVE = None

    def loadImages():
        ImageLoader.AND = pygame.image.load("images/AND.png")
        ImageLoader.OR = pygame.image.load("images/OR.png")
        ImageLoader.XOR = pygame.image.load("images/XOR.png")

        ImageLoader.NAND = pygame.image.load("images/NAND.png")
        ImageLoader.NOR = pygame.image.load("images/NOR.png")
        ImageLoader.NXOR = pygame.image.load("images/NXOR.png")

        ImageLoader.NOT =  pygame.image.load("images/NOT.png")

        ImageLoader.WIRE = pygame.image.load("images/WIRE.png")
        ImageLoader.GATE = pygame.image.load("images/GATE.png")
        ImageLoader.FILE = pygame.image.load("images/FILE.png")

        ImageLoader.DRAW = pygame.image.load("images/DRAW.png")
        ImageLoader.JONCTION = pygame.image.load("images/JONCTION.png")
        ImageLoader.INPUT = pygame.image.load("images/INPUT.png")
        ImageLoader.OUTPUT = pygame.image.load("images/OUTPUT.png")
        ImageLoader.CLICK = pygame.image.load("images/CLICK.png")
        ImageLoader.DELETE = pygame.image.load("images/ERASER.png")

        ImageLoader.SAVE = pygame.image.load("images/SAVE.png")
        ImageLoader.LOAD = pygame.image.load("images/LOAD.png")