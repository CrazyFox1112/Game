import pygame
import sys
import Settings

def appear_and_disappear_text(text, duration):
    start_time = pygame.time.get_ticks()  # Запоминаем время начала отображения текста

    while pygame.time.get_ticks() - start_time < duration:  # Пока не прошло достаточно времени
        # Выводим текст на экран
        screen.fill(WHITE)
        text_surface = Settings.font.render(text, True, Settings.BLACK)
        text_rect = text_surface.get_rect(center=(width // 2, height // 2))
        screen.blit(text_surface, text_rect)
        pygame.display.update(text_rect)

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Semi-Transparent Rectangles")

# Цвета
WHITE = (255, 255, 255)
GREY = (128, 128, 128, 128)  # Серый цвет с уровнем прозрачности 128

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(Settings.background_image_1, Settings.background_rect_1)  # Заливка экрана белым цветом


    pygame.display.flip()

# Выход из программы
pygame.quit()
sys.exit()
