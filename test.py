import pygame
import random
import sys

# 초기화
pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks")
clock = pygame.time.Clock()

# 색상
WHITE = (255, 255, 255)
BLUE = (0, 102, 255)
RED = (255, 50, 50)
PINK = (255, 105, 180)
GREEN = (0, 200, 0)
BROWN = (139, 69, 19)

# 플레이어
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 5

# 적
enemy_size = 30
enemy_list = []
enemy_speed = 5

# 점수
score = 0
font = pygame.font.SysFont(None, 36)

def drop_enemies(enemy_list):
    if len(enemy_list) < 7 and random.random() < 0.05:
        x_pos = random.randint(0, WIDTH - enemy_size)
        enemy_list.append([x_pos, 0])

def draw_enemies(enemy_list):
    for enemy in enemy_list:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))

def update_enemy_positions(enemy_list, score):
    for enemy in enemy_list:
        enemy[1] += enemy_speed
    enemy_list = [enemy for enemy in enemy_list if enemy[1] < HEIGHT]
    score += 1
    return enemy_list, score

def collision_check(enemy_list, player_rect):
    for enemy in enemy_list:
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_size, enemy_size)
        if player_rect.colliderect(enemy_rect):
            return True
    return False

def show_score(score):
    text = font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(text, (10, 10))

# 메인 루프
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    drop_enemies(enemy_list)
    enemy_list, score = update_enemy_positions(enemy_list, score)

    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    pygame.draw.rect(screen, BLUE, player_rect)
    draw_enemies(enemy_list)

    if collision_check(enemy_list, player_rect):
        text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(text, (WIDTH // 2 - 80, HEIGHT // 2 - 20))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    show_score(score // 10)
    pygame.display.update()
    clock.tick(30)