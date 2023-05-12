import time
import pywinauto
from pywinauto import timings
import pygame.mixer

click_interval = 480

window_name = "Path of Exile"

pygame.mixer.init()
sound = pygame.mixer.Sound("uwu.mp3")

def keep_game_active():
    while True:
        try:
            app = pywinauto.Application().connect(title=window_name)
            window = app[window_name]
        except Exception:
            print(f"Could not find window with name {window_name}")
            break

        if not timings.wait_until_passes(5 * 1000, 0.5, window.is_active, True):
            window.set_focus()

        window.click_input()

        window.minimize()

        time.sleep(click_interval)
        sound.play()
        time.sleep(2)

if __name__ == '__main__':
    keep_game_active()
