import pygame
from HeroPlane import HeroPlane
import random

if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode([512, 768])
    clock = pygame.time.Clock()
    # 初始化英雄飞机
    hero = HeroPlane(window)
    actions = [hero.left, hero.right, hero.top, hero.bottom]

    index = 0
    action_index = 0
    while True:

        # 清空窗口
        window.fill((0, 0, 0))
        # 计算坐标
        hero.calc_position()
        # 绘制图像
        hero.draw_element()
        # 发射子弹
        hero.shoot(3)

        # 随机选择方向
        actions[action_index]()
        index += 1
        if index > 50:
            action_index = random.randint(0, 3)
            index = 0

        events = pygame.event.get()
        for event in events:

            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()
        clock.tick(60)