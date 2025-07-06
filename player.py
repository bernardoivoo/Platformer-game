from pgzero.actor import Actor
from pygame import Rect
from config import GRAVITY, JUMP_STRENGTH

class Player:
    def __init__(self):
        self.actor = Actor("player_idle1", (100, 500))
        self.vy = 0
        self.on_ground = False
        self.anim_index = 0
        self.anim_timer = 0

    def update(self, platforms):
        self.vy += GRAVITY
        self.actor.y += self.vy
        self.on_ground = False

        for p in platforms:
            if self.collides(p):
                if self.vy > 0:
                    self.actor.y = p.y - self.actor.height / 2
                    self.vy = 0
                    self.on_ground = True

        keys = keyboard
        if keys.left:
            self.actor.x -= 3
            self.animate("left")
        elif keys.right:
            self.actor.x += 3
            self.animate("right")
        else:
            self.animate("idle")

        if keys.space and self.on_ground:
            self.vy = JUMP_STRENGTH

    def animate(self, state):
        self.anim_timer += 1
        if self.anim_timer > 5:
            self.anim_index = (self.anim_index + 1) % 4
            self.actor.image = f"player_{state}{self.anim_index+1}"
            self.anim_timer = 0

    def draw(self):
        self.actor.draw()

    def collides(self, platform):
        return Rect(self.actor.left, self.actor.top, self.actor.width, self.actor.height).colliderect(platform)
