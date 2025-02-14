import pygame
import json
import os

DATA_DIR = "data"
SPRITE_DIR = os.path.join(DATA_DIR, "sprites")
POKEMON_FILE = os.path.join(DATA_DIR, "pokemon.json")
POKEDEX_FILE = os.path.join(DATA_DIR, "pokedex.json")

def load_pokemon():
    """Loads Pokémon data from JSON."""
    if not os.path.exists(POKEMON_FILE):
        print("No Pokémon data found! Run fetch_pokemon.py first.")
        return []
    with open(POKEMON_FILE, "r") as f:
        return json.load(f)

def load_sprite(pokemon):
    """Loads a Pokémon sprite from file."""
    sprite_path = pokemon["sprite"]
    if os.path.exists(sprite_path):
        return pygame.image.load(sprite_path)
    print(f"Sprite not found: {sprite_path}")
    return None
