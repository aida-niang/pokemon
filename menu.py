import pygame
from settings import *
from pokedex import pokedex
from save_manager import load_save

background = pygame.image.load('assets/images/background/bg1.jpg')

class Menu:
    def __init__(self, player_name):
        self.options = [
            "Launch the game",
            "View Pokédex",
            "Quit"
        ]
        self.player_name = player_name 
        self.button_rects = []

    def display_menu(self):
        print("\nWelcome to Pokémon Game!")
        print("\n=== Menu ===")
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")

    def draw(self):
        screen.blit(background, (0, 0))
        y = 200
        self.button_rects.clear()
        
        for option in self.options:
            text = font.render(option, True, (255, 255, 255))
            text_rect = text.get_rect(center=(WIDTH // 2, y))
            button_rect = pygame.Rect(text_rect.x - 20, text_rect.y - 10, text_rect.width + 40, text_rect.height + 20)
            pygame.draw.rect(screen, (0, 122, 255), button_rect, border_radius=10)
            screen.blit(text, text_rect)
            self.button_rects.append(text_rect)
            y += 80
        
        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i, text_rect in enumerate(self.button_rects):
                if text_rect.collidepoint(mouse_pos):
                    if i == 1:  # View Pokédex
                        pokedex(self.player_name)
                        return None  # Prevent immediate return to menu
                    return i
        return None