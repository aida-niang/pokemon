# utils.py

import os
import json
import pygame
import requests
import io
from io import BytesIO

# Constants
DATA_DIR = "data"
SPRITE_DIR = os.path.join(DATA_DIR, "sprites")
POKEMON_FILE = os.path.join(DATA_DIR, "pokemon.json")

# Manually define the three Pokémon (Carapuce, Salamèche, Bulbizarre)
pokemon_choices = [
    {"name": "Carapuce", "id": 7, "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png"},
    {"name": "Salamèche", "id": 4, "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png"},
    {"name": "Bulbizarre", "id": 1, "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"}
]

# Fetch Pokémon from API (Fallback to Local Data)
def fetch_pokemon():
    api_url = "https://pokebuildapi.fr/api/v1/pokemon/generation/1"
    
    try:
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            with open(POKEMON_FILE, "w") as f:
                json.dump(data, f, indent=4)
            return data
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error fetching Pokémon data online: {e}")

    return load_pokemon()

# Load Pokémon Data Locally
def load_pokemon():
    if not os.path.exists(POKEMON_FILE):
        print("❌ No Pokémon data found locally. Run online fetch first.")
        return []
    with open(POKEMON_FILE, "r") as f:
        return json.load(f)

# Load sprite (URL first, fallback to local file)
def load_sprite(url):
    """Charge une image depuis une URL et la convertit en surface Pygame."""
    try:
        response = requests.get(url)  # Télécharge l'image
        if response.status_code == 200:
            image = pygame.image.load(io.BytesIO(response.content))  # Charge l'image en mémoire
            return image
        else:
            print(f"Erreur de chargement de l'image: {url}")
            return None
    except Exception as e:
        print(f"Exception lors du chargement du sprite: {e}")
        return None

