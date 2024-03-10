import pygame
from Settings import *
import time
from BattleEngine import *
from Units import *
import time


class Heal_Min_game:
    def __init__(self):
        self.alpha = 0
        self.HealButton = Button((width - (button_width + 50)) // 2, (height - (button_height + 25)) // 2,
                                 button_width + 50,
                                 button_height + 25, (2, 46, 14), WHITE, 'Лечение')
        self.heal_time = 5

    def run(self):
        timer_running = False
        start_ticks = pygame.time.get_ticks()
        seconds = 0
        running = True
        countdawn = self.heal_time
        while running:

            if timer_running:
                elapsed_time = pygame.time.get_ticks() - start_ticks
                seconds = (elapsed_time / 1000) - 1
                countdawn = self.heal_time - seconds
            if self.alpha < 255:
                self.alpha += 10  # Увеличиваем значение альфа-канала
                background_image_2.set_alpha(self.alpha)  # Устанавливаем значение альфа-канала изображению
            else:
                self.alpha = 255  # Полностью непрозрачный

            screen.fill(BLACK)  # Заливаем экран черным цветом
            screen.blit(background_image_2, background_rect_2)

            self.HealButton.color = (0, 100, 0, self.alpha - 10)
            self.HealButton.colortext = (255, 255, 255, self.alpha - 10)
            self.HealButton.draw(screen)

            text = font.render('Нажимай на кнопку в течении {} секунд'.format(round(countdawn, 2)), True, WHITE)
            text_rect = text_surface.get_rect(center=(screen.get_width() // 2 - 200, screen.get_height() // 2 - 300))
            screen.blit(text, text_rect)

            player.draw_hp_bar(width // 2 - 575, height // 2 + 285, 250, 30)
            hp = "Ваше ХП " + str(player.health)
            hp_surface = font.render(hp, True, WHITE)
            hp_rect = hp_surface.get_rect(center=(width // 2 - 450, height // 2 + 300))
            screen.blit(hp_surface, hp_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.HealButton.is_clicked(pygame.mouse.get_pos()):
                        timer_running = True
                        player.health += 1

            if self.heal_time - seconds < 0:
                running = False

            pygame.display.flip()
            pygame.time.Clock().tick(60)

