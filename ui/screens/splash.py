import pygame
import imageio

start_scale = 1
target_scale = 2
total_duration = 3  # Total duration of the transition in seconds
frames_per_second = 60

# Calculate change in scale per frame
scale_change_per_frame = (target_scale - start_scale) / (total_duration * frames_per_second)

current_scale = start_scale

def draw_button(x, y, width, height, text, button_color, text_color,screen):
    pygame.draw.rect(screen, button_color, (x, y, width, height))

    text_surface = pygame.font.Font('font/Alkhemikal.ttf', 25).render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))

    screen.blit(text_surface, text_rect)
    return text_rect
def render_splash(screen):
    global current_scale

    background_image = pygame.image.load("assets/splash_background.jpeg").convert()
    background_rect = background_image.get_rect()

    current_scale += scale_change_per_frame

    current_scale = min(current_scale, target_scale)

    new_width = int(background_rect.width * current_scale)
    new_height = int(background_rect.height * current_scale)

    scaled_background = pygame.transform.scale(background_image, (new_width, new_height))
    scaled_rect = scaled_background.get_rect(center=screen.get_rect().center)

    ############################
    screen.fill((255, 255, 255))
    screen.blit(scaled_background, scaled_rect)


    #draw_button(800, 500, 350, 50, "SPLASH", (225, 224, 204), 'White', screen)