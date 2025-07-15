import pygame
import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_MAX_RADIUS



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, screen):
       pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()  # Remove the current asteroid

        # Logic to split the asteroid into smaller ones
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Create two smaller asteroids
    
        degrees = random.uniform(20, 50)
        
        velocity1 = self.velocity.rotate(degrees)
        velocity2 = self.velocity.rotate(-degrees)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        position1 = self.position + pygame.Vector2(0, 1).rotate(degrees) * self.radius
        position2 = self.position + pygame.Vector2(0, 1).rotate(-degrees) * self.radius
        
        asteroid1 = Asteroid(position1.x, position1.y, new_radius)
        asteroid2 = Asteroid(position2.x, position2.y, new_radius)
        
        asteroid1.velocity = velocity1 * 1.2
        asteroid2.velocity = velocity2 * 1.2