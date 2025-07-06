menu_active = True
buttons = [
    {"label": "Start Game", "x": 300, "y": 200},
    {"label": "Toggle Sound", "x": 300, "y": 260},
    {"label": "Exit", "x": 300, "y": 320}
]

def draw_menu(screen):
    screen.draw.text("Platformer Game", center=(400, 100), fontsize=60, color="white")
    for b in buttons:
        screen.draw.textbox(b["label"], pygame.Rect(b["x"], b["y"], 200, 40), color="black", background="white")

def handle_click(pos):
    global menu_active
    for i, b in enumerate(buttons):
        r = pygame.Rect(b["x"], b["y"], 200, 40)
        if r.collidepoint(pos):
            if i == 0:
                menu_active = False
            elif i == 1:
                import sound
                sound.toggle_music()
            elif i == 2:
                exit()
