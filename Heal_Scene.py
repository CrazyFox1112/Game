from Units import *
from Settings import *
import pygame
from BattleEngine import Button


class HealScene:
    def __init__(self):
        self.text_alpha = 0  # Изначально текст непрозрачен
        self.text_surface = font.render('Текст появился!', True, WHITE)
        self.text_rect = self.text_surface.get_rect(center=(width // 2, height - 50))
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

            # Устанавливаем альфа-канал для текста
            self.text_surface.set_alpha(self.text_alpha)
            screen.blit(self.text_surface, self.text_rect)

            # Отображение кнопки
            self.HealButton.color = (0, 100, 0, self.alpha / 2)
            self.HealButton.colortext = (255, 255, 255, self.alpha / 2)
            self.HealButton.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.HealButton.is_clicked(pygame.mouse.get_pos()):
                        self.text_alpha = 255

            pygame.display.flip()
            clock.tick(60)  # Ограничение FPS
