from Bullet import Bullet
import pygame


if __name__ == '__main__':

    pygame.init()
    window = pygame.display.set_mode([512, 768])
    clock = pygame.time.Clock()

    # 初始化子弹
    bullet1 = Bullet(window)
    bullet1.set_used(100, 600)

    bullet2 = Bullet(window)
    bullet2.set_used(300, 600)

    while True:

        # 清空屏幕
        window.fill((0, 0, 0))

        # 子弹坐标
        bullet1.move(0, -5)
        bullet2.move(0, -3)

        # 子弹绘制
        bullet1.draw_element()
        bullet2.draw_element()

        if bullet1.bbox[1] <= 0:
            bullet1.set_used(100, 600)

        if bullet2.bbox[1] <= 0:
            bullet2.set_used(300, 600)

        # 读取事件，避免窗口卡顿
        pygame.event.get()

        pygame.display.update()
        clock.tick(60)