import pygame
from constants import *
from player import Player  # Assuming player.py is in the same directory



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    pygame.display.set_caption("Asteroids")
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Initialize player at the center of the screen

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)

        screen.fill((0, 0, 0))  # Fill the screen with black
        player.draw(screen) # Draw the player
        pygame.display.flip()  # Update the display

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000.0  # Calculate delta time in seconds


if __name__ == "__main__":
    main()
