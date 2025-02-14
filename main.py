import pygame
import random
from utils import load_sprite

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokémon Battle")

# Manually define the three Pokémon (Carapuce, Salamèche, Bulbizarre)
pokemon_choices = [
    {"name": "Carapuce", "id": 7, "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png"},
    {"name": "Salamèche", "id": 4, "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png"},
    {"name": "Bulbizarre", "id": 1, "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"}
]

current_index = 0
player_pokemon = None
enemy_pokemon = None

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fonts
font = pygame.font.Font(None, 36)

def draw_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x - text_surface.get_width() // 2, y))

def draw_health_bar(x, y, health, max_health):
    bar_width = 150
    bar_height = 15
    fill = (health / max_health) * bar_width
    pygame.draw.rect(screen, RED, (x, y, bar_width, bar_height))
    pygame.draw.rect(screen, GREEN, (x, y, fill, bar_height))

def select_pokemon():
    """Menu de sélection du Pokémon"""
    global player_pokemon, enemy_pokemon, current_index

    running = True
    while running:
        screen.fill(WHITE)
        draw_text("Select Your Pokémon", WIDTH // 2, 50)

        pokemon = pokemon_choices[current_index]
        sprite = load_sprite(pokemon)
        
        if sprite:
            sprite = pygame.transform.scale(sprite, (200, 200))
            screen.blit(sprite, (WIDTH // 2 - 100, HEIGHT // 2 - 100))

        draw_text(pokemon["name"], WIDTH // 2, HEIGHT // 2 + 120)

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

# Main Game Loop
select_pokemon()

pygame.quit()
