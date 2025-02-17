import json

# Load save data from file
def load_save():
    try:
        with open("save_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Return an empty dictionary if no save file exists

# Save game data to file
def save_game(player_name, defeated_pokemon):
    # Load existing save data
    saved_data = load_save()

    # If player data exists, update it, otherwise, create a new entry
    if player_name in saved_data:
        # Add the defeated Pokémon to the player's list of won Pokémon (if not already in the list)
        if defeated_pokemon not in saved_data[player_name].get("pokemon_won", []):
            saved_data[player_name]["pokemon_won"].append(defeated_pokemon)
    else:
        # Create a new entry for the player if they don't exist
        saved_data[player_name] = {
            "pokemon_won": [defeated_pokemon]  # Add the first won Pokémon
        }

    # Write the updated data back to the save file
    with open("save_data.json", "w") as file:
        json.dump(saved_data, file, indent=4)

# Get the player's available Pokémon (initial + won Pokémon)
def get_player_pokemon(player_name, pokemon_choices):
    saved_data = load_save()
    if player_name in saved_data:
        # Combine initial Pokémon (first 3) with the ones won by the player
        return pokemon_choices[:3] + saved_data[player_name].get("pokemon_won", [])
    else:
        # If no saved data, just return the first 3 Pokémon from pokemon_choices
        return pokemon_choices[:3]
