import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

# Цвета
grey = (169, 169, 169)
dark_grey = (140, 140, 140)
black = (0, 0, 0)
pink = (255, 182, 193)
light_pink = (255, 228, 225)
white = (255, 255, 255)


def draw_body(surface, x, y, width, height, color):
    '''
    Рисует тело зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_head(surface, x, y, size, color):
    '''
    Рисует голову зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    size - диаметр головы
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    circle(surface, color, (x, y), size // 2)


def draw_ear(surface, x, y, width, height, color):
    '''
    Рисует ухо зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_leg(surface, x, y, width, height, color):
    '''
    Рисует ногу зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_eye(surface, x, y, size, color):
    '''
    Рисует глаз.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    size - размер изображения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    circle(surface, color, (x, y), size)


def draw_nose(surface, x, y, size, color):
    '''
    Рисует нос.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    size - размер изображения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    polygon(surface, color, [(x, y), (x + size // 2, y - size), (x - size // 2, y - size)])


clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    # Заполнение фона
    screen.fill((255, 255, 255))

    # Рисуем зайца
    draw_ear(screen, 180, 150, 40, 100, grey)
    draw_ear(screen, 220, 150, 40, 100, grey)
    draw_ear(screen, 180, 150, 30, 90, pink)
    draw_ear(screen, 220, 150, 30, 90, pink)
    draw_leg(screen, 160, 350, 40, 80, dark_grey)
    draw_leg(screen, 240, 350, 40, 80, dark_grey)
    draw_leg(screen, 180, 370, 40, 80, grey)
    draw_leg(screen, 220, 370, 40, 80, grey)
    draw_body(screen, 200, 300, 100, 150, grey)
    draw_head(screen, 200, 200, 80, grey)
    draw_head(screen, 200, 215, 40, dark_grey)

    # Рисуем глаза
    draw_eye(screen, 185, 190, 5, black)
    draw_eye(screen, 215, 190, 5, black)

    # Рисуем нос
    draw_nose(screen, 200, 210, 10, light_pink)

    pygame.display.update()
pygame.quit()
