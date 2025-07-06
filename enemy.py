from pgzero.actor import Actor
from pygame import Rect
import random

class Enemy:
    def __init__(self, x, y):
        self.actor = Actor("enemy_idle1", (x, y))
        self.direction = random.choice([-1, 1])
        self.speed = 2
        self.anim_index = 0
        self.timer = 0

    def update(self):
        self.actor.x += self.speed * self.direction
        if self.actor.left < 0 or self.actor.right > 800:
            self.direction *= -1
        self.animate()

    def animate(self):
        self.timer += 1
        if self.timer > 6:
            self.anim_index = (self.anim_index + 1) % 2
            self.actor.image = f"enemy_idle{self.anim_index+1}"
            self.timer = 0

    def draw(self):
        self.actor.draw()

    def collides_with(self, player):
        return self.actor.colliderect(player.actor)
