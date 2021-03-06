import pygame
import random


class Food(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super(Food, self).__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((126, 126, 126))
        self.rect = self.surf.get_rect(topleft=(
            round(random.randint(0, screen_width - 10), -1),
            round(random.randint(0, screen_height - 10), -1)
        ))
