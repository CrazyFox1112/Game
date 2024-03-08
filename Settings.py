import pygame


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
button_width = 100
button_height = 50
button_padding = 20
# Загрузка изображения фона
background_image = pygame.image.load('img/BG_2.jpg')
background_rect = background_image.get_rect()
# Создание двух кнопок

button1_x = (width - button_width * 2 - button_padding) // 2
button2_x = button1_x + button_width + button_padding
button_y = (height - button_height)










