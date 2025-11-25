import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Space Invaders")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_SPEED = 5

# Enemy
ENEMY_WIDTH = 40
ENEMY_HEIGHT = 40
ENEMY_SPEED = 1
ENEMY_DROP_SPEED = 10

# Bullet
BULLET_WIDTH = 5
BULLET_HEIGHT = 15
BULLET_SPEED = 7

# Fonts
FONT = pygame.font.Font(None, 36)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([PLAYER_WIDTH, PLAYER_HEIGHT])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed_x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.speed_x += PLAYER_SPEED
        self.rect.x += self.speed_x
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def shoot(self):
        bullet = PlayerBullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        player_bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([ENEMY_WIDTH, ENEMY_HEIGHT])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = ENEMY_SPEED

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed_x *= -1
            self.rect.y += ENEMY_DROP_SPEED

class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([BULLET_WIDTH, BULLET_HEIGHT])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

    def update(self):
        self.rect.y -= BULLET_SPEED
        if self.rect.bottom < 0:
            self.kill()

# Game setup
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player_bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

def spawn_enemies(rows, cols):
    for row in range(rows):
        for col in range(cols):
            enemy = Enemy(50 + col * 60, 50 + row * 60)
            all_sprites.add(enemy)
            enemies.add(enemy)

spawn_enemies(5, 10) # 5 rows, 10 columns of enemies

score = 0
game_over = False

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    if not game_over:
        all_sprites.update()

        # Check for bullet-enemy collisions
        hits = pygame.sprite.groupcollide(enemies, player_bullets, True, True)
        for hit in hits:
            score += 10 # Increase score for each hit

        # Check if all enemies are defeated
        if not enemies:
            game_over = True
            print("YOU WIN!")

        # Check for enemy reaching player's level (or bottom of screen)
        for enemy in enemies:
            if enemy.rect.bottom >= player.rect.top:
                game_over = True
                print("GAME OVER!")

    # Drawing
    SCREEN.fill((0, 0, 0)) # Black background
    all_sprites.draw(SCREEN)

    # Display score
    score_text = FONT.render(f"Score: {score}", True, WHITE)
    SCREEN.blit(score_text, (10, 10))

    if game_over:
        if not enemies:
            game_over_text = FONT.render("YOU WIN!", True, GREEN)
        else:
            game_over_text = FONT.render("GAME OVER!", True, RED)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        SCREEN.blit(game_over_text, text_rect)

    pygame.display.flip()
    clock.tick(60) # 60 FPS

pygame.quit()