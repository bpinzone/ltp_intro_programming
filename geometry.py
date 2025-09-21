import pygame
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Rectangle:
    """Top left is 0, 0"""
    def __init__(self, left: int, top: int, width: int, height: int):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def get_left_half(self):
        return Rectangle(self.left, self.top, self.width / 2, self.height)

    def get_right_half(self):
        return Rectangle(self.left + self.width / 2, self.top, self.width / 2, self.height)

    def get_center(self):
        return Point(self.left + self.width / 2, self.top + self.height / 2)

    def as_square(self):
        size = min(self.width, self.height)
        center = self.get_center()
        return Rectangle(center.x - size / 2, center.y - size / 2, size, size)

    def as_shrunk_square(self, size_keep_percent: float):
        square = self.as_square()
        shrunk_square_size = square.width * size_keep_percent
        center = square.get_center()
        return Rectangle(center.x - shrunk_square_size / 2, center.y - shrunk_square_size / 2, shrunk_square_size, shrunk_square_size)

    def as_shrunk(self, size_keep_percent: float):
        shrunk_width = self.width * size_keep_percent
        shrunk_height = self.height * size_keep_percent
        shrunk_left = self.left + ((self.width - shrunk_width)/2)
        shrunk_top = self.top + ((self.height - shrunk_height)/2)
        return Rectangle(shrunk_left, shrunk_top, shrunk_width, shrunk_height)

    def print(self):
        print(f"Rectangle(left={self.left}, top={self.top}, width={self.width}, height={self.height})")
    
    def as_pygame_rect(self):
        return pygame.Rect(self.left, self.top, self.width, self.height)