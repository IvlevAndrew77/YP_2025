import pygame
from pygame.draw import *
pygame.init()
# Константы
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
FPS = 30
COLORS = {
    'grey': (169, 169, 169),
    'dark_grey': (140, 140, 140),
    'black': (0, 0, 0),
    'pink': (255, 182, 193),
    'light_pink': (255, 228, 225),
    'white': (255, 255, 255)
}


class Hare:
    def __init__(self, surface):
        self.surface = surface
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2

    def draw_body(self, x, y, width, height, color): #Рисует тело зайца
        ellipse(self.surface, color, (x - width // 2, y - height // 2, width, height))

    def draw_head(self, x, y, size, color):# Рисует голову зайца
        circle(self.surface, color, (x, y), size // 2)

    def draw_ear(self, x, y, width, height, outer_color, inner_color=None): #Рисует ухо зайца с цветом
        ellipse(self.surface, outer_color, (x - width // 2, y - height // 2, width, height))
        if inner_color:
            ellipse(self.surface, inner_color,
                    (x - width // 3, y - height // 3, width * 2 // 3, height * 2 // 3))

    def draw_limb(self, x, y, width, height, color):# Общая функция для рисования ног

        ellipse(self.surface, color, (x - width // 2, y - height // 2, width, height))

    def draw_face(self, x, y):# Рисует глаза, нос
        # Глаза
        circle(self.surface, COLORS['black'], (x - 15, y - 10), 5)
        circle(self.surface, COLORS['black'], (x + 15, y - 10), 5)

        # Нос (треугольник)
        polygon(self.surface, COLORS['light_pink'],
                [(x, y), (x + 5, y - 10), (x - 5, y - 10)])

    def draw(self): # метод рисования
        # Уши (внешняя и внутренняя часть)
        self.draw_ear(180, 150, 40, 100, COLORS['grey'], COLORS['pink'])
        self.draw_ear(220, 150, 40, 100, COLORS['grey'], COLORS['pink'])

        # Ноги
        self.draw_limb(160, 350, 40, 80, COLORS['dark_grey'])
        self.draw_limb(240, 350, 40, 80, COLORS['dark_grey'])
        self.draw_limb(180, 370, 40, 80, COLORS['grey'])
        self.draw_limb(220, 370, 40, 80, COLORS['grey'])

        # Тело и голова
        self.draw_body(200, 300, 100, 150, COLORS['grey'])
        self.draw_head(200, 200, 80, COLORS['grey'])
        self.draw_head(200, 215, 40, COLORS['dark_grey'])

        # Мордочка
        self.draw_face(200, 210)


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Рисуем зайца")
    clock = pygame.time.Clock()

    hare = Hare(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(COLORS['white'])
        hare.draw()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()