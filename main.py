import pygame
import random
from menu import Menu

pygame.init()

# Set screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
    global player_pokemon, enemy_pokemon, current_index
    current_index = 0  # Initialize index

    running = True
    while running:
        screen.fill(WHITE)
        draw_text("Select Your Pokémon", SCREEN_WIDTH // 2, 50)

        pokemon = pokemon_choices[current_index]
        
        draw_text(pokemon["name"], SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120)

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
            choice = menu.handle_event(event)

            if choice == 0:  # "Launch the game"
                select_pokemon()
            elif choice == 1:  # "Add a Pokémon" (to be implemented)
                print("Add Pokémon feature coming soon...")
            elif choice == 2:  # "Quit"
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
