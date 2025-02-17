import pygame
import random
from menu import Menu
from utils import load_sprite
from settings import *
from battle import battle  # Import the battle function

pygame.init()

# Set screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pokémon Game")

# Define colors
WHITE = (255, 255, 255)

# Pokémon choices
pokemon_choices = [
    {"name": "Carapuce", "id": 7, "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png"},
    {"name": "Salamèche", "id": 4, "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png"},
    {"name": "Bulbizarre", "id": 1, "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"}
]

# Function to display text
def draw_text(text, x, y):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Pokémon selection function
def select_pokemon():
    """Menu for selecting a Pokémon"""
    global player_pokemon, enemy_pokemon
    current_index = 0  # Initialize index

    running = True
    while running:
        screen.fill(WHITE)
        draw_text("Select Your Pokémon", SCREEN_WIDTH // 2, 50)

        pokemon = pokemon_choices[current_index]
        
        # Charger l'image du Pokémon
        sprite_url = pokemon["sprite"]  # Récupère l'URL sous forme de string
        sprite = load_sprite(sprite_url)  # Passe uniquement l'URL à load_sprite()

        
        if sprite:
            sprite = pygame.transform.scale(sprite, (200, 200))  # Redimensionner
            screen.blit(sprite, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 100))

        # Affichage du nom et des points de vie
        draw_text(pokemon["name"], SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120)
        draw_text(f"HP: 100", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 160)  # Exemple de PV

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    current_index = (current_index + 1) % len(pokemon_choices)  # Cycle right
                elif event.key == pygame.K_LEFT:
                    current_index = (current_index - 1) % len(pokemon_choices)  # Cycle left
                elif event.key == pygame.K_RETURN:
                    player_pokemon = pokemon
                    enemy_pokemon = random.choice(pokemon_choices)  # Random enemy choice
                    running = False

    return player_pokemon, enemy_pokemon  # Retourner les choix pour la bataille

# Main loop
def main():
    menu = Menu()
    running = True

    while running:
        screen.fill(WHITE)
        menu.draw()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                choice = menu.handle_event(event)

                if choice == 0:  # "Launch the game"
                    player_pokemon, enemy_pokemon = select_pokemon()
                    battle(player_pokemon, enemy_pokemon)  # Lancer la bataille après la sélection
                elif choice == 1:  # "Add a Pokémon" (to be implemented)
                    print("Add Pokémon feature coming soon...")
                elif choice == 2:  # "Quit"
                    running = False

    pygame.quit()

if __name__ == "__main__":
    main()
