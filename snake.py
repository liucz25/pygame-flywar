import pygame
import random
# 游戏窗口大小
WIDTH = 800
HEIGHT = 600
# 蛇身和食物大小
BLOCK_SIZE = 20
# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# 初始化pygame
pygame.init()
# 创建游戏窗口
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇")
# 设置游戏时钟
clock = pygame.time.Clock()
# 蛇的初始位置和移动方向
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = "RIGHT"
# 食物的初始位置
food_position = [random.randrange(1, (WIDTH // BLOCK_SIZE)) * BLOCK_SIZE,
                 random.randrange(1, (HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE]
food_spawned = True
# 游戏结束标志
game_over = False
# 游戏主循环
while not game_over:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = "RIGHT"
            elif event.key == pygame.K_LEFT:
                direction = "LEFT"
            elif event.key == pygame.K_UP:
                direction = "UP"
            elif event.key == pygame.K_DOWN:
                direction = "DOWN"
    # 移动蛇头
    if direction == "RIGHT":
        snake_position[0] += BLOCK_SIZE
    elif direction == "LEFT":
        snake_position[0] -= BLOCK_SIZE
    elif direction == "UP":
        snake_position[1] -= BLOCK_SIZE
    elif direction == "DOWN":
        snake_position[1] += BLOCK_SIZE
    # 增加蛇身长度
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        food_spawned = False
    else:
        snake_body.pop()
    # 生成新的食物
    if not food_spawned:
        food_position = [random.randrange(1, (WIDTH // BLOCK_SIZE)) * BLOCK_SIZE,
                         random.randrange(1, (HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE]
        food_spawned = True
    # 绘制游戏画面
    window.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(window, GREEN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(window, RED, pygame.Rect(food_position[0], food_position[1], BLOCK_SIZE, BLOCK_SIZE))
    # 检测碰撞
    if snake_position[0] >= WIDTH or snake_position[0] < 0 or snake_position[1] >= HEIGHT or snake_position[1] < 0:
        game_over = True
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over = True
    # 刷新游戏画面
    pygame.display.flip()
    # 控制游戏帧率
    clock.tick(10)
# 退出游戏
pygame.quit()