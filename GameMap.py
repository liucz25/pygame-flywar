import random

import pygame
from Config import *


class GameMap:

    # 初始化地图
    def __init__(self, scene):

        # 地图编号
        map_index = MAP_INDEX if MAP_INDEX >= 1 and MAP_INDEX <= 5 else random.randint(1, 5)
        map_filename = f'image/img_bg_level_{map_index}.jpg'

        # 加载相同图片资源,做交替实现地图滚动
        self.image1 = pygame.image.load(map_filename)
        self.image2 = self.image1.copy()

        # 地图滚动速度
        self.scroll_speed = 3

        # 保存场景对象
        self.main_scene = scene

        # 初始化两张图片初始化位置
        self.y1 = 0
        self.y2 = -SCENE_H

    # 计算地图图片绘制坐标
    def calc_position(self):
        self.y1 = 0 if self.y1 >= SCENE_H else self.y1 + self.scroll_speed
        self.y2 = -SCENE_H if self.y2 >=0 else self.y2 + self.scroll_speed


    # 绘制地图的两张图片
    def draw_element(self):
        self.main_scene.blit(self.image1, (0, self.y1))
        self.main_scene.blit(self.image2, (0, self.y2))