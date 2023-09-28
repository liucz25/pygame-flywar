import random
import pygame
from Config import *
from GameMap import GameMap
from HeroPlane import HeroPlane
from EnemyManage import EnemyManager
import sys


# 主场景
class MainScene:

    # 初始化主场景
    def __init__(self):

          # 统计战斗数据
        self.defeat_count = 0  # 击败敌机数
        self.damage_count = 0  # 被击中次数
        self.impact_count = 0  # 被撞击次数

        # 初始化组件
        pygame.init()
        # 初始化时钟
        self.clock = pygame.time.Clock()
        # 初始化游戏窗口
        self.scene = pygame.display.set_mode((SCENE_W, SCENE_H))
        # 设置窗口标题
        pygame.display.set_caption("飞机大战-v1.0 作者: 孟宝亮")
        # 初始化游戏元素
        self.init_elements()
         # 游戏背景音乐
        pygame.mixer.music.load('image/bg.wav')
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(-1)


    # 初始化游戏元素
    def init_elements(self):
        # 初始化游戏地图
        self.map = GameMap(self.scene)
        # 初始化英雄飞机
        self.hero = HeroPlane(self.scene)
        # 初始化敌机序列
        self.enemy = EnemyManager(self.scene)

    # 计算坐标
    def calc_position(self):
        # 计算地图坐标
        self.map.calc_position()
        # 计算英雄弹夹坐标
        self.hero.calc_position()
        # 计算敌机位置
        self.enemy.calc_position()


    # 绘制元素
    def draw_elements(self):
        # 绘制滚动地图
        self.map.draw_element()
        # 绘制英雄飞机
        self.hero.draw_element()
        # 绘制敌机
        self.enemy.draw_element()
        self.draw_battle_data()

    # 处理事件
    def handle_events(self):

        self.detect_conlision()

        # 窗口关闭事件
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 敌机出发事件
            if event.type == EnemyManager.ENEMY_START_EVENT:
                self.enemy.set_out()

            # 敌机发射子弹
            if event.type == EnemyManager.ENEMY_SHOOT_EVENT:
                self.enemy.shoot()

        # 获得当前按下的键
        keys = pygame.key.get_pressed()
        # 射击
        if keys[pygame.K_j]:
            self.hero.shoot(1)

        if keys[pygame.K_k]:
            self.hero.shoot(3)

        if keys[pygame.K_l]:
            self.hero.shoot(5)
        # 上
        if keys[pygame.K_w]:
            self.hero.top()
        # 下
        if keys[pygame.K_s]:
            self.hero.bottom()
        # 左
        if keys[pygame.K_a]:
            self.hero.left()
        # 右
        if keys[pygame.K_d]:
            self.hero.right()

# 碰撞检测
    def detect_conlision(self):
        # 敌机和英雄子弹
        for bullet in self.hero.bullets.bullet_list:
            if not bullet.visible:
                continue
            for enemy in self.enemy.enemies:
                if not enemy.visible or not bullet.visible:
                    continue
                if pygame.Rect.colliderect(bullet.bbox, enemy.bbox):
                    enemy.bomb.set_used(enemy.bbox[0],enemy.bbox[1])
                    self.defeat_count+=1
                    bullet.set_unused()
                    enemy.set_unused()
                    
                    # enemy.bomb.draw_element()
        # 敌机和英雄飞机
        for enemy in self.enemy.enemies:
            if not enemy.visible:
                continue
            if pygame.Rect.colliderect(self.hero.bbox, enemy.bbox):
                enemy.set_unused()
                self.damage_count+=1
        # 敌机子弹和英雄飞机
        for enemy in self.enemy.enemies:
            if not enemy.bullet.visible:
                continue
            if pygame.Rect.colliderect(self.hero.bbox, enemy.bullet.bbox):
                enemy.bullet.set_unused()
                self.impact_count+=1
        # 敌机子弹和英雄子弹
        for enemy in self.enemy.enemies:
            if not enemy.bullet.visible:
                continue
            for bullet in self.hero.bullets.bullet_list:
                if not bullet.visible:
                    continue
                if pygame.Rect.colliderect(bullet.bbox, enemy.bullet.bbox):
                    enemy.bullet.set_unused()
                    bullet.set_unused()



    def draw_battle_data(self):
            # 使用 SimHei 字体，并设置 16 号大小
            font = pygame.font.Font('image/STKAITI.ttf', 16)
            text = f"击毁数:{self.defeat_count} 被击中:{self.damage_count} 被撞击:{self.impact_count}"
            # 文字内容、抗锯齿、颜色
            text = font.render(text, True, (255, 255, 255))
            # 绘制文本内容
            self.scene.blit(text, (150, 20))

    # 主循环
    def run(self):

        while True:
            # 碰撞检测
            self.detect_conlision()
            # 计算元素坐标
            self.calc_position()
            # 绘制元素图片
            self.draw_elements()
            # 处理事件
            self.handle_events()
            # 刷新显示
            pygame.display.update()
            # 控制帧率
            self.clock.tick(60)