from Settings import *


class Character:
    def __init__(self, name, health, attack_power, heal_power, actions=None):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.heal_power = heal_power
        self.actions = actions if actions is not None else []

    def attack(self):
        return self.attack_power

    def heal(self):
        return self.heal_power

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

    def draw_hp_bar(self, x, y, width, height):
        # Рассчитываем длину HP bar
        hp_bar_length = int((self.health / self.max_health) * width)

        # Рисуем рамку HP bar
        pygame.draw.rect(screen, BLACK, (x, y, width, height), 2)

        # Рисуем текущий HP bar
        if self.health > 0.4 * self.max_health:
            pygame.draw.rect(screen, GREEN, (x, y, hp_bar_length, height))
        else:
            pygame.draw.rect(screen, RED, (x, y, hp_bar_length, height))


player = Character("Игрок", health=100, attack_power=20, heal_power=10, actions=["атака", "лечение"])
enemy = Character("Враг", health=100, attack_power=10, heal_power=5, actions=["атака", "лечение"])

