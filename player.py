import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT
)

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super(Player, self).__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((255, 255, 255))
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rect = self.surf.get_rect(center=(
            (screen_width-self.surf.get_width())/2,
            (screen_height-self.surf.get_height())/2
        ))
        self.speed = 10
        self.tail = 0
        self.last_pressed_direction_key = K_RIGHT

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.last_pressed_direction_key = K_UP
        elif pressed_keys[K_DOWN]:
            self.last_pressed_direction_key = K_DOWN
        elif pressed_keys[K_LEFT]:
            self.last_pressed_direction_key = K_LEFT
        elif pressed_keys[K_RIGHT]:
            self.last_pressed_direction_key = K_RIGHT

        if self.last_pressed_direction_key == K_UP:
            self.rect.move_ip(0, -self.speed)
        elif self.last_pressed_direction_key == K_DOWN:
            self.rect.move_ip(0, self.speed)
        elif self.last_pressed_direction_key == K_LEFT:
            self.rect.move_ip(-self.speed, 0)
        elif self.last_pressed_direction_key == K_RIGHT:
            self.rect.move_ip(self.speed, 0)

    def is_band_collision(self):
        return self.rect.left < 0 or \
            self.rect.right > self.screen_width or \
            self.rect.top < 0 or \
            self.rect.bottom > self.screen_height
