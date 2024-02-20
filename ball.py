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
        self.calc_mids()

    def calc_mids(self):
        self.mid_top_x = self.x
        self.mid_top_y = self.y - self.r
        self.mid_right_x = self.x + self.r
        self.mid_right_y = self.y
        self.mid_bottom_x = self.x
        self.mid_bottom_y = self.y + self.r
        self.mid_left_x = self.x - self.r
        self.mid_left_y = self.y
        
    def update(self):
        #изменение координат
        self.x += self.speedx
        self.y += self.speedy
        
        self.calc_mids()
        
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


    def get_mid_top_x(self):
        return self.mid_top_x
    
    def get_mid_top_y(self):
        return self.mid_top_y

    def get_mid_right_x(self):
        return self.mid_right_x

    def get_mid_right_y(self):
        return self.mid_right_y    

    def get_mid_bottom_x(self):
        return self.mid_bottom_x

    def get_mid_bottom_y(self):
        return self.mid_bottom_y

    def get_mid_left_x(self):
        return self.mid_left_x

    def get_mid_left_y(self):
        return self.mid_left_y

    def reverse_speedx(self):
        self.speedx = -self.speedx

    def reverse_speedy(self):
        self.speedy = -self.speedy



        
