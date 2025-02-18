import json

# Load save data from file
def load_save():
    try:
        with open("save_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Return an empty dictionary if no save file exists

# Save game data to file
def save_game(player_name, defeated_pokemon, player_level):
    # Load existing save data
    saved_data = load_save()

    # Ensure defeated_pokemon is in dictionary form if it's not already
    if isinstance(defeated_pokemon, dict):
        pokemon_to_save = defeated_pokemon
    else:
        pokemon_to_save = {"name": defeated_pokemon, "id": 999}  # Replace 999 with the correct Pokémon ID

    # If player data exists, update it, otherwise, create a new entry
    if player_name in saved_data:
        # Add the defeated Pokémon to the player's list of won Pokémon (if not already in the list)
        if pokemon_to_save not in saved_data[player_name].get("pokemon_won", []):
            saved_data[player_name]["pokemon_won"].append(pokemon_to_save)
        # Update the player's level
        saved_data[player_name]["level"] = player_level
    else:
        # Create a new entry for the player if they don't exist
        saved_data[player_name] = {
            "pokemon_won": [pokemon_to_save],  # Add the first won Pokémon
            "level": player_level  # Initialize the player's level
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

# Load saved player's level
def get_player_level(player_name):
    saved_data = load_save()
    if player_name in saved_data:
        return saved_data[player_name].get("level", 0)  # Default to 0 if no level is saved
    else:
        return 0  # Default level if no saved data
