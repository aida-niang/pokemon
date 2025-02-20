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
from pokemon import Pokemon
from gif import load_gif_frames

pygame.init()

#Load background 
start_screen_bg = pygame.image.load("assets/images/background/loading.jpg")
start_screen_bg = pygame.transform.scale(start_screen_bg, (WIDTH, HEIGHT))
name_bg = pygame.image.load('assets/images/background/name.jpg')
name_bg = pygame.transform.scale(start_screen_bg, (WIDTH, HEIGHT))
select_bg = pygame.image.load('assets/images/background/choose.jpg')
select_bg= pygame.transform.scale(select_bg, (WIDTH, HEIGHT))

#load GIF frames
loading_frames = load_gif_frames("assets/images/gif/loading")

#load sounds :
sound_loading = pygame.mixer.Sound('assets/sounds/loading.mp3')
sound_start = pygame.mixer.Sound('assets/sounds/start.mp3')
sound_Battle = pygame.mixer.Sound('assets/sounds/battle.wav')
sound_Attack = pygame.mixer.Sound('assets/sounds/attack.wav')
sound_Victory = pygame.mixer.Sound('assets/sounds/victory.wav')

sound_loading.play()
def loading_screen():
    frame_index = 0
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()

    running = True
    while running:
        screen.blit(start_screen_bg, (0, 0))

        # Display text "Loading..."
        loading_text = font.render("Loading...", True, WHITE)
        screen.blit(loading_text, (620, 700))

        # Display animation gif
        screen.blit(loading_frames[frame_index], (600, 730))
        frame_index = (frame_index + 1) % len(loading_frames)  # Change frame

        pygame.display.flip()
        clock.tick(10)  # speed (~10 FPS)

        # Stop after 3 seconds
        if pygame.time.get_ticks() - start_time > 3000:
            running = False

        # Handle events (close window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    sound_loading.stop()

sound_start.play()
def select_pokemon(player_name, pokemon_choices):
    """Handles Pokémon selection."""
    global player_pokemon
    current_index = 0
    running = True

    # Get all available Pokémon (initial + won Pokémon)
    available_pokemon = get_player_pokemon(player_name, pokemon_choices)

    while running:
        screen.blit(select_bg, (0, 0))
        draw_text("Select Your Pokémon", WIDTH // 2, 50)

        # Show current Pokémon selection
        pokemon = available_pokemon[current_index]
        print(pokemon)
        sprite = load_sprite(pokemon)

        if sprite:
            sprite = pygame.transform.scale(sprite, (300, 300))
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
                pokemon_list = fetch_pokemon()
                sound_start.stop()
                #temp_pokemon = Pokemon(pokemon_list[5].get('id'), pokemon_list[5].get('name'), pokemon_list[5].get('sprite'), pokemon_list[5].get('stats'), pokemon_list[5].get('apiTypes'), pokemon_list[5].get('apiResistances'))

                for pokemon in pokemon_list: 
                    if pokemon.get('id') == player_pokemon.get('id'):
                        playable_player_pokemon = Pokemon(pokemon.get('id'), pokemon.get('name'), pokemon.get('sprite'), pokemon.get('stats'), pokemon.get('apiTypes'), pokemon.get('apiResistances'))
                        print(playable_player_pokemon)
                        #playable_player_pokemon.attack_target(temp_pokemon, playable_player_pokemon.special_attack)

                # Create a list of enemies (excluding player's Pokémon)
                enemy_pokemon_list = [p for p in pokemon_list if p["id"] != player_pokemon["id"]]
                enemy_id = random.randint(0, 150)
                playable_enemy_pokemon = Pokemon(pokemon_list[enemy_id].get('id'), pokemon_list[enemy_id].get('name'), pokemon_list[enemy_id].get('sprite'), pokemon_list[enemy_id].get('stats'), pokemon_list[enemy_id].get('apiTypes'), pokemon_list[enemy_id].get('apiResistances'))


                while True:  # Keep battling until player loses or runs out of enemies
                    if not enemy_pokemon_list:
                        print("🎉 You defeated all enemies!")
                        draw_text("You defeated all enemies!", WIDTH // 2, HEIGHT // 2)
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        break

                    enemy_pokemon = enemy_pokemon_list.pop(0)  # Get next enemy
                    winner = battle(player_pokemon, [enemy_pokemon], player_name, playable_player_pokemon, playable_enemy_pokemon)  # Pass list with one enemy

                    if winner == playable_player_pokemon:
                        print(f"🎉 {player_name} won with {playable_player_pokemon.name}!")
                        sound_Battle.stop()
                        sound_Victory.play()
                        save_game(player_name, enemy_pokemon, player_level)  # Save the defeated Pokémon
                    else:
                        print(f"💥 {player_name} lost with {playable_player_pokemon.name}!")
                        break  # Stop the loop when the player loses
    pygame.quit()