import sys
import pygame
from constants import *
from player import Player 
from asteroid import Asteroid 
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Asteroids")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()


    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Initialize player at the center of the screen

    dt = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.colision(asteroid):
                print("Game Over!")
                sys.exit()

        screen.fill((0, 0, 0))  # Fill the screen with black
        
        for obj in drawable:
            obj.draw(screen) # Draw the player

        pygame.display.flip()  # Update the display

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000.0  # Calculate delta time in seconds


if __name__ == "__main__":
    main()
