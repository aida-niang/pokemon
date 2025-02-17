import json
import os

def load_save(): #Load the game save file.
    if os.path.exists('save_data.json'):
        with open('save_data.json', 'r') as file:
            return json.load(file)
    else:
        return {}

def save_game(player_name, enemy_pokemon): #Save the player's game, including the Pokémon they defeated.
    saved_data = load_save()

    if player_name not in saved_data:
        saved_data[player_name] = {"pokemon_won": []}

    # Add the defeated enemy to the player's won Pokémon list
    saved_data[player_name]["pokemon_won"].append(enemy_pokemon)

    with open('save_data.json', 'w') as file:
        json.dump(saved_data, file, indent=4)

    print(f"{enemy_pokemon['name']} has been saved to your collection!")
