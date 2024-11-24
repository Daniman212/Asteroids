import pygame
from circleshape import CircleShape

class Shot(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def update(self, dt):
        self.position += (self.velocity * dt)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, 1)