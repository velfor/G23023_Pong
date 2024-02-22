import pygame
import sys
from settings import *
from ball import Ball
from paddle import Paddle
from text_obj import Text_Obj

# создание объектов
pygame.init()
screen = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
clock = pygame.time.Clock()

ball = Ball(SC_WIDTH//2, SC_HEIGHT//2, 10, WHITE, screen)
left_paddle = Paddle(P_OFFSET, SC_HEIGHT//2 - P_HEIGHT//2, WHITE, screen, pygame.K_UP, pygame.K_DOWN)
right_paddle = Paddle(SC_WIDTH - P_OFFSET - P_WIDTH, SC_HEIGHT//2 - P_HEIGHT//2, WHITE, screen, pygame.K_w, pygame.K_s)
left_text = Text_Obj(100, 20, ball.get_left_score(), screen)
right_text = Text_Obj(650, 20, ball.get_right_score(), screen)


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
    left_text.update(ball.get_left_score())
    right_text.update(ball.get_right_score())

    #пересечение объектов, collisions
    #левая ракетка
    #нижняя точка мяча, верхний край ракетки
    if ball.get_mid_bottom_x() >= left_paddle.get_x():
        if ball.get_mid_bottom_x() <= left_paddle.get_x() + P_WIDTH:
            if ball.get_mid_bottom_y() >= left_paddle.get_y():
                ball.reverse_speedy()
    #левая часть мяча, правый край ракетки
    if ball.get_mid_left_x() <= left_paddle.get_x() + P_WIDTH:
        if ball.get_mid_left_y() >= left_paddle.get_y():
            if ball.get_mid_left_y() <= left_paddle.get_y() + P_HEIGHT:
                ball.reverse_speedx()
    #верхняя точка мяча, нижний край ракетки
    if ball.get_mid_top_x() >= left_paddle.get_x():
        if ball.get_mid_top_x() <= left_paddle.get_x() + P_WIDTH:
            if ball.get_mid_top_y() <= left_paddle.get_y() + P_HEIGHT:
                ball.reverse_speedy()

    #правая ракетка
    #нижняя точка мяча, верхний край ракетки
    if ball.get_mid_bottom_x() >= right_paddle.get_x():
        if ball.get_mid_bottom_x() <= right_paddle.get_x() + P_WIDTH:
            if ball.get_mid_bottom_y() >= right_paddle.get_y():
                ball.reverse_speedy()
    #правая часть мяча, левый край ракетки
    if ball.get_mid_right_x() >= right_paddle.get_x():
        if ball.get_mid_right_y() >= right_paddle.get_y():
            if ball.get_mid_right_y() <= right_paddle.get_y() + P_HEIGHT:
                ball.reverse_speedx()
    #верхняя точка мяча, нижний край ракетки
    if ball.get_mid_top_x() >= right_paddle.get_x():
        if ball.get_mid_top_x() <= right_paddle.get_x() + P_WIDTH:
            if ball.get_mid_top_y() <= right_paddle.get_y() + P_HEIGHT:
                ball.reverse_speedy()            
    # обновление экрана
    screen.fill(BLACK)
    ball.draw()
    left_paddle.draw()
    right_paddle.draw()
    left_text.draw()
    right_text.draw()
    pygame.display.update()



    
