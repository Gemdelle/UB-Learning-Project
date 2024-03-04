import pygame

class Frame:
    def __init__(self, screen, x, y, width, height, border_color):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.elements = []
        self.border_color = border_color

    def add_element(self, element):
        self.elements.append(element)

    def draw(self):
        pygame.draw.rect(self.screen, self.border_color, self.rect, border_radius=10)
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect.inflate(-6, -6), border_radius=6)
        for element in self.elements:
            element.draw()

class Button:
    def __init__(self, screen, x, y, width, height, text, text_color, color, action):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.color = color
        self.action = action

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 2)

        text_surface = pygame.font.Font('font/Alkhemikal.ttf', 25).render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)

        self.screen.blit(text_surface, text_rect)

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.action()



def draw_button(x, y, width, height, text, button_color, text_color, screen):
    pygame.draw.rect(screen, button_color, (x, y, width, height))

    text_surface = pygame.font.Font('font/Alkhemikal.ttf', 25).render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))

    #screen.blit(text_surface, text_rect)
    return text_rect
def render_main(screen):
    screen.fill((255, 255, 255))
    frame = Frame(screen, 600, 400, 400, 400, (100, 100, 100))
    play_button = Button(screen,860, 460, 200, 80, "PLAY", (225, 224, 204), 'White', lambda: print("Play Button pressed"))
    progress_button = Button(screen,860, 560, 200, 80, "PROGRESS", (225, 224, 204), 'White', lambda: print("Progress Button pressed"))
    frame.add_element(play_button)
    frame.add_element(progress_button)
    frame.draw()
