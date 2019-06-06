import pygame
from GUIElement import *
from Color import *


class Panel(GUIElement):
    
    children = []
    bgColor = None

    def __init__(self,x,y,w,h,bgColor):

        GUIElement.__init__(self,x,y,w,h)
        self.children = []
        self.bgColor = bgColor
        self.rect = pygame.Rect(self.x-1,self.y,self.w+1,self.h)

    def addChild(self,child):
        child.x += self.x
        child.y += self.y
        child.rect = pygame.Rect(child.x,child.y,child.w,child.h)
        self.children.append(child)

    def removeChild(self,index):
        if index > len(self.children) - 1 or index < 0:
            return
        del self.children[index]

    def render(self,screen):

        
        #fill
        screen.fill(self.bgColor, self.rect)

        #border
        pygame.draw.rect(screen, Color.black, self.rect , 2)

        for i in range(len(self.children)):
            self.children[i].render(screen)

    def update(self):
        for i in range(len(self.children)):
            self.children[i].update()