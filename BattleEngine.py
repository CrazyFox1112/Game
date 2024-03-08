import random


class BattleEngine:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.enemy_last_action = None
        self.enemy_current_action = None

    def player_turn(self, action):

        # Ход игрока
        if action == "attack":
            damage = self.player.attack()
            self.enemy.take_damage(damage)
        elif action == 'heal':
            heal = self.player.heal_power
            self.player.health += heal

    def enemy_turn(self):
        # Ход врага
        self.enemy_last_action = self.enemy_current_action
        self.enemy_current_action = random.choice(self.enemy.actions)

        if self.enemy_current_action == "attack":
            damage = self.enemy.attack()
            self.player.take_damage(damage)
        elif self.enemy_current_action == 'heal':
            heal = self.enemy.heal_power
            self.enemy.health += heal
    def check_game_over(self):
        # Проверка на окончание игры
        if self.player.health <= 0:
            return True

        elif self.enemy.health <= 0:
            return True
        return False
