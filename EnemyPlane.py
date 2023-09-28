import pygame
import random
from Bullet import Bullet
from Config import *
from Bomb import Bomb
class EnemyPlane:

    def __init__(self, scene, speed=10):
        # 游戏主场景
        self.scene = scene
        # 敌机资源
        self.image = pygame.image.load(f'image/img-plane_{random.randint(1, 7)}.png')
        # 敌机边框
        self.bbox = self.image.get_rect()
        # 移动速度
        self.speed = speed
        # 是否可见
        self.visible = False
        # 初始化子弹
        self.bullet = Bullet(scene, is_enemy=True)
        # 初始化爆炸
        self.bomb = Bomb(self.scene)

    def set_used(self, start_x, start_y):
        self.bbox[0] = start_x
        self.bbox[1] = start_y
        self.speed = random.randint(4, 8)
        self.visible = True


    def calc_position(self):

        # 计算飞机位置
        if self.visible:
            self.bbox.move_ip(0, self.speed)
            if self.bbox[1] > SCENE_H:
                self.set_unused()

        # 计算子弹位置
        if self.bullet.visible:
            self.bullet.move(0, self.speed + 5)
                # -----------爆炸效果----------
        # 切换爆炸帧
        self.bomb.switch_frame()

    def draw_element(self):
        # 绘制飞机
        if self.visible:
            self.scene.blit(self.image, self.bbox)
        # 绘制子弹
        if self.bullet.visible:
            self.bullet.draw_element()
        # 绘制爆炸图片
        self.bomb.draw_element()

    def set_unused(self):
        self.visible = False
        self.bbox[0] = -1000
        self.bbox[1] = -1000

    def shoot(self):
        if self.bullet.visible:
            return
        start_x = self.bbox[0] + self.bbox[2]/2 - self.bullet.bbox[2]/2
        start_y = self.bbox[1] + self.bbox[3] - 10
        self.bullet.set_used(start_x, start_y)