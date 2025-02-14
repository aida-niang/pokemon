import requests
import json
import os

DATA_DIR = "data"
SPRITE_DIR = os.path.join(DATA_DIR, "sprites")
POKEMON_FILE = os.path.join(DATA_DIR, "pokemon.json")

os.makedirs(SPRITE_DIR, exist_ok=True)  # Ensure sprite directory exists

def download_sprite(pokemon):
    """Downloads the Pokémon sprite and saves it locally."""
    sprite_path = os.path.join(SPRITE_DIR, f"{pokemon['id']}.png")

    if os.path.exists(sprite_path):
        return sprite_path  # Use existing file

    sprite_url = pokemon["sprites"]["front_default"]
    if sprite_url:
        response = requests.get(sprite_url)
        if response.status_code == 200:
            with open(sprite_path, "wb") as f:
                f.write(response.content)
            return sprite_path

    print(f"Failed to download sprite for {pokemon['name']}")
    return None

def fetch_pokemon():
    """Fetch Pokémon data from PokéAPI and save it locally."""
    url = "https://pokeapi.co/api/v2/pokemon?limit=151"  # Change 151 to 1025 for all Pokémon
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch Pokémon data!")
        return

    data = response.json()
    pokemon_list = []

    for pokemon in data["results"]:
        pokemon_data = requests.get(pokemon["url"]).json()
        sprite_path = download_sprite(pokemon_data)  # Download and save sprite

        pokemon_list.append({
            "id": pokemon_data["id"],
            "name": pokemon_data["name"],
            "sprite": sprite_path  # Save local path instead of URL
        })

    # Save data to JSON
    with open(POKEMON_FILE, "w") as f:
        json.dump(pokemon_list, f, indent=4)

    print(f"Successfully saved {len(pokemon_list)} Pokémon to {POKEMON_FILE}")

if __name__ == "__main__":
    fetch_pokemon()
