import pygame
from settings import *

class Ball:

    def __init__(self, x, y, r, color, screen):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.speedx = 2
        self.speedy = 3
        self.screen = screen

    def update(self):
        #изменение координат
        self.x += self.speedx
        self.y += self.speedy
        #проверка на границы экрана
        #правая
        if self.x + self.r >= SC_WIDTH:
            self.speedx = -self.speedx
        #левая
        if self.x - self.r <= 0:
            self.speedx = -self.speedx
        #верхняя
        if self.y - self.r <= 0:
            self.speedy = -self.speedy    
        #нижняя
        if self.y + self.r >= SC_HEIGHT:
            self.speedy = -self.speedy

    def draw(self):
        pygame.draw.circle(self.screen, WHITE, (self.x, self.y), self.r)




            
