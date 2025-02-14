import pygame
import random
from utils import load_sprite
from settings import *
from battle import battle  # Import the battle function

pygame.init()

# Manually define the three Pokémon (Carapuce, Salamèche, Bulbizarre)
pokemon_choices = [
    {"name": "Carapuce", "id": 7, "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png"},
    {"name": "Salamèche", "id": 4, "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png"},
    {"name": "Bulbizarre", "id": 1, "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"}
]

def select_pokemon():
    """Menu de sélection du Pokémon"""
    global player_pokemon, enemy_pokemon, current_index
    current_index = 0  # Initialize index

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
battle(player_pokemon, enemy_pokemon)  # Call battle with selected Pokémon

pygame.quit()
