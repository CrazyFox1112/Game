import pygame
import sys
from BattleEngine import *
from Units import *
from Settings import *
# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Надпись с таймером в Pygame")

# Шрифт для текста
font = pygame.font.Font(None, 36)

# Основной цикл программы
running = True
while running:

    button.draw()
    button_2.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # второй слот
            if button.is_clicked(pygame.mouse.get_pos()):
                player_action = 'attack'
                battle_engine.player_turn(player_action)
                if not battle_engine.check_game_over():
                    battle_engine.enemy_turn()
                if enemy.health <= 0 or player.health <= 0:
                    sys.exit()
                appear_and_disappear_text("Удар!", 1000)

            # Первый слот
            elif button_2.is_clicked(pygame.mouse.get_pos()):
                player_action = 'heal'
                battle_engine.player_turn(player_action)
                if not battle_engine.check_game_over():
                    battle_engine.enemy_turn()
                if enemy.health <= 0 or player.health <= 0:
                    sys.exit()
                appear_and_disappear_text("Лечение!", 1000)

    pygame.display.flip()

# Выход из программы
pygame.quit()
sys.exit()

import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Text Display")

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Создание шрифта
font = pygame.font.Font(None, 36)


def display_text(text, duration):
    # Выводим текст на экран
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(width // 2, height // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

    # Ждем заданное количество миллисекунд
    pygame.time.delay(duration)

    # Убираем текст
    screen.fill(WHITE)
    pygame.display.flip()


# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Выводим текст на 3 секунды, затем убираем его
    display_text("Hello, world!", 3000)
    pygame.time.delay(2000)

# Выход из программы
pygame.quit()
sys.exit()

