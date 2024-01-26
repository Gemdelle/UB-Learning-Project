import pygame

from sys import exit  # to exit the game without having issues with the True loop
from random import randint
import math

from core.screens import Screens
from ui.screens.main_screen import render_main
from ui.screens.select_character import render_select_character
from ui.screens.select_language import render_select_language
from ui.screens.select_pet import render_select_pet
from ui.screens.select_regions import render_select_regions
from ui.screens.splash import render_splash
from ui.screens.training_regions import render_training_regions
from ui.screens.water_region.water_region import render_water_region
from ui.screens.water_region.water_region_lily import render_water_region_lily
from ui.screens.water_region.water_training_region import render_water_training_region

# Setup
pygame.init()
PRODUCT_HEIGHT = 28
MARGIN = 130
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
MIN_STOCK_TO_UPDATE = 100
screen = pygame.display.set_mode((SCREEN_WIDTH,
                                  SCREEN_HEIGHT))
pygame.display.set_caption('PyEvolve')
clock = pygame.time.Clock()  # clock object to handle frame rate
game_active = True
running = True

screen_selected = Screens.SPLASH

button_font_manager = pygame.font.Font('font/Alkhemikal.ttf', 25)
def listen_to_key_binding():
    global event, running, screen_selected
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

while running:  # The game will be continuously updated.
    listen_to_key_binding()
    if game_active:
        if screen_selected == Screens.SPLASH:
            render_splash(screen)
        elif screen_selected == Screens.MAIN:
            render_main(screen)
        elif screen_selected == Screens.SELECT_LANGUAGE:
            render_select_language(screen)
        elif screen_selected == Screens.SELECT_CHARACTER:
            render_select_character(screen)
        elif screen_selected == Screens.SELECT_PET:
            render_select_pet(screen)
        elif screen_selected == Screens.REGIONS:
            render_select_regions(screen)
        elif screen_selected == Screens.TRAINING_REGIONS:
            render_training_regions(screen)
        elif screen_selected == Screens.WATER_REGION:
            render_water_region(screen)
        elif screen_selected == Screens.WATER_TRAINING_REGION:
            render_water_training_region(screen)
        elif screen_selected == Screens.WATER_REGION_LILY:
            render_water_region_lily(screen)
        else:
            print("HOLA")

    pygame.display.update()  # update the screen
    clock.tick(60)  # while True runs 60 times per second