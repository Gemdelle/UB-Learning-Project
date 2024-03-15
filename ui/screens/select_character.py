import pygame

from ui.components.button import Button
from ui.components.character_selection_box import CharacterSelectionBox, CharacterSelectionID, CharacterSelectionInput
from ui.components.frame import Frame

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (150, 150, 150)

margen = 20
ancho_personaje = 200
alto_personaje = 200
columnas = 3

personaje_seleccionado = None
is_writing_name = False

text_input = ""

text_surface_rect = None

def listen_to_key_binding(select_character, select_character_name):
    global personaje_seleccionado, text_input, is_writing_name, text_surface_rect
    characterSelectionIDs = [
        CharacterSelectionID.PEPE,
        CharacterSelectionID.NORBERT,
        CharacterSelectionID.DORY,
    ]
    character_images = [
        pygame.transform.scale(pygame.image.load('assets/character1.jpg').convert_alpha(), (200, 200)),
        pygame.transform.scale(pygame.image.load('assets/character2.jpg').convert_alpha(), (200, 200)),
        pygame.transform.scale(pygame.image.load('assets/character3.jpg').convert_alpha(), (200, 200)),
    ]
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for i, imagen_personaje in enumerate(character_images):
                columna = i % columnas
                fila = i // columnas
                x = margen + (margen + ancho_personaje) * columna
                y = margen + (margen + alto_personaje) * fila
                rectangulo_personaje = pygame.Rect(500 + x, 200 + y, ancho_personaje, alto_personaje)
                if rectangulo_personaje.collidepoint(mouse_x, mouse_y):
                    personaje_seleccionado = i
                    select_character(characterSelectionIDs[i])
            if text_surface_rect and text_surface_rect.collidepoint(mouse_x, mouse_y):
                is_writing_name = True

        elif event.type == pygame.KEYDOWN and is_writing_name != False:
            if event.key == pygame.K_RETURN:
                print("Entered text:", text_input)
                is_writing_name = False
                if (len(text_input) > 4):
                    select_character_name(text_input)
            elif event.key == pygame.K_BACKSPACE:
                text_input = text_input[:-1]
            else:
                text_input += event.unicode
                print(text_input)

def render_select_character(screen, select_character, select_character_name, can_continue_from_character_selection, execute_continue_from_select_character):
    global text_surface_rect, text_input
    listen_to_key_binding(select_character, select_character_name)
    character_images = [
        (pygame.image.load('assets/character1.jpg'), CharacterSelectionID.PEPE),
        (pygame.image.load('assets/character2.jpg'), CharacterSelectionID.NORBERT),
        (pygame.image.load('assets/character3.jpg'), CharacterSelectionID.DORY),
    ]
    filas = (len(character_images) // columnas) + (1 if len(character_images) % columnas != 0 else 0)
    frame = Frame(screen, 400, 100, 800, 800, (100, 100, 100))
    for i, imagen_personaje in enumerate(character_images):
        columna = i % columnas
        fila = i // columnas
        x = margen + (margen + ancho_personaje) * columna
        y = margen + (margen + alto_personaje) * fila
        character_selection_box = CharacterSelectionBox(screen, 500 + x, 200 + y, 200, 200, imagen_personaje[0], imagen_personaje[1])
        frame.add_element(character_selection_box)

    text_surface = CharacterSelectionInput(screen, 600, 600, 400, 50, text_input)
    text_surface_rect = text_surface.rect
    frame.add_element(text_surface)
    if (can_continue_from_character_selection()):
        play_button = Button(screen, 720, 720, 200, 80, "Continue", (225, 224, 204), 'White', lambda: execute_continue_from_select_character())
        frame.add_element(play_button)
        play_button.check_click()

    frame.draw()

    for i, imagen_personaje in enumerate(character_images):
        columna = i % columnas
        fila = i // columnas
        x = margen + (margen + ancho_personaje) * columna
        y = margen + (margen + alto_personaje) * fila
        pygame.draw.rect(screen, NEGRO if personaje_seleccionado == i else GRIS,
                         (500+x, 200+y, ancho_personaje, alto_personaje), 2)
