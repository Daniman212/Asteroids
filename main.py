import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()

    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        player.update(dt)
        screen.fill((0, 0, 0))  # Fill the screen with black
        player.draw(screen)   # draw the player
        pygame.display.flip()  # Refresh the screen


if __name__ == "__main__":
    main()
