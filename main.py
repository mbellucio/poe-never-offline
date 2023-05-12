import time
import pywinauto
from pywinauto import timings
import pygame.mixer

# Set the interval for mouse clicks (in seconds)
click_interval = 590

# Set the name of the game window
window_name = "Path of Exile"

pygame.mixer.init()
sound = pygame.mixer.Sound("uwu.mp3")
# Function to keep the game active


def keep_game_active():
    while True:
        try:
            # Find the game window
            app = pywinauto.Application().connect(title=window_name)
            window = app[window_name]
        except Exception:
            print(f"Could not find window with name {window_name}")
            break

        # Bring the game window to the foreground (if it's not already)
        if not timings.wait_until_passes(5 * 1000, 0.5, window.is_active, True):
            window.set_focus()

        # Simulate a mouse click to keep the game active
        window.click_input()

        # Minimize the game window
        window.minimize()

        # Wait for the click interval
        time.sleep(click_interval)
        sound.play()
        time.sleep(2)


if __name__ == '__main__':
    # Call the function to keep the game active
    keep_game_active()
