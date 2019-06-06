import pygame      

class GUIElement:
    x = 0
    y = 0
    w = 0
    h = 0

    def __init__(self,x,y,w,h):

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        

    def render(self):
        pass

    def update(self):
        pass
