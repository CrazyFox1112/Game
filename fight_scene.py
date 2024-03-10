import pygame
import sys
from Settings import *
from BattleEngine import *
from Units import *
import time
# Движок
class BattleScene:
    def __init__(self):
        self.battle_engine = BattleEngine(player, enemy)

        self.alpha = 0
        # Кнопки
        self.button_attack = Button(button1_x, button_y, button_width, button_height, (RED[0], RED[1], RED[2], 255), (WHITE[0], WHITE[1], WHITE[2], 255 ), 'Attack')
        self.button_heal = Button(button2_x, button_y, button_width, button_height, (RED[0], RED[1], RED[2], 255), (WHITE[0], WHITE[1], WHITE[2], 255 ),'Heal')

        # Сила удара пресонажей
        self.force_enemy_info = font.render('Сила {}'.format(enemy.attack_power), True, RED)
        self.force_player_info = font.render('Сила {}'.format(player.attack_power), True, RED)

        # Сила лечения
        self.heal_enemy_info = font.render('Лечение {}'.format(enemy.heal_power), True, GREEN)
        self.heal_player_info = font.render('Лечение {}'.format(player.heal_power), True, GREEN)


    # Основной цикл программы
    def run(self):
        running = True
        while running:

            # Плавный переход от черного фона к изображению
            if self.alpha < 255:
                self.alpha += 1  # Увеличиваем значение альфа-канала
                background_image_1.set_alpha(self.alpha)  # Устанавливаем значение альфа-канала изображению
            else:
                alpha = 255  # Полностью непрозрачный



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:

                    # Кнопка 1
                    if self.button_attack.is_clicked(pygame.mouse.get_pos()):
                        player_action = 'атака'
                        self.battle_engine.player_turn(player_action)
                        if not self.battle_engine.check_game_over():
                            self.battle_engine.enemy_turn()
                        if self.battle_engine.check_game_over():
                            running = False
                        show_text('противник использовал: {}'.format(self.battle_engine.enemy_current_action), 1000)



                    # Кнопка 2
                    elif self.button_heal.is_clicked(pygame.mouse.get_pos()):
                        player_action = 'лечение'
                        self.battle_engine.player_turn(player_action)
                        if not self.battle_engine.check_game_over():
                            self.battle_engine.enemy_turn()
                        if self.battle_engine.check_game_over():
                            running = False
                        show_text('противник использовал: {}'.format(self.battle_engine.enemy_current_action), 1000)

            screen.blit(background_image_1, background_rect_1)

            # Прямоугольники сверху и снизу
            pygame.draw.rect(screen, (GREY[0], GREY[1], GREY[2], self.alpha), (0, 0, 1280, 100))
            pygame.draw.rect(screen, (26, 26, 26, self.alpha), (0, 90, 1280, 10))
            pygame.draw.rect(screen, (GREY[0], GREY[1], GREY[2], self.alpha), (0, 620, 1280, 100))
            pygame.draw.rect(screen, (26, 26, 26, self.alpha), (0, 610, 1280, 10))

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

            self.button_attack.draw(screen)
            self.button_heal.draw(screen)

            screen.blit(self.force_enemy_info, (10, 20))
            screen.blit(self.force_player_info, (1120, 645))

            screen.blit(self.heal_enemy_info, (10, 60))
            screen.blit(self.heal_player_info, (1120, 685))






            pygame.display.flip()
            clock.tick(60)  # Ограничение FPS
