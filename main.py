import pygame
import random
from utils import load_sprite, fetch_pokemon, pokemon_choices
from settings import *
from battle import battle
from menu import Menu
from pokedex import pokedex
from players import get_player_name, load_pokedex  
from save_manager import load_save, save_game  

pygame.init()

player_name = get_player_name()
pokemon_list = fetch_pokemon()

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

def select_pokemon():
    global player_pokemon, enemy_pokemon
    current_index = 0
    running = True

    # Include saved Pokémon in the list of choices
    pokemon_choices_with_saved = pokemon_choices.copy()  # Copy the original list
    if saved_pokemon:  # If there is a saved Pokémon, add it to the list
        pokemon_choices_with_saved.append(saved_pokemon)

    while running:
        screen.fill(WHITE)
        draw_text("Select Your Pokémon", WIDTH // 2, 50)

        # Show current Pokémon selection
        pokemon = pokemon_choices_with_saved[current_index]  # Pokémon is a dictionary
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
                    current_index = (current_index + 1) % len(pokemon_choices_with_saved)
                elif event.key == pygame.K_LEFT:
                    current_index = (current_index - 1) % len(pokemon_choices_with_saved)
                elif event.key == pygame.K_RETURN:
                    player_pokemon = pokemon  # Set the selected Pokémon as player's Pokémon
                    enemy_pokemon = random.choice([p for p in pokemon_list if p["id"] != player_pokemon["id"]])
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
            # Ask if player wants to use saved Pokémon or select a new one
            if saved_pokemon:
                screen.fill(WHITE)
                draw_text(f"Would you like to use your saved Pokémon {saved_pokemon['name']}?", WIDTH // 2, HEIGHT // 2 - 40)
                draw_text("Press ENTER to use saved, ESC to select a new one", WIDTH // 2, HEIGHT // 2 + 40)
                pygame.display.flip()

                waiting_for_input = True
                while waiting_for_input:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                player_pokemon = saved_pokemon  # Use saved Pokémon
                                enemy_pokemon = random.choice([p for p in pokemon_choices if p["id"] != player_pokemon["id"]])
                                waiting_for_input = False
                            elif event.key == pygame.K_ESCAPE:
                                player_pokemon, enemy_pokemon = select_pokemon()
                                waiting_for_input = False
            else:
                player_pokemon, enemy_pokemon = select_pokemon()

            winner = battle(player_pokemon, enemy_pokemon)
            if winner == player_pokemon:
                print(f"🎉 {player_name} won with {player_pokemon['name']}!")
                save_game(player_name, enemy_pokemon)  # Save the defeated enemy Pokémon if the player wins
            else:
                print(f"💥 {player_name} lost with {player_pokemon['name']}!")
                save_game(player_name, enemy_pokemon)  # Save the defeated enemy Pokémon even if the player loses

pygame.quit()
