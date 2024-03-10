import pygame

import Chill_room
from fight_scene import *
from Settings import *
pygame.init()
pygame.display.set_caption("Main")
battle_scene = BattleScene()
Chill_scene = Chill_room.Chill_room_scene()
import Heal_Min_Game
Heal_scene = Heal_Min_Game.Heal_Min_game()



# Основной цикл программы
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:# Проверяем нажатие на клавишу "пробел"
                Chill_scene.run()
            elif event.key == pygame.K_TAB:
                battle_scene.run()

    pygame.display.flip()




pygame.quit()
sys.exit()


