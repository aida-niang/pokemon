#players.py

import os
import pygame
from settings import *

POKEDEX_FILE = "pokedex.txt"
background = pygame.image.load('assets/images/background/bg1.jpg')

def get_player_name():
    """Ask the player to enter their name."""
    pygame.init()
    pygame.display.set_caption("Enter Your Name")
    
    input_box = pygame.Rect(300, 300, 200, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ""

    font = pygame.font.Font(None, 36)

    while True:
        screen.blit(background, (0, 0))
        
        label = font.render("Enter your name:", True, (255, 255, 255))
        screen.blit(label, (310, 250))

        pygame.draw.rect(screen, color, input_box, 2)
        name_surface = font.render(text, True, (255, 255, 255))
        screen.blit(name_surface, (input_box.x + 5, input_box.y + 5))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                    color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN and text.strip():
                        return text.strip()
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

def load_pokedex(player_name):
    """Loads the player's saved Pokémon or assigns starter Pokémon."""
    default_pokemon = ["Charmander", "Squirtle", "Bulbasaur"]

    if not os.path.exists(POKEDEX_FILE):
        return default_pokemon  # Return default Pokémon if file doesn't exist

    try:
        with open(POKEDEX_FILE, "r", encoding="utf-8") as f:
            pokedex_data = {}
            for line in f:
                parts = line.strip().split(": ")
                if len(parts) == 2:
                    name, pokemons = parts
                    pokedex_data[name] = pokemons.split(", ")

        return pokedex_data.get(player_name, default_pokemon)  # Return player’s Pokémon or default
    except Exception as e:
        print(f"⚠️ Error loading Pokédex: {e}")
        return default_pokemon  # Return default in case of error

def update_pokedex(player_name, new_pokemon):
    """Updates the player's saved Pokémon after winning battles."""
    pokedex_data = {}

    # Read existing data
    if os.path.exists(POKEDEX_FILE):
        try:
            with open(POKEDEX_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(": ")
                    if len(parts) == 2:
                        name, pokemons = parts
                        pokedex_data[name] = pokemons.split(", ")
        except Exception as e:
            print(f"⚠️ Error reading Pokédex file: {e}")

    # Ensure the player has an entry
    if player_name not in pokedex_data:
        pokedex_data[player_name] = ["Charmander", "Squirtle", "Bulbasaur"]

    # Add the new Pokémon if it's not already in the list
    if new_pokemon not in pokedex_data[player_name]:
        pokedex_data[player_name].append(new_pokemon)

    # Write back to file
    try:
        with open(POKEDEX_FILE, "w", encoding="utf-8") as f:
            for name, pokemons in pokedex_data.items():
                f.write(f"{name}: {', '.join(pokemons)}\n")
        print(f"✅ {new_pokemon} added to {player_name}'s Pokédex!")
    except Exception as e:
        print(f"⚠️ Error saving Pokédex: {e}")