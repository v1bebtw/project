import sys
import pygame as pg
import random


pg.init()

FPS = 120
window_width = 600
window_height = 400

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
background_color = (128, 128, 128)

r = 25

width_rect = 100
height_rect = 10

x_rect = (window_width // 2 - width_rect // 2)
y_rect = window_height - height_rect
direct_x_rect = 5

x_ball = random.randint(25, window_width - 25)
y_ball = random.randint(25, 100)
direct_x_ball, direct_y_ball = 1, 1

screen = pg.display.set_mode((window_width, window_height))

clock = pg.time.Clock()

score_count = 0

pg.display.set_caption("Ping-Pong")
img = pg.image.load('logo.png')
pg.display.set_icon(img)

run = True

while run:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            print(score_count)
            sys.exit()
        elif i.type == pg.MOUSEMOTION:
            position = i.pos
            x_rect = position[0] - width_rect // 2

    """Анимация"""
    clock.tick(FPS)
    screen.fill(background_color)
    pg.event.pump()

    ball = pg.draw.circle(screen, green, (x_ball, y_ball), r)
    pg.draw.rect(screen, red, (x_rect, y_rect, width_rect, height_rect))

    """Перемещение"""
    if pg.key.get_pressed()[pg.K_LEFT]:
        if x_rect > 0:
            x_rect -= direct_x_rect
    elif pg.key.get_pressed()[pg.K_RIGHT]:
        if x_rect + width_rect < window_width:
            x_rect += direct_x_rect

    """Изменение по OX"""
    x_ball += direct_x_ball
    if x_ball > window_width - r or x_ball < 0 + r:
        direct_x_ball = -direct_x_ball

    """Изменение по OY"""
    y_ball += direct_y_ball
    if y_ball < 0 + r:
        direct_y_ball = -direct_y_ball

    """Соприкосновение с платформой"""
    if x_ball in range(x_rect, x_rect + width_rect) and y_ball + r == y_rect:
        if direct_x_ball < 8 and direct_y_ball < 8:
            direct_x_ball += 0.5
            direct_y_ball += 0.5
        direct_y_ball = -direct_y_ball
        score_count += 1

    if y_ball + r >= window_height:
        font_ = pg.font.SysFont('tahoma', 32)
        text = font_.render(f'Ваш счёт: {score_count}', True, red)
        screen.blit(text, (200, 175))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_KP_ENTER:
                    x_ball, y_ball = random.randint(25, window_width - 25), random.randint(25, 100)
                    score_count = 0

    pg.display.update()

