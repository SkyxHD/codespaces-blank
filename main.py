import sys
import pygame

pygame.init()

GAME_ACTIVE = True
position = (0, 0)

black = (0, 0, 0)
SPRITE_SIZE = (50, 50)
sprite_size = (0, 0)

screen = pygame.display.set_mode((640, 480))

sprite = pygame.image.load('test.bmp').convert_alpha()
sprite = pygame.transform.scale(sprite, SPRITE_SIZE)
screen.blit(sprite, (100, 100))
pygame.display.flip()

while GAME_ACTIVE is True:
    for eventlist in pygame.event.get():
        if eventlist.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            screen.fill(black)
            screen.blit(sprite, (position[0] - SPRITE_SIZE[0]/2, position[1] - SPRITE_SIZE[1]/2))
            pygame.display.flip()