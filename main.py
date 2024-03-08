
from fight_scene import *

from Settings import *
pygame.init()
pygame.display.set_caption("Main")
battle_scene = BattleScene()




# Основной цикл программы
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Проверяем нажатие на кнопку
            if battle_scene.button_attack.is_clicked(pygame.mouse.get_pos()) or battle_scene.button_heal.is_clicked(pygame.mouse.get_pos()):
                # Запускаем сцену битвы
                battle_scene.run()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Проверяем нажатие на клавишу "пробел"
                battle_scene.run()
                enemy.health = enemy.max_health

    pygame.display.flip()


pygame.quit()
sys.exit()


