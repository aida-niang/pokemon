import pygame
import random
from utils import load_sprite, fetch_pokemon, pokemon_choices
from settings import *
from battle import battle
from menu import Menu
from pokedex import pokedex
from players import get_player_name  
from save_manager import load_save, save_game, get_player_pokemon

pygame.init()

player_name = get_player_name()
pokemon_list = fetch_pokemon()
background = pygame.image.load('data/background/bg1.jpg')

# Load existing save if available
saved_data = load_save()
if player_name in saved_data:
    saved_pokemon_list = saved_data[player_name].get("pokemon_won", [])
    if saved_pokemon_list:
        saved_pokemon = saved_pokemon_list[-1]  # Get the last Pokémon the player won
        print(f"🎉 Welcome back, {player_name}! Your saved Pokémon: {saved_pokemon['name']}")
    else:
        saved_pokemon = None  # No saved Pokémon
else:
    saved_pokemon = None  # No saved data

def select_pokemon(player_name, pokemon_choices):
    global player_pokemon, enemy_pokemon
    current_index = 0
    running = True

    # Get all available Pokémon (initial + won Pokémon)
    available_pokemon = get_player_pokemon(player_name, pokemon_choices)

    while running:
        screen.blit(background, (0, 0))
        draw_text("Select Your Pokémon", WIDTH // 2, 50)

        # Show current Pokémon selection
        pokemon = available_pokemon[current_index]  # Pokémon is a dictionary
        sprite = load_sprite(pokemon)  # load_sprite expects a dictionary

        if sprite:
            sprite = pygame.transform.scale(sprite, (200, 200))
            screen.blit(sprite, (WIDTH // 2 - 100, HEIGHT // 2 - 100))

        # Display Pokémon info
        draw_text(f"{pokemon['name']} (#{pokemon['id']})", WIDTH // 2, HEIGHT // 2 + 120)
        draw_text("← / → : Navigate  |  ENTER : Select  |  ESC : Back", WIDTH // 2, HEIGHT - 50)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    current_index = (current_index + 1) % len(available_pokemon)
                elif event.key == pygame.K_LEFT:
                    current_index = (current_index - 1) % len(available_pokemon)
                elif event.key == pygame.K_RETURN:
                    player_pokemon = pokemon  # Set the selected Pokémon as player's Pokémon
                    enemy_pokemon = random.choice([p for p in pokemon_choices if p["id"] != player_pokemon["id"]])
                    running = False
                elif event.key == pygame.K_ESCAPE:
                    running = False

    return player_pokemon, enemy_pokemon


# Main Game Loop
menu = Menu()
option = None

while option != 2:
    menu.draw()
    pygame.display.flip()

    for event in pygame.event.get():
        option = menu.handle_event(event)

        if option == 1:
            pokedex()
        elif option == 0:
            available_pokemon = get_player_pokemon(player_name, pokemon_choices)
            player_pokemon, enemy_pokemon = select_pokemon(player_name, pokemon_choices)

            winner = battle(player_pokemon, enemy_pokemon)
            if winner == player_pokemon:
                print(f"🎉 {player_name} won with {player_pokemon['name']}!")
                save_game(player_name, enemy_pokemon)  # Save the defeated enemy Pokémon if the player wins
            else:
                print(f"💥 {player_name} lost with {player_pokemon['name']}!")
                save_game(player_name, enemy_pokemon)  # Save the defeated enemy Pokémon even if the player loses

pygame.quit()