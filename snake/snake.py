import pygame
from snake.tail import Tail
from snake.player import Player
from snake.food import Food

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)


class Snake(object):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.__screen_width = screen_width
        self.__screen_height = screen_height
        self.__font_name = pygame.font.match_font('arial')

    def play(self):
        pygame.init()

        clock = pygame.time.Clock()

        screen = pygame.display.set_mode((self.__screen_width, self.__screen_height))

        player = Player(self.__screen_width, self.__screen_height)
        food = Food(self.__screen_width, self.__screen_height)

        tail_parts = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)
        all_sprites.add(food)

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                elif event.type == QUIT:
                    running = False

            if player.tail > 0:
                new_tail = Tail(player.rect.left, player.rect.top)
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
                tail_parts.empty()
                running = False

            if pygame.sprite.spritecollideany(player, [food]):
                food.kill()
                food = Food(self.__screen_width, self.__screen_height)
                all_sprites.add(food)
                player.tail += 1

            self.__update_score(player.tail, screen)
            pygame.display.flip()

            clock.tick(30)

    def __draw_text(self, surf, text, size, x, y):
        font = pygame.font.Font(self.__font_name, size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    def __update_score(self, score, screen):
        self.__draw_text(screen, str(score), 18, self.__screen_width / 2, 10)
