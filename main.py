#IMPORTS
import pygame
import sys
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

#GROUPS
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots_group = pygame.sprite.Group()

#CONTAINERS
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = updatable
Shot.containers = (shots_group, updatable, drawable)

# MY MAIN THANG
def main():
    pygame.init()
    clock = pygame.time.Clock()

    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# GAME LOOP
    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()  # Call the shoot method on the player
            
        # Update and handle collisions    
        for entity in updatable:
            entity.update(dt)

        # Check shot-asteroid collisions
        for asteroid in asteroids:
            for shot in shots_group:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.kill()
            if player.check_collision(asteroid):
                print("Game over!")
                sys.exit()

        screen.fill((0, 0, 0))  # Fill the screen with black

        for entity in drawable:
            entity.draw(screen)    # draw the player

        pygame.display.flip()  # Refresh the screen

# HOLLER BACK NOW
if __name__ == "__main__":
    main()
