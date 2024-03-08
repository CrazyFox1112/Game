import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Text Display")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Шрифт и его размер
font = pygame.font.Font(None, 36)

# Функция для вывода текста на экран и его последующего исчезновения
def display_text(message, duration):
    text_surface = font.render(message, True, WHITE)
    text_rect = text_surface.get_rect(center=(width // 2, height // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()  # Обновление экрана, чтобы текст отобразился

    # Ожидаем заданное количество миллисекунд
    pygame.time.wait(duration)

    # После истечения времени исчезаем текст
    text_rect.x = -text_rect.width  # Перемещаем текст за пределы экрана
    pygame.display.flip()  # Обновляем экран, чтобы скрыть текст

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                display_text("Привет, мир!", 2000)  # Вызываем функцию для вывода текста на 2 секунды

    pygame.display.update()

# Выход из программы
pygame.quit()
sys.exit()

