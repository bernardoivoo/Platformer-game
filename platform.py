from pygame import Rect

class Platform:
    def __init__(self, x, y, width=100, height=20):
        self.rect = Rect(x, y, width, height)

    def draw(self, screen):
        screen.draw.filled_rect(self.rect, (100, 100, 100))
