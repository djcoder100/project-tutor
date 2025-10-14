import pygame
import random
import sys
import os

# --- SETUP ---
pygame.init()
pygame.mixer.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks Deluxe")

# Colors
WHITE = (255, 255, 255)
RED = (255, 50, 50)
BLUE = (50, 150, 255)
BLACK = (10, 10, 10)

# Player setup
player_size = 50
player_speed = 7

# Enemy setup
enemy_size = 50
enemy_list = []
enemy_speed = 5
spawn_rate = 0.02  # starting spawn rate

# Game setup
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 32)
large_font = pygame.font.SysFont("Arial", 64)

# --- ASSETS ---

# Make sure these files exist in the same folder as your script:
# - background.jpg (or .png)
# - music.mp3 (or .wav)

# Load background image
if os.path.exists("background.jpg"):
    background = pygame.image.load("background.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
else:
    background = None

# Load and play background music (loop)
if os.path.exists("music.mp3"):
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)  # -1 means loop forever
    pygame.mixer.music.set_volume(0.5)

# Load hit sound
if os.path.exists("hit.wav"):
    hit_sound = pygame.mixer.Sound("hit.wav")
else:
    hit_sound = None  # optional fallback


# --- FUNCTIONS ---
def drop_enemies(enemy_list, rate):
    """Spawn enemies at random positions"""
    if len(enemy_list) < 10 and random.random() < rate:
        x_pos = random.randint(0, WIDTH - enemy_size)
        enemy_list.append([x_pos, 0])


def draw_enemies(enemy_list):
    """Draw all enemies"""
    for enemy in enemy_list:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))


def update_enemy_positions(enemy_list, speed):
    """Move enemies down the screen"""
    new_list = []
    for enemy in enemy_list:
        enemy[1] += speed
        if enemy[1] < HEIGHT:
            new_list.append(enemy)
    return new_list


def detect_collision(px, py, ex, ey):
    """Detect collision between player and enemy"""
    return (
        ex < px + player_size and ex + enemy_size > px and
        ey < py + player_size and ey + enemy_size > py
    )


def show_text_centered(text, font, color, y):
    """Draw centered text"""
    label = font.render(text, True, color)
    screen.blit(label, (WIDTH // 2 - label.get_width() // 2, y))


def game_loop():
    """Main game loop"""
    player_x = WIDTH // 2
    player_y = HEIGHT - player_size * 2
    score = 0
    difficulty = 1
    global enemy_list
    enemy_list = []

    running = True
    while running:
        clock.tick(30)

        # Draw background (image or solid color)
        if background:
            screen.blit(background, (0, 0))
        else:
            screen.fill(BLACK)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
            player_x += player_speed

        # Enemy logic
        drop_enemies(enemy_list, spawn_rate + difficulty * 0.002)
        enemy_list = update_enemy_positions(enemy_list, enemy_speed + difficulty * 0.5)

        # Check collisions
        for enemy in enemy_list:
            if detect_collision(player_x, player_y, enemy[0], enemy[1]):
                if hit_sound:
                    hit_sound.play()
                return score

        # Increase score and difficulty
        score += 1
        difficulty = 1 + score / 200

        # Draw everything
        draw_enemies(enemy_list)
        pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

        # Display score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.update()


def game_over_screen(score):
    """Display restart or quit screen"""
    if background:
        screen.blit(background, (0, 0))
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
    else:
        screen.fill(BLACK)

    show_text_centered("GAME OVER", large_font, RED, HEIGHT // 2 - 80)
    show_text_centered(f"Final Score: {score}", font, WHITE, HEIGHT // 2)
    show_text_centered("Press SPACE to Restart or ESC to Quit", font, WHITE, HEIGHT // 2 + 60)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


# --- MAIN LOOP ---
while True:
    final_score = game_loop()
    game_over_screen(final_score)
