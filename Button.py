from GUIElement import *
from Color import *
import pygame

class Button(GUIElement):
    

    def __init__(self,x,y,w,h,bgColor,pressedColor,onClickAction,image = None):
        GUIElement.__init__(self,x,y,w,h)
        self.bgColor = bgColor
        self.pressedColor = pressedColor
        self.onClickAction = onClickAction
        self.isHovered = False
        self.isPressed = False
        self.canUpdate = True
        self.image = image
        if self.image != None:
            self.image = pygame.transform.scale(image,(self.w,self.h))
        

    def render(self,screen):
        if self.isPressed:
            if self.isHovered:
                screen.fill(Color.darken(self.pressedColor,20),self.rect)
            else:
                screen.fill(self.pressedColor,self.rect)
        else:
            if self.isHovered:
                screen.fill(Color.darken(self.bgColor,20),self.rect)
            else:
                screen.fill(self.bgColor,self.rect)

        pygame.draw.rect(screen,Color.black,self.rect,2)

        if self.image != None:
            screen.blit(self.image,self.rect)

    def update(self):
        (mX,mY)=pygame.mouse.get_pos()
        (l,m,r)=pygame.mouse.get_pressed()
        if (mX > self.x and mY > self.y and
            mX < self.x + self.w and 
            mY < self.y + self.h):
                self.isHovered = True
                if l and self.canUpdate: 
                    self.isPressed = not self.isPressed
                    if self.isPressed:
                        self.onClickAction()
                    self.canUpdate = False
        else:
            self.isHovered = False
            self.canUpdate = True

    def dePush(self):
        self.isPressed = False