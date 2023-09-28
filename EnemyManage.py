import pygame
import random
from EnemyPlane import EnemyPlane
from Config import *
class EnemyManager:

    ENEMY_START_EVENT = pygame.USEREVENT + 1
    ENEMY_SHOOT_EVENT = pygame.USEREVENT + 2

    def __init__(self, scene):
        # 初始化敌机
        self.enemies = [EnemyPlane(scene) for _ in range(8)]
        # 定时器事件
        pygame.time.set_timer(EnemyManager.ENEMY_START_EVENT, 2000)
        pygame.time.set_timer(EnemyManager.ENEMY_SHOOT_EVENT, 1000)

    def calc_position(self):
        for enemy in self.enemies:
            enemy.calc_position()

    def draw_element(self):
        for enemy in self.enemies:
            enemy.draw_element()

    def set_out(self):

        # 随机选择 1- 4 个飞机
        number = random.randint(1, 4)

        # 候选敌机
        wait_for_out = []
        for enemy in self.enemies:
            if not enemy.visible:
                wait_for_out.append(enemy)
            if len(wait_for_out) == number:
                break

        # 敌机出发
        if len(wait_for_out) == number:

            # 敌机位置
            position_xs = []
            range_distance = int((SCENE_W - 100) / number)
            for index in range(number):
                x = random.randint(index * range_distance, index * range_distance + range_distance - 100)
                position_xs.append(x)

            # 敌机出发
            for enemy, x in zip(wait_for_out, position_xs):
                enemy.set_used(x, -enemy.bbox[3])

    def shoot(self):
        for enemy in self.enemies:
            if not enemy.visible:
                continue
            if random.randint(1, 100) > 50 and enemy.bbox[1] < 500:
                enemy.shoot()