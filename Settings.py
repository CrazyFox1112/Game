import pygame
import sys

width = 1280
height = 720
fps = 60
screen = pygame.display.set_mode((width, height))
# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (139, 0, 0)
GREEN = (0, 100, 0)
BLUE = (0, 0, 255)
GREY = (105, 105, 105)
# Время (фпс)
clock = pygame.time.Clock()
# Основной шрифт
pygame.font.init()
font = pygame.font.Font(None, 36)
text_color = (0, 0, 0)  # Цвет текста (RGB)
text_surface = font.render("Удар!", True, text_color)
# Размер изображения
new_width = 100
new_height = 200


# Класс кнопки
class Button:
    def __init__(self, x, y, width, height, color, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.text != '':
            text_surface = font.render(self.text, True, WHITE)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


# Функция для появления и исчезания текста
# Функция для появления и исчезания текста
def appear_and_disappear_text(text, duration):
    # Выводим текст на экран
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(width // 2, height // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.update(text_rect)

    # Ждем заданное количество миллисекунд
    pygame.time.delay(duration)

    # Убираем текст
    pygame.display.update(text_rect)








