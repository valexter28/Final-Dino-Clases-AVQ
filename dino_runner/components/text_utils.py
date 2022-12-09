import pygame

from dino_runner.utils.constants import (FONT_STYLE, BLACK_COLOR)

def get_score_element(points):
    front = pygame.font.font(FONT_STYLE, 20)

    text = font.render('points:' + str(points), True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (1000, 50)
    return (text, text_rect)