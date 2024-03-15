import pygame

from ui.components.button import Button
from ui.components.frame import Frame
from ui.components.pet_selection_box import PetSelectionID, PetSelectionBox

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (150, 150, 150)

margen = 20
ancho_personaje = 200
alto_personaje = 200
columnas = 3

pet_seleccionado = None

def listen_to_key_binding(select_pet):
    global pet_seleccionado
    petSelectionIDs = [
        PetSelectionID.ORKY,
        PetSelectionID.TOBI,
        PetSelectionID.HUNNY,
    ]
    pet_images = [
        pygame.transform.scale(pygame.image.load('assets/pet1.jpg').convert_alpha(), (200, 200)),
        pygame.transform.scale(pygame.image.load('assets/pet2.jpg').convert_alpha(), (200, 200)),
        pygame.transform.scale(pygame.image.load('assets/pet3.jpg').convert_alpha(), (200, 200)),
    ]
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for i, imagen_personaje in enumerate(pet_images):
                columna = i % columnas
                fila = i // columnas
                x = margen + (margen + ancho_personaje) * columna
                y = margen + (margen + alto_personaje) * fila
                rectangulo_personaje = pygame.Rect(500 + x, 200 + y, ancho_personaje, alto_personaje)
                if rectangulo_personaje.collidepoint(mouse_x, mouse_y):
                    pet_seleccionado = i
                    select_pet(petSelectionIDs[i])
def render_select_pet(screen, select_pet, can_continue_from_pet_selection, execute_continue_from_select_pet):
    listen_to_key_binding(select_pet)
    pet_images = [
        (pygame.image.load('assets/pet1.jpg'), PetSelectionID.ORKY),
        (pygame.image.load('assets/pet2.jpg'), PetSelectionID.TOBI),
        (pygame.image.load('assets/pet3.jpg'), PetSelectionID.HUNNY),
    ]
    filas = (len(pet_images) // columnas) + (1 if len(pet_images) % columnas != 0 else 0)
    frame = Frame(screen, 400, 100, 800, 800, (100, 100, 100))
    for i, imagen_pet in enumerate(pet_images):
        columna = i % columnas
        fila = i // columnas
        x = margen + (margen + ancho_personaje) * columna
        y = margen + (margen + alto_personaje) * fila
        pet_selection_box = PetSelectionBox(screen, 500 + x, 200 + y, 200, 200, imagen_pet[0], imagen_pet[1])
        frame.add_element(pet_selection_box)

    if (can_continue_from_pet_selection()):
        play_button = Button(screen, 720, 480, 200, 80, "Continue", (225, 224, 204), 'White', lambda: execute_continue_from_select_pet())
        frame.add_element(play_button)
        play_button.check_click()

    frame.draw()

    for i, imagen_pet in enumerate(pet_images):
        columna = i % columnas
        fila = i // columnas
        x = margen + (margen + ancho_personaje) * columna
        y = margen + (margen + alto_personaje) * fila
        pygame.draw.rect(screen, NEGRO if pet_seleccionado == i else GRIS,
                         (500+x, 200+y, ancho_personaje, alto_personaje), 2)