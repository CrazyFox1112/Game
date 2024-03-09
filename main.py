import Heal_Scene
from fight_scene import *
from Settings import *
pygame.init()
pygame.display.set_caption("Main")
battle_scene = BattleScene()
heal_scene = Heal_Scene.HealScene()




# Основной цикл программы
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Проверяем нажатие на клавишу "пробел"
                battle_scene.run()




pygame.quit()
sys.exit()


