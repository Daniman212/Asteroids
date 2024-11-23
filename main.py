import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = updatable

def main():
    pygame.init()
    clock = pygame.time.Clock()

    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for entity in updatable:
            entity.update(dt)
        screen.fill((0, 0, 0))  # Fill the screen with black
        for entity in drawable:
            entity.draw(screen)    # draw the player

        pygame.display.flip()  # Refresh the screen


if __name__ == "__main__":
    main()
