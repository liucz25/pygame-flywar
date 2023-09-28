import pygame
from EnemyManage import EnemyManager
if __name__ == '__main__':

    pygame.init()
    window = pygame.display.set_mode([512, 768])
    clock = pygame.time.Clock()

    # 初始化敌机管理器
    enemy = EnemyManager(window)

    while True:

        # 清空窗口
        window.fill((0, 0, 0))
        # 敌机位置
        enemy.calc_position()
        # 绘制敌机
        enemy.draw_element()
        # 处理定时器事件
        events = pygame.event.get()
        for event in events:
            if event.type == EnemyManager.ENEMY_START_EVENT:
                enemy.set_out()
            if event.type == EnemyManager.ENEMY_SHOOT_EVENT:
                enemy.shoot()
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()
        clock.tick(60)