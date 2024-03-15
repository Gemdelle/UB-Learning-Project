import pygame

from ui.components.character_selection_box import CharacterSelectionID, CharacterSelectionBox
from ui.components.dialog_text import DialogText
from ui.components.frame import Frame
from ui.components.pet_selection_box import PetSelectionID, PetSelectionBox

# Text to be displayed
text_to_type_phase_3_1 = "{name}, that is weird but very sweet, thank you. From now on,"
text_to_type_phase_3_2 = "remember to print every time you want to answer to someone."

typed_text_phase_3_1 = ""
typed_text_phase_3_2 = ""

# Typing speed (characters per second)
typing_speed = 10

def render_pet_dialog_text_phase_3(screen, pet_name, character_selected_id, pet_selected_id, go_to_select_regions):
    global typed_text_phase_3_1, typed_text_phase_3_2, text_to_type_phase_3_1, text_to_type_phase_3_2
    text_to_type_phase_3_1 = text_to_type_phase_3_1.replace("{name}", pet_name)
    character_images = {
        CharacterSelectionID.PEPE: pygame.image.load('assets/character1.jpg'),
        CharacterSelectionID.NORBERT: pygame.image.load('assets/character2.jpg'),
        CharacterSelectionID.DORY: pygame.image.load('assets/character3.jpg')
    }
    pet_images = {
        PetSelectionID.ORKY: pygame.image.load('assets/pet1.jpg'),
        PetSelectionID.TOBI: pygame.image.load('assets/pet2.jpg'),
        PetSelectionID.HUNNY: pygame.image.load('assets/pet3.jpg')
    }
    screen.fill((255, 255, 255))
    frame = Frame(screen, 50, 50, 1640, 940, (100, 100, 100))
    dialog_frame = Frame(screen, 50, 600, 1640, 400, (100, 100, 100))
    frame.add_element(dialog_frame)
    pet_avatar = PetSelectionBox(screen, 1400, 700, 200, 200, pet_images[pet_selected_id], pet_selected_id)
    frame.add_element(pet_avatar)
    character_avatar = CharacterSelectionBox(screen, 150, 700, 200, 200, character_images[character_selected_id],character_selected_id)
    frame.add_element(character_avatar)


    dialog_text_phase_3_1 = DialogText(screen, 400, 700, 500, 300, typed_text_phase_3_1)
    frame.add_element(dialog_text_phase_3_1)
    dialog_text_phase_3_2 = DialogText(screen, 400, 750, 500, 300, typed_text_phase_3_2)
    frame.add_element(dialog_text_phase_3_2)

    # Delay for the typing speed
    pygame.time.delay(int(1000 / typing_speed))
    # Add a character to the typed text
    if text_to_type_phase_3_1:
        typed_text_phase_3_1 += text_to_type_phase_3_1[0]
        text_to_type_phase_3_1 = text_to_type_phase_3_1[1:]

    if not text_to_type_phase_3_1:
        if text_to_type_phase_3_2:
            typed_text_phase_3_2 += text_to_type_phase_3_2[0]
            text_to_type_phase_3_2 = text_to_type_phase_3_2[1:]

        if not text_to_type_phase_3_2:
            pygame.time.delay(3000)
            go_to_select_regions()

    frame.draw()



