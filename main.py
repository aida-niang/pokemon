import pygame
import random
from utils import load_sprite, fetch_pokemon, pokemon_choices
from settings import *
from battle import battle
from menu import Menu
from pokedex import pokedex

pygame.init()

pokemon_list = fetch_pokemon()

def select_pokemon():
    global player_pokemon, enemy_pokemon
    current_index = 0
    running = True
    
    while running:
        screen.fill(WHITE)
        draw_text("Select Your Pokémon", WIDTH // 2, 50)
        
        pokemon = pokemon_choices[current_index]
        sprite = load_sprite(pokemon)
        
        if sprite:
            sprite = pygame.transform.scale(sprite, (200, 200))
            screen.blit(sprite, (WIDTH // 2 - 100, HEIGHT // 2 - 100))
        
        draw_text(f"{pokemon['name']} (#{pokemon['id']})", WIDTH // 2, HEIGHT // 2 + 120)
        draw_text("← / → : Naviguer  |  ENTER : Sélectionner", WIDTH // 2, HEIGHT - 50)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    current_index = (current_index + 1) % len(pokemon_choices)
                elif event.key == pygame.K_LEFT:
                    current_index = (current_index - 1) % len(pokemon_choices)
                elif event.key == pygame.K_RETURN:
                    player_pokemon = pokemon
                    enemy_pokemon = random.choice([p for p in pokemon_choices if p != player_pokemon])  # Random adversary. Remplace pokemon_choices with pokemon_list for random among all the Pokedex.
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
            player_pokemon, enemy_pokemon = select_pokemon()
            battle(player_pokemon, enemy_pokemon)

pygame.quit()
