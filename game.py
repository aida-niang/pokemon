#game

import pygame
import random
from utils import load_sprite, fetch_pokemon, pokemon_choices
from settings import *
from battle import battle
from menu import Menu
from pokedex import pokedex
from players import get_player_name  
from save_manager import load_save, save_game, get_player_pokemon,get_player_level

pygame.init()

background = pygame.image.load('assets/images/background/bg1.jpg')
  
def select_pokemon(player_name, pokemon_choices):
    """Handles Pokémon selection."""
    global player_pokemon
    current_index = 0
    running = True

    # Get all available Pokémon (initial + won Pokémon)
    available_pokemon = get_player_pokemon(player_name, pokemon_choices)

    while running:
        screen.blit(background, (0, 0))
        draw_text("Select Your Pokémon", WIDTH // 2, 50)

        # Show current Pokémon selection
        pokemon = available_pokemon[current_index]
        sprite = load_sprite(pokemon)

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
                    running = False
                elif event.key == pygame.K_ESCAPE:
                    running = False

    return player_pokemon

# Main Game Loop
def start_game():
    player_name = get_player_name()
    pokemon_list = fetch_pokemon()
    player_level = get_player_level(player_name)  

    # Load existing save if available
    saved_data = load_save()
    if player_name in saved_data:
        saved_pokemon_list = saved_data[player_name].get("pokemon_won", [])
        if saved_pokemon_list:
            saved_pokemon = saved_pokemon_list[-1]  # Get the last Pokémon the player won
            print(f"🎉 Welcome back, {player_name}! Your saved Pokémon: {saved_pokemon}")
            if isinstance(saved_pokemon, dict):
                print(f"Saved Pokémon Name: {saved_pokemon['name']}")
            else:
                print("Error: The saved Pokémon is not in the expected format.")
        else:
            saved_pokemon = None  # No saved Pokémon
  
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
                player_pokemon = select_pokemon(player_name, pokemon_choices)

                # Create a list of enemies (excluding player's Pokémon)
                enemy_pokemon_list = [p for p in pokemon_list if p["id"] != player_pokemon["id"]]

                while True:  # Keep battling until player loses or runs out of enemies
                    if not enemy_pokemon_list:
                        print("🎉 You defeated all enemies!")
                        draw_text("You defeated all enemies!", WIDTH // 2, HEIGHT // 2)
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        break

                    enemy_pokemon = enemy_pokemon_list.pop(0)  # Get next enemy
                    winner = battle(player_pokemon, [enemy_pokemon], player_name)  # Pass list with one enemy

                    if winner == player_pokemon:
                        print(f"🎉 {player_name} won with {player_pokemon['name']}!")
                        save_game(player_name, enemy_pokemon, player_level)  # Save the defeated Pokémon
                    else:
                        print(f"💥 {player_name} lost with {player_pokemon['name']}!")
                        break  # Stop the loop when the player loses

    pygame.quit()