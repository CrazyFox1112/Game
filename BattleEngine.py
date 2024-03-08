import random
from Settings import *


class BattleEngine:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.enemy_last_action = None
        self.enemy_current_action = None

    def player_turn(self, action):

        # Ход игрока
        if action == "атака":
            damage = self.player.attack()
            self.enemy.take_damage(damage)
        elif action == 'лечение':
            heal = self.player.heal_power
            self.player.health += heal

    def enemy_turn(self):
        # Ход врага
        self.enemy_last_action = self.enemy_current_action
        self.enemy_current_action = random.choice(self.enemy.actions)

        if self.enemy_current_action == "атака":
            damage = self.enemy.attack()
            self.player.take_damage(damage)
        elif self.enemy_current_action == 'лечение':
            heal = self.enemy.heal_power
            self.enemy.health += heal

    def check_game_over(self):
        # Проверка на окончание игры
        if self.player.health <= 0:
            return True

        elif self.enemy.health <= 0:
            return True
        return False




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


def appear_and_disappear_text(text, duration):
    start_time = pygame.time.get_ticks()  # Запоминаем время начала отображения текста

    while pygame.time.get_ticks() - start_time < duration:  # Пока не прошло достаточно времени
        # Выводим текст на экран
        screen.fill(WHITE)
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=(width // 2, height // 2))
        screen.blit(text_surface, text_rect)
        pygame.display.update(text_rect)

