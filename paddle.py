import pygame
from settings import *

class Paddle:

    def __init__(self, x, y, color, screen):
       self.x = x
       self.y = y
       self.color = color
       self.width = P_WIDTH
       self.height = P_HEIGHT
       self.speedy = P_SPEEDY
       self.screen = screen

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
           self.y -= self.speedy
        elif keys[pygame.K_DOWN]:
            self.y += self.speedy

        if self.y <= 0:
            self.y = 0
        if self.y >= SC_HEIGHT - P_HEIGHT:
            self.y = SC_HEIGHT - P_HEIGHT

    def draw(self):
        pygame.draw.rect(self.screen, WHITE, (self.x, self.y, self.width, self.height))



    
            
