import pygame
import math
from dataclasses import dataclass
from typing import Tuple, List

# Инициализация Pygame
pygame.init()
FPS = 30
screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))

@dataclass
class Color:
    """Класс для хранения цветов"""
    WHITE: Tuple[int, int, int] = (255, 255, 255)
    BLACK: Tuple[int, int, int] = (0, 0, 0)
    PINK: Tuple[int, int, int] = (255, 100, 100)
    GRAY: Tuple[int, int, int] = (200, 200, 200)

@dataclass
class HareConfig:
    """Конфигурация зайца"""
    position: Tuple[int, int] = (250, 250)
    size: Tuple[int, int] = (200, 400)
    color: Tuple[int, int, int] = Color.GRAY
    ear_inner_color_ratio: float = 0.5  # Отношение цвета внутренней части уха к основному

class DrawingUtils:
    @staticmethod
    def draw_pixel(surface, x, y, color):
        """Рисует пиксель на поверхности с проверкой границ"""
        if 0 <= x < surface.get_width() and 0 <= y < surface.get_height():
            surface.set_at((int(x), int(y)), color)

    @staticmethod
    def draw_circle(surface, center_x, center_y, radius, color):
        """Рисует круг вручную"""
        for y in range(int(center_y - radius), int(center_y + radius) + 1):
            for x in range(int(center_x - radius), int(center_x + radius) + 1):
                if math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2) <= radius:
                    DrawingUtils.draw_pixel(surface, x, y, color)

    @staticmethod
    def draw_ellipse(surface, x, y, width, height, color):
        """Рисует эллипс вручную"""
        hw = width / 2
        hh = height / 2
        cx = x + hw
        cy = y + hh

        for py in range(int(y), int(y + height) + 1):
            for px in range(int(x), int(x + width) + 1):
                dx = (px - cx) / hw
                dy = (py - cy) / hh
                if dx ** 2 + dy ** 2 <= 1:
                    DrawingUtils.draw_pixel(surface, px, py, color)

    @staticmethod
    def draw_arc(surface, x, y, width, height, start_angle, end_angle, color, thickness=1):
        """Рисует дугу вручную"""
        hw = width / 2
        hh = height / 2
        cx = x + hw
        cy = y + hh

        for py in range(int(y), int(y + height) + 1):
            for px in range(int(x), int(x + width) + 1):
                dx = (px - cx) / hw
                dy = (py - cy) / hh
                angle = math.atan2(dy, dx)
                if (start_angle <= angle <= end_angle) and (0.9 <= dx ** 2 + dy ** 2 <= 1.1):
                    DrawingUtils.draw_pixel(surface, px, py, color)

class HareComponents:
    @staticmethod
    def draw_body(surface, x, y, width, height, color):
        """Рисует тело зайца"""
        DrawingUtils.draw_ellipse(surface, x - width // 2, y - height // 2, width, height, color)

    @staticmethod
    def draw_head(surface, x, y, size, color):
        """Рисует голову зайца с глазами, носом и ртом"""
        # Голова
        DrawingUtils.draw_circle(surface, x, y, size // 2, color)

        # Глаза
        eye_size = size // 8
        eye_positions = [
            (x - size // 6, y - size // 10),  # Левый глаз
            (x + size // 6, y - size // 10)   # Правый глаз
        ]
        for ex, ey in eye_positions:
            DrawingUtils.draw_circle(surface, ex, ey, eye_size, Color.WHITE)
            DrawingUtils.draw_circle(surface, ex, ey, eye_size // 2, Color.BLACK)

        # Нос
        nose_size = size // 12
        DrawingUtils.draw_circle(surface, x, y + size // 10, nose_size, Color.PINK)

        # Рот
        mouth_width = size // 3
        mouth_height = size // 10
        mouth_y = y + size // 4
        DrawingUtils.draw_arc(surface,
                            x - mouth_width // 2,
                            mouth_y - mouth_height // 2,
                            mouth_width, mouth_height,
                            0.2, 2.94, Color.BLACK)

    @staticmethod
    def draw_ear(surface, x, y, width, height, color, inner_color_ratio):
        """Рисует ухо зайца с внутренней частью"""
        # Внешняя часть уха
        DrawingUtils.draw_ellipse(surface, x - width // 2, y - height // 2, width, height, color)
        
        # Внутренняя часть уха (более темная)
        inner_color = (int(color[0] * inner_color_ratio), 
                      int(color[1] * inner_color_ratio), 
                      int(color[2] * inner_color_ratio))
        DrawingUtils.draw_ellipse(surface,
                                x - width // 3,
                                y - height // 3,
                                width * 2 // 3, height * 2 // 3,
                                inner_color)

    @staticmethod
    def draw_leg(surface, x, y, width, height, color):
        """Рисует лапу зайца"""
        DrawingUtils.draw_ellipse(surface, x - width // 2, y - height // 2, width, height, color)

class Hare:
    def __init__(self, surface, config=HareConfig()):
        self.surface = surface
        self.config = config
        self.x, self.y = config.position
        self.width, self.height = config.size
        self.color = config.color

    def draw(self):
        """Рисует всего зайца"""
        # Тело
        body_width = self.width // 2
        body_height = self.height // 2
        body_y = self.y + body_height // 2
        HareComponents.draw_body(self.surface, self.x, body_y, body_width, body_height, self.color)

        # Голова
        head_size = self.height // 4
        HareComponents.draw_head(self.surface, self.x, self.y - head_size // 2, head_size, self.color)

        # Уши
        ear_height = self.height // 3
        ear_y = self.y - self.height // 2 + ear_height // 2
        ear_width = self.width // 8
        ear_positions = [
            (self.x - head_size // 4, ear_y),  # Левое ухо
            (self.x + head_size // 4, ear_y)   # Правое ухо
        ]
        for ex, ey in ear_positions:
            HareComponents.draw_ear(self.surface, ex, ey, ear_width, ear_height, 
                                  self.color, self.config.ear_inner_color_ratio)

        # Лапы
        leg_height = self.height // 16
        leg_y = self.y + self.height // 2 - leg_height // 2
        leg_width = self.width // 4
        leg_positions = [
            (self.x - self.width // 4, leg_y),  # Левая лапа
            (self.x + self.width // 4, leg_y)    # Правая лапа
        ]
        for lx, ly in leg_positions:
            HareComponents.draw_leg(self.surface, lx, ly, leg_width, leg_height, self.color)

# Создаем и рисуем стандартного зайца (большой серый в центре)
hare1 = Hare(screen)
hare1.draw()

# Создаем и рисуем кастомного зайца (меньший розовый в левом верхнем углу)
custom_config = HareConfig(
    position=(100, 100),
    size=(150, 300),
    color=(220, 180, 180),  # светло-розовый
    ear_inner_color_ratio=0.6
)
hare2 = Hare(screen, custom_config)
hare2.draw()

# Основной цикл
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
