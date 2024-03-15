import pygame

from ui.components.button import Button
from ui.components.frame import Frame


def render_main(screen, execute_play):
    screen.fill((255, 255, 255))
    frame = Frame(screen, 600, 400, 400, 400, (100, 100, 100))
    play_button = Button(screen,720, 480, 200, 80, "PLAY", (225, 224, 204), 'White', lambda: execute_play())
    #progress_button = Button(screen,860, 560, 200, 80, "PROGRESS", (225, 224, 204), 'White', lambda: print("Progress Button pressed"))
    frame.add_element(play_button)
    #frame.add_element(progress_button)
    frame.draw()
    play_button.check_click()
    #progress_button.check_click()
