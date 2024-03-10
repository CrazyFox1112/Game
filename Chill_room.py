from Units import *
from Settings import *
import pygame
from BattleEngine import Button
import Heal_Min_Game

heal_min_game = Heal_Min_Game.Heal_Min_game()


class Chill_room_scene:
    def __init__(self):
        self.alpha = 0
        self.HealButton = Button((width - (button_width + 50)) // 2, (height - (button_height + 25)) // 2,
                                 button_width + 50,
                                 button_height + 25, (2, 46, 14), WHITE, 'Лечение')


    def run(self):
        running = True
        while running:

            # Плавный переход от черного фона к изображению
            if self.alpha < 255:
                self.alpha += 10  # Увеличиваем значение альфа-канала
                background_image_2.set_alpha(self.alpha)  # Устанавливаем значение альфа-канала изображению
            else:
                self.alpha = 255  # Полностью непрозрачный

            screen.fill(BLACK)  # Заливаем экран черным цветом
            screen.blit(background_image_2, background_rect_2)  # Отображаем изображение с установленным альфа-каналом

            player.draw_hp_bar(width // 2 - 575, height // 2 + 285, 250, 30)
            hp = "Ваше ХП " + str(player.health)
            hp_surface = font.render(hp, True, WHITE)
            hp_rect = hp_surface.get_rect(center=(width // 2 - 450, height // 2 + 300))
            screen.blit(hp_surface, hp_rect)

            # Отображение кнопки
            self.HealButton.color = (0, 100, 0, self.alpha / 2)
            self.HealButton.colortext = (255, 255, 255, self.alpha / 2)
            self.HealButton.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.HealButton.is_clicked(pygame.mouse.get_pos()):
                        heal_min_game.run()
                        running = False

            pygame.display.flip()
            clock.tick(60)  # Ограничение FPS
