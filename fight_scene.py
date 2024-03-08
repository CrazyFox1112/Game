import pygame
import sys
from Settings import *
import BattleEngine
from Units import *

# Движок
battle_engine = BattleEngine.BattleEngine(player, enemy)

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
pygame.display.set_caption("Fight Scene")

# Загрузка изображения фона
background_image = pygame.image.load('img/BG_2.jpg')
background_rect = background_image.get_rect()

# Создание двух кнопок
button_width = 100
button_height = 50
button_padding = 20
button1_x = (width - button_width * 2 - button_padding) // 2
button2_x = button1_x + button_width + button_padding
button_y = (height - button_height)

button = Button(button1_x, button_y, button_width, button_height, RED, 'Attack')
button_2 = Button(button2_x, button_y, button_width, button_height, RED, 'Heal')

# Основной цикл программы
running = True
while running:

    clock.tick(60)
    screen.blit(background_image, background_rect)

    # Прямоугольники сверху и снизу

    pygame.draw.rect(screen, GREY, (0, 0, 1280, 100))
    pygame.draw.rect(screen, (26, 26, 26), (0, 90, 1280, 10))
    pygame.draw.rect(screen, GREY, (0, 620, 1280, 100))
    pygame.draw.rect(screen, (26, 26, 26), (0, 610, 1280, 10))

    enemy.draw_hp_bar(width // 2 + 325, height // 2 - 335, 250, 30)
    hp_enemy = "Хп Врага " + str(enemy.health)
    hp_enemy_surface = font.render(hp_enemy, True, WHITE)
    hp_enemy_rect = hp_enemy_surface.get_rect(center=(width // 2 + 450, height // 2 - 320))
    screen.blit(hp_enemy_surface, hp_enemy_rect)

    player.draw_hp_bar(width // 2 - 575, height // 2 + 285, 250, 30)
    hp = "Ваше ХП " + str(player.health)
    hp_surface = font.render(hp, True, WHITE)
    hp_rect = hp_surface.get_rect(center=(width // 2 - 450, height // 2 + 300))
    screen.blit(hp_surface, hp_rect)

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

                appear_and_disappear_text("противник использовал {}".format(battle_engine.enemy_current_action), 2000)






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
