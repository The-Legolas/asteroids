import pygame
from circleshape import *
from constants import PLAYER_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        # Initialize player-specific attributes
        self.rotation = 0  # Player's rotation angle
        self.shoot_timer = 0  # Timer for shooting cooldown

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        
        
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
        ## Keep the player within the screen bounds
        self.position.x = max(PLAYER_RADIUS, min(SCREEN_WIDTH - PLAYER_RADIUS, self.position.x))
        self.position.y = max(PLAYER_RADIUS, min(SCREEN_HEIGHT - PLAYER_RADIUS, self.position.y))

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_position = self.position + forward * self.radius
        shot = Shot(shot_position.x, shot_position.y)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
    
            

    