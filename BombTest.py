from Bomb import *
if __name__ == '__main__':

    pygame.init()
    window = pygame.display.set_mode([512, 768])
    clock = pygame.time.Clock()

    # 初始化爆炸对象
    bomb = Bomb(window)
    bomb.set_used(200, 450)

    while True:
        window.fill((0, 0, 0))

        # 切换爆炸图片
        bomb.switch_frame()
        # 绘制爆炸图片
        bomb.draw_element()

        if not bomb.visible:
            bomb.set_used(200, 450)

        pygame.event.get()
        pygame.display.update()
        clock.tick(60)