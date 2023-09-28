import pygame
from BulletHero import BulletForHero
from Config import *


class HeroPlane:

    def __init__(self, scene):
        # 游戏主场景
        self.scene = scene
        # 英雄飞机资源
        self.image = pygame.image.load(f'image/hero.png')
        # 英雄飞机边框
        self.bbox = self.image.get_rect()
        # 初始化飞机位置
        self.bbox[0] = SCENE_W / 2 - self.bbox[2] / 2
        self.bbox[1] = SCENE_H - self.bbox[3] - 10
        # 初始化弹夹
        self.bullets = BulletForHero(scene)
        # 移动速度
        self.speed = 4


    def top(self):
        if self.bbox[1] <= 0:
            return
        self.bbox.move_ip(0, -self.speed)

    def bottom(self):
        if self.bbox[1] >= SCENE_H - self.bbox[3]:
            return
        self.bbox.move_ip(0, self.speed)

    def left(self):
        if self.bbox[0] <= 0:
            return
        self.bbox.move_ip(-self.speed, 0)

    def right(self):
        if self.bbox[0] >= (SCENE_W - self.bbox[2]):
            return
        self.bbox.move_ip(self.speed, 0)

    def shoot(self, num):
        shoot_x = self.bbox[0] + self.bbox[2] / 2
        shoot_y = self.bbox[1]
        self.bullets.shoot(shoot_x, shoot_y, num)

    def draw_element(self):
        self.scene.blit(self.image, self.bbox)
        self.bullets.draw_element()

    def calc_position(self):
        self.bullets.calc_position()