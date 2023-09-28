import math
from Bullet import Bullet


class BulletForHero:

    def __init__(self, scene):
        # 初始化子弹列表
        self.bullet_list = [Bullet(scene) for _ in range(15)]
        # 子弹发射频率
        self.frame_limit = 8
        self.frame_index = 0

    def calc_position(self):
        for bullet in self.bullet_list:
            bullet.move(0, -15)

    def draw_element(self):
        for bullet in self.bullet_list:
            bullet.draw_element()

    def shoot(self, start_x, start_y, shoot_number):

        self.frame_index += 1
        if self.frame_index < self.frame_limit:
            return
        self.frame_index = 0

        # 计算子弹初始位置
        distance = 31
        position_xs = [ start_x + (index - math.floor(shoot_number / 2)) * distance for index in range(shoot_number)]

        wait_for_shoot = []
        for bullet in self.bullet_list:
            if not bullet.visible:
                wait_for_shoot.append(bullet)
            if len(wait_for_shoot) == shoot_number:
                break

        if len(wait_for_shoot) == shoot_number:
            for bullet, x in zip(wait_for_shoot, position_xs):
                bullet.set_used(x - bullet.bbox[2]/2, start_y - bullet.bbox[3])