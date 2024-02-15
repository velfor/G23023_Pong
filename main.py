import pygame
import sys
from settings import *
from ball import Ball

# здесь происходит инициация,
# создание объектов
pygame.init()
screen = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
clock = pygame.time.Clock()

ball = Ball(SC_WIDTH//2, SC_HEIGHT//2, 10, WHITE, screen)

# главный цикл
while True:
    # задержка
    clock.tick(FPS)
    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # --------
    # изменение объектов
    # --------
    ball.update()
    
    # обновление экрана
    screen.fill(BLACK)
    ball.draw()
    pygame.display.update()



    
