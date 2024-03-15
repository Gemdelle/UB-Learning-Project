import pygame

from sys import exit

from core.screens import Screens
from ui.components.character_selection_box import CharacterSelectionID
from ui.components.pet_selection_box import PetSelectionID
from ui.screens.main_screen import render_main
from ui.screens.pet_dialog_text_phase_1 import render_pet_dialog_text_phase_1
from ui.screens.pet_dialog_text_phase_2 import render_pet_dialog_text_phase_2
from ui.screens.pet_dialog_text_phase_3 import render_pet_dialog_text_phase_3
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
clock = pygame.time.Clock()
game_active = True
running = True

screen_selected = Screens.PET_INTRO_DIALOG_TEXT_PHASE_1

button_font_manager = pygame.font.Font('font/Alkhemikal.ttf', 25)

character_selected_id = None
character_name = None

pet_selected_id = None
pet_name = None

def listen_to_key_binding():
    global event, running, screen_selected
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

def go_to_select_character():
    global screen_selected
    screen_selected = Screens.SELECT_CHARACTER
    print("Navigate to:", screen_selected)

def select_character(character_selection_id):
    global character_selected_id
    character_selected_id = character_selection_id
    print("Personaje seleccionado:", character_selection_id)
def select_character_name(character_name_selected):
    global character_name
    character_name = character_name_selected
    print("Nombre seleccionado:", character_name_selected)

def can_continue_from_character_selection():
    global character_selected_id, character_name
    return character_selected_id != None and character_name != None

def go_to_select_pet():
    global screen_selected
    screen_selected = Screens.SELECT_PET
    print("Navigate to:", screen_selected)

def select_pet(pet_selection_id):
    global pet_selected_id
    pet_selected_id = pet_selection_id
    print("Pet seleccionado:", pet_selection_id)

def can_continue_from_pet_selection():
    global pet_selected_id
    return pet_selected_id != None

def go_to_pet_dialog_text_phase_1():
    global screen_selected
    screen_selected = Screens.PET_INTRO_DIALOG_TEXT_PHASE_1
    print("Navigate to:", screen_selected)

def select_pet_name(pet_name_selected):
    global pet_name
    pet_name = pet_name_selected
    print("Nombre del pet seleccionado:", pet_name_selected)

def go_to_select_regions():
    global screen_selected
    screen_selected = Screens.REGIONS
    print("Navigate to:", screen_selected)
def go_to_dialog_text_phase_2():
    global screen_selected
    screen_selected = Screens.PET_INTRO_DIALOG_TEXT_PHASE_2
    print("Navigate to:", screen_selected)

def go_to_dialog_text_phase_3():
    global screen_selected
    screen_selected = Screens.PET_INTRO_DIALOG_TEXT_PHASE_3
    print("Navigate to:", screen_selected)

while running:
    listen_to_key_binding()
    if game_active:
        if screen_selected == Screens.SPLASH:
            render_splash(screen)
        elif screen_selected == Screens.MAIN:
            render_main(screen, go_to_select_character)
        elif screen_selected == Screens.SELECT_LANGUAGE:
            render_select_language(screen)
        elif screen_selected == Screens.SELECT_CHARACTER:
            render_select_character(screen, select_character, select_character_name, can_continue_from_character_selection, go_to_select_pet)
        elif screen_selected == Screens.SELECT_PET:
            render_select_pet(screen, select_pet, can_continue_from_pet_selection, go_to_pet_dialog_text_phase_1)
        elif screen_selected == Screens.PET_INTRO_DIALOG_TEXT_PHASE_1:
            # render_pet_dialog_text_phase_1(screen, "Gemy", CharacterSelectionID.PEPE, PetSelectionID.ORKY, go_to_dialog_text_phase_2)
            render_pet_dialog_text_phase_1(screen, "Gemy", CharacterSelectionID.PEPE, PetSelectionID.ORKY, go_to_dialog_text_phase_2)
        elif screen_selected == Screens.PET_INTRO_DIALOG_TEXT_PHASE_2:
            # render_pet_dialog_text_phase_2(screen, "Gemy", CharacterSelectionID.PEPE, PetSelectionID.ORKY, go_to_dialog_text_phase_3)
            render_pet_dialog_text_phase_2(screen, CharacterSelectionID.PEPE, PetSelectionID.ORKY, go_to_dialog_text_phase_3)
        elif screen_selected == Screens.PET_INTRO_DIALOG_TEXT_PHASE_3:
            # render_pet_dialog_text_phase_3(screen, "Gemy", CharacterSelectionID.PEPE, PetSelectionID.ORKY, go_to_dialog_text_phase_3)
            render_pet_dialog_text_phase_3(screen, "Ornelyno", CharacterSelectionID.PEPE, PetSelectionID.ORKY, go_to_select_regions)
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

    pygame.display.update()
    clock.tick(60)