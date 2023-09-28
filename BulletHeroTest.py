from BulletHero import BulletForHero
import pygame


if __name__ == '__main__':

    pygame.init()
    window = pygame.display.set_mode([512, 768])
    clock = pygame.time.Clock()

    # 初始化弹夹
    bullets = BulletForHero(window)


    while True:

        # 清空屏幕
        window.fill((0, 0, 0))

        # 子弹坐标
        bullets.calc_position()
        # 子弹绘制
        bullets.draw_element()
        # 发射子弹
        bullets.shoot(250, 600, 3)

        # 读取事件，避免窗口卡顿
        pygame.event.get()

        pygame.display.update()
        clock.tick(60)