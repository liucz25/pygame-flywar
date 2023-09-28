import pygame
from EnemyPlane import EnemyPlane
import random
from Config import *
if __name__ == '__main__':

    pygame.init()
    window = pygame.display.set_mode([512, 768])
    clock = pygame.time.Clock()

    enemy = EnemyPlane(window)
    enemy.set_used(random.randint(0, SCENE_W - enemy.bbox[2]), -enemy.bbox[3])

    index = 0
    while True:
        # 清空窗口
        window.fill((0, 0, 0))
        # 计算位置
        enemy.calc_position()
        # 绘制敌机
        enemy.draw_element()
        # 发射子弹
        index += 1
        if index > 120 and random.randint(1, 100) > 80 and enemy.bbox[1] < 300:
            enemy.shoot()
            index = 0

        # 敌机复活
        if not enemy.visible:
            enemy.set_used(random.randint(0, SCENE_W - enemy.bbox[2]), -enemy.bbox[3])

        pygame.event.get()
        pygame.display.update()
        clock.tick(60)