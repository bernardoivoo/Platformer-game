import pgzrun
from player import Player
from enemy import Enemy
from platform import Platform
import menu
import sound

from config import WIDTH, HEIGHT

TITLE = "Platformer Game"

player = Player()
platforms = [Platform(100, 550), Platform(300, 400), Platform(500, 300)]
enemies = [Enemy(400, 500), Enemy(600, 300)]

def draw():
    screen.clear()
    if menu.menu_active:
        menu.draw_menu(screen)
    else:
        for p in platforms:
            p.draw(screen)
        for e in enemies:
            e.draw()
        player.draw()

def update():
    if not menu.menu_active:
        player.update([p.rect for p in platforms])
        for e in enemies:
            e.update()
            if e.collides_with(player):
                print("Você perdeu!")  # Pode reiniciar o jogo

def on_mouse_down(pos):
    if menu.menu_active:
        menu.handle_click(pos)

sound.toggle_music()
pgzrun.go()
