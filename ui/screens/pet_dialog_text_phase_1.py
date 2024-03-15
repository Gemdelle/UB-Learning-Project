import pygame

from ui.components.character_selection_box import CharacterSelectionID, CharacterSelectionBox
from ui.components.dialog_text import DialogText
from ui.components.frame import Frame
from ui.components.pet_selection_box import PetSelectionID, PetSelectionBox

# Text to be displayed
text_to_type_phase_1_1 = "Hello, {name}. Thank you for choosing me. To communicate with"
text_to_type_phase_1_2 = "people, you will need to print messages. Let's start by giving"
text_to_type_phase_1_3 = "me a name."

typed_text_phase_1_1 = ""
typed_text_phase_1_2 = ""
typed_text_phase_1_3 = ""

# Typing speed (characters per second)
typing_speed = 10

def render_pet_dialog_text_phase_1(screen, character_name, character_selected_id, pet_selected_id, go_to_dialog_text_phase_2):
    global typed_text_phase_1_1, typed_text_phase_1_2, typed_text_phase_1_3, text_to_type_phase_1_1, text_to_type_phase_1_2, text_to_type_phase_1_3
    text_to_type_phase_1_1 = text_to_type_phase_1_1.replace("{name}", character_name)
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

    dialog_text_phase_1_1 = DialogText(screen, 400, 700, 500, 300, typed_text_phase_1_1)
    frame.add_element(dialog_text_phase_1_1)
    dialog_text_phase_1_2 = DialogText(screen, 400, 750, 500, 300, typed_text_phase_1_2)
    frame.add_element(dialog_text_phase_1_2)
    dialog_text_phase_1_3 = DialogText(screen, 400, 800, 500, 300, typed_text_phase_1_3)
    frame.add_element(dialog_text_phase_1_3)
    # Delay for the typing speed
    pygame.time.delay(int(1000 / typing_speed))

    if text_to_type_phase_1_1:
        typed_text_phase_1_1 += text_to_type_phase_1_1[0]
        text_to_type_phase_1_1 = text_to_type_phase_1_1[1:]

    if not text_to_type_phase_1_1:
        if text_to_type_phase_1_2:
            typed_text_phase_1_2 += text_to_type_phase_1_2[0]
            text_to_type_phase_1_2 = text_to_type_phase_1_2[1:]

        if not text_to_type_phase_1_2:
            if text_to_type_phase_1_3:
                typed_text_phase_1_3 += text_to_type_phase_1_3[0]
                text_to_type_phase_1_3 = text_to_type_phase_1_3[1:]
            if not text_to_type_phase_1_3:
                # Optional: Wait for a few seconds after typing is complete
                pygame.time.delay(3000)
                go_to_dialog_text_phase_2()
    frame.draw()



