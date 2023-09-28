import random

import pygame
from Config import *

class Bullet:

    def __init__(self, scene, is_enemy=False):

        # 保存主场景
        self.scene = scene
        # 子弹是否可见
        self.visible = False
        # 加载子弹资源
        bullet_index = ENEM_BULLET_INDEX if is_enemy else HERO_BULLET_INDEX
        bullet_filename = f'image/bullet_{bullet_index}.png'
        self.image = pygame.image.load(bullet_filename)
        if is_enemy:
            self.image = pygame.transform.flip(self.image, False, True)
        # 子弹位置边框
        self.bbox = self.image.get_rect()

    def move(self, dx, dy):
        if not self.visible:
            return
        self.bbox.move_ip(dx, dy)
        if self.bbox[1] < 0 or self.bbox[1] > SCENE_H - 10:
            self.set_unused()

    def draw_element(self):
        if not self.visible:
            return
        self.scene.blit(self.image, self.bbox)

    def set_unused(self):
        self.visible = False
        self.bbox[0] = -1000
        self.bbox[1] = -1000

    def set_used(self, start_x, start_y):
        self.visible = True
        self.bbox[0] = start_x
        self.bbox[1] = start_y