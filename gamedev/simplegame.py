import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("GameDev")

# define a player
player = pygame.Rect(300, 250, 50, 50)

def main():
    run = True
    while run:

        # Refresh the screen
        SCREEN.fill((0, 0, 0))

        # Draw the player
        pygame.draw.rect(SCREEN, (250, 0, 0), player)

        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.move_ip(0, -1)
            # player.y -= 1
        if keys[pygame.K_s]:
            player.move_ip(0, 1)
            # player.y += 1
        if keys[pygame.K_a]:
            player.move_ip(-1, 0)
            # player.x -= 1
        if keys[pygame.K_d]:
            player.move_ip(1, 0)
            # player.x += 1   

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Update the screen
        pygame.display.update()
    pygame.quit()    
        

if __name__ == "__main__":
    main()
