music_on = True

def toggle_music():
    global music_on
    if music_on:
        music.stop()
        music_on = False
    else:
        music.play("background")
        music.set_volume(0.3)
        music_on = True
