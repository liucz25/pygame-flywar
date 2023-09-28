import pygame
class Bomb:

    def __init__(self, scene):
        # 加载爆炸素材
        self.images = [ pygame.image.load(f'image/bomb-{index + 1}.png') for index in range(7)]
        # 爆炸位置
        self.position = [0, 0]
        # 帧播放间隔
        self.interval = 5
        self.interval_index = 0
        # 当前绘制的图像
        self.draw_index = 0
        # 爆炸是否可见
        self.visible = False
        # 持有场景对象
        self.scene = scene
        # 加载爆炸音效
        self.sound = pygame.mixer.Sound('image/baozha.ogg')
        self.sound.set_volume(0.1)

    def set_used(self, start_x, start_y):
        self.visible = True
        self.draw_index = 0
        self.position[0] = start_x
        self.position[1] = start_y
        self.sound.play()

    def set_unused(self):
        self.visible = False
        self.draw_index = 0
        self.position[0] = -1000
        self.position[1] = -1000

    def switch_frame(self):
        if not self.visible:
            return
        self.interval_index += 1
        if self.interval_index < self.interval:
            return
        self.interval_index = 0

        self.draw_index += 1
        if self.draw_index >= len(self.images):
            self.set_unused()

    def draw_element(self):
        if not self.visible:
            return
        self.scene.blit(self.images[self.draw_index], self.position)