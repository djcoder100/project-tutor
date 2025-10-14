import pygame
import random
import math
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Load images (you can replace with your own PNGs)
player_img = pygame.Surface((50, 40))
player_img.fill(BLUE)

enemy_img = pygame.Surface((40, 30))
enemy_img.fill(RED)

bullet_img = pygame.Surface((5, 15))
bullet_img.fill(WHITE)

# Sounds (optional)
shoot_sound = None
explosion_sound = None

# Player setup
player_x = WIDTH // 2 - 25
player_y = HEIGHT - 70
player_x_change = 0
player_speed = 6

# Enemy setup
num_of_enemies = 6
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []

for i in range(num_of_enemies):
    enemy_x.append(random.randint(0, WIDTH - 40))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(3)
    enemy_y_change.append(40)

# Bullet setup
bullet_x = 0
bullet_y = player_y
bullet_y_change = 10
bullet_state = "ready"  # "ready" = can't see bullet, "fire" = bullet is moving

# Score setup
score_value = 0
font = pygame.font.SysFont("Arial", 32)
text_x = 10
text_y = 10

def show_score(x, y):
    score = font.render(f"Score: {score_value}", True, WHITE)
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_img, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 22, y - 20))

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((enemy_x - bullet_x)**2 + (enemy_y - bullet_y)**2)
    return distance < 27

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Keyboard movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -player_speed
            if event.key == pygame.K_RIGHT:
                player_x_change = player_speed
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player_x_change = 0

    # Update player position
    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= WIDTH - 50:
        player_x = WIDTH - 50

    # Enemy movement
    for i in range(num_of_enemies):
        # Game Over
        if enemy_y[i] > HEIGHT - 100:
            for j in range(num_of_enemies):
                enemy_y[j] = 2000  # move enemies off screen
            show_score(WIDTH//2 - 80, HEIGHT//2)
            pygame.display.update()
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()

        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0:
            enemy_x_change[i] = 3
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= WIDTH - 40:
            enemy_x_change[i] = -3
            enemy_y[i] += enemy_y_change[i]

        # Collision
        if is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
            bullet_y = player_y
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0, WIDTH - 40)
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i], i)

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
    if bullet_y <= 0:
        bullet_y = player_y
        bullet_state = "ready"

    # Draw player and score
    player(player_x, player_y)
    show_score(text_x, text_y)

    pygame.display.update()
