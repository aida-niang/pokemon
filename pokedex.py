#pokedex

import pygame
from settings import *
from utils import fetch_pokemon, load_sprite

def display_pokemon_info(pokemon):
    running = True
    while running:
        screen.fill(WHITE)
        draw_text("Pokémon Info", WIDTH // 2, 50)

        sprite = load_sprite(pokemon)
        if sprite:
            sprite = pygame.transform.scale(sprite, (200, 200))
            screen.blit(sprite, (WIDTH // 2 - 100, HEIGHT // 2 - 100))

        draw_text(f"{pokemon['name']} (#{pokemon['id']})", WIDTH // 2, HEIGHT // 2 + 120)
        draw_text(f"Type: {', '.join([t['name'] for t in pokemon['apiTypes']])}", WIDTH // 2, HEIGHT // 2 + 150)
        draw_text(f"HP: {pokemon['stats']['HP']} | ATK: {pokemon['stats']['attack']} | DEF: {pokemon['stats']['defense']}", WIDTH // 2, HEIGHT // 2 + 180)

        draw_text("Press ESC to return", WIDTH // 2, HEIGHT - 50)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return 

def pokedex():
    pokemon_list = fetch_pokemon()
    current_index = 0
    running = True

    while running:
        screen.fill(WHITE)
        draw_text("Pokédex", WIDTH // 2, 50)

        if pokemon_list:
            pokemon = pokemon_list[current_index]
            sprite = load_sprite(pokemon)
            
            if sprite:
                sprite = pygame.transform.scale(sprite, (200, 200))
                screen.blit(sprite, (WIDTH // 2 - 100, HEIGHT // 2 - 100))

            draw_text(f"{pokemon['name']} (#{pokemon['id']})", WIDTH // 2, HEIGHT // 2 + 120)

        draw_text("← / → : Naviguer  |  ESC : Quitter  |  ENTER : Voir Infos", WIDTH // 2, HEIGHT - 50)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RIGHT:
                    current_index = (current_index + 1) % len(pokemon_list)
                elif event.key == pygame.K_LEFT:
                    current_index = (current_index - 1) % len(pokemon_list)
                elif event.key == pygame.K_RETURN:
                    display_pokemon_info(pokemon)

    return None
