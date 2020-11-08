import pygame


class Tail(pygame.sprite.Sprite):
    def __init__(self, left, top):
        super(Tail, self).__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(topleft=(left, top))
