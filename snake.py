import pygame
import tail
import player
import food

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = player.Player(SCREEN_WIDTH, SCREEN_HEIGHT)
snake_food = food.Food(SCREEN_WIDTH, SCREEN_HEIGHT)

tail_parts = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(snake_food)

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

    if player.tail > 0:
        new_tail = tail.Tail(player.rect.left, player.rect.top)
        tail_parts.add(new_tail)
        all_sprites.add(new_tail)

    if len(tail_parts) > player.tail:
        tail_parts.sprites()[0].kill()

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    screen.fill((0, 0, 0))

    if player.is_band_collision():
        running = False

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, tail_parts):
        player.kill()
        tail_parts.kill()
        running = False

    if pygame.sprite.spritecollideany(player, [snake_food]):
        snake_food.kill()
        snake_food = food.Food(SCREEN_WIDTH, SCREEN_HEIGHT)
        all_sprites.add(snake_food)
        player.tail += 1

    pygame.display.flip()

    clock.tick(30)
