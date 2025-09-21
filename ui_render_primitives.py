import pygame
from colors import *
from geometry import Rectangle

k_rect_thickness = 2

def draw_rectangle_outline(surface, rect: Rectangle, color : tuple[int, int, int], thickness=k_rect_thickness):
    assert rect is not None
    py_rect = pygame.Rect(rect.left, rect.top, rect.width, rect.height)
    pygame.draw.rect(surface, color, py_rect, thickness)

def draw_rectangle(surface, rect: Rectangle, color : tuple[int, int, int]):
    assert rect is not None
    py_rect = pygame.Rect(rect.left, rect.top, rect.width, rect.height)
    pygame.draw.rect(surface, color, py_rect)

def draw_juicy_rectangle(surface, rect: Rectangle, color : tuple[int, int, int]):
    assert rect is not None

    outer_rect = rect
    inner_rect = rect.as_shrunk(0.9)
    # inner_rect = rect.as_shrunk_square(0.9)

    dimming = 0.7
    outer_color = (color[0] * dimming, color[1] * dimming, color[2] * dimming)
    inner_color = color

    draw_rectangle(surface, outer_rect, outer_color)
    draw_rectangle(surface, inner_rect, inner_color)

# So far only tried with a single character
def draw_text(surface: pygame.Surface, screen_section: Rectangle, text: str, text_color: tuple[int, int, int]):
    assert screen_section is not None
    py_screen_section = pygame.Rect(screen_section.left, screen_section.top, screen_section.width, screen_section.height)

    font = pygame.font.SysFont('arial', int(screen_section.width / len(text)))

    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=py_screen_section.center)
    surface.blit(text_surface, text_rect)