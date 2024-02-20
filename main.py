import pygame
import sys
from settings import *
from ball import Ball
from paddle import Paddle

# создание объектов
pygame.init()
screen = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
clock = pygame.time.Clock()

ball = Ball(SC_WIDTH//2, SC_HEIGHT//2, 10, WHITE, screen)
left_paddle = Paddle(P_OFFSET, SC_HEIGHT//2 - P_HEIGHT//2, WHITE, screen, pygame.K_UP, pygame.K_DOWN)
right_paddle = Paddle(SC_WIDTH - P_OFFSET - P_WIDTH, SC_HEIGHT//2 - P_HEIGHT//2, WHITE, screen, pygame.K_w, pygame.K_s)

# главный цикл
while True:
    # задержка
    clock.tick(FPS)
    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # изменение объектов, update
    ball.update()
    left_paddle.update()
    right_paddle.update()

    #пересечение объектов, collisions
    #левая ракетка
    #нижняя точка мяча, верхний край ракетки
    if ball.get_mid_bottom_x() >= left_paddle.get_x():
        if ball.get_mid_bottom_x() <= left_paddle.get_x() + P_WIDTH:
            if ball.get_mid_bottom_y() >= left_paddle.get_y():
                ball.reverse_speedy()
    
    # обновление экрана
    screen.fill(BLACK)
    ball.draw()
    left_paddle.draw()
    right_paddle.draw()
    pygame.display.update()



    
