import pygame
import os


pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pokémon Game")
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Couleurs
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
DARK_GRAY = (50, 50, 50)
BLUE = (0, 122, 255)

# Classe pour le menu
class Menu:
    def __init__(self):
        self.options = [
            "Launch the game",
            "Add a Pokémon",
            "Quit"
        ]
        self.button_rects = []

    def display_menu(self):
        print("\nWelcome to Pokémon Game!")
        print("\n=== Menu ===")
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")

    def draw(self):
        screen.fill(DARK_GRAY)
        y = 200
        self.button_rects.clear()
        
        for option in self.options:
            text_surface = font.render(option, True, WHITE)
            text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, y))
            button_rect = pygame.Rect(text_rect.x - 20, text_rect.y - 10, text_rect.width + 40, text_rect.height + 20)
            
            pygame.draw.rect(screen, BLUE, button_rect, border_radius=10)
            screen.blit(text_surface, text_rect)
            self.button_rects.append(button_rect)
            y += 100

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i, button_rect in enumerate(self.button_rects):
                if button_rect.collidepoint(mouse_pos):
                    return i
        return None
