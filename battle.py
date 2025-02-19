import pygame
import random
from utils import load_sprite, pokemon_choices, fetch_pokemon
from settings import *
from save_manager import save_game, get_player_level
from pokemon import Pokemon
import math

# Load the background image
background = pygame.image.load('assets/images/background/bg1.jpg')

# Load the feu.png image (for the object)
fire_object = pygame.image.load('fire.png')  # Adjust the path as needed
fire_object = pygame.transform.scale(fire_object, (fire_object.get_width() // 6, fire_object.get_height() // 6))
fire_object_rect = fire_object.get_rect()

def draw_health_bar(x, y, health, max_health):
    """Draws a health bar for Pokémon."""
    bar_width = 150
    bar_height = 15
    fill = max(0, (health / max_health) * bar_width)  # Ensure health bar doesn't go negative
    pygame.draw.rect(screen, RED, (x, y, bar_width, bar_height))  # Background (red)
    pygame.draw.rect(screen, GREEN, (x, y, fill, bar_height))  # Health (green)

def battle(player_pokemon, enemy_pokemon_list, player_name, playable_player_pokemon, playable_enemy_pokemon):
    """Simulates a Pokémon battle with movement and multiple enemies."""
    enemy_index = 0  
    player_level = get_player_level(player_name)  

    # Position initiale du Pokémon du joueur
    player_x = WIDTH // 4 - 75
    player_y = HEIGHT // 2 - 75

    # Position de l'ennemi
    enemy_x = 3 * WIDTH // 4 - 75
    enemy_y = HEIGHT // 2 - 75

    # Position initiale du feu
    fire_x, fire_y = player_x + 50, player_y + 50
    fire_speed = 15  
    fire_moving = False  

    running = True
    while running:
        screen.fill(WHITE)  

        # Charger les sprites
        player_sprite = load_sprite(playable_player_pokemon)
        enemy_sprite = load_sprite(playable_enemy_pokemon)

        if player_sprite:
            player_sprite = pygame.transform.scale(player_sprite, (150, 150))
            screen.blit(player_sprite, (player_x, player_y))

        if enemy_sprite:
            enemy_sprite = pygame.transform.scale(enemy_sprite, (150, 150))
            screen.blit(enemy_sprite, (enemy_x, enemy_y))

        # Afficher le feu
        screen.blit(fire_object, (fire_x, fire_y))

        # Afficher les noms et niveaux
        draw_text(playable_player_pokemon.name.capitalize(), WIDTH // 4, HEIGHT - 100)
        draw_text(playable_enemy_pokemon.name.capitalize(), 3 * WIDTH // 4, HEIGHT - 100)

        # Afficher les barres de vie
        draw_health_bar(WIDTH // 4 - 75, HEIGHT - 130, playable_player_pokemon.stats.get("HP"), playable_player_pokemon.max_hp)
        draw_health_bar(3 * WIDTH // 4 - 75, HEIGHT - 130, playable_enemy_pokemon.stats.get("HP"), playable_enemy_pokemon.max_hp)

        # Déplacer le feu vers l'ennemi
        if fire_moving:
            dx, dy = enemy_x - fire_x, enemy_y - fire_y
            distance = math.sqrt(dx ** 2 + dy ** 2)
            if distance > 0:
                dx /= distance
                dy /= distance
                fire_x += dx * fire_speed
                fire_y += dy * fire_speed

            # Vérifier la collision du feu avec l'ennemi
            if abs(fire_x - enemy_x) < 20 and abs(fire_y - enemy_y) < 20:
                playable_enemy_pokemon.stats["HP"] -= 10  # Réduire les HP de l'ennemi
                fire_x, fire_y = player_x + 50, player_y + 50  # Reset du feu
                fire_moving = False  

                if playable_enemy_pokemon.stats["HP"] <= 0:
                    print(f"{playable_enemy_pokemon.name} est vaincu !")
                    draw_text(f"{playable_enemy_pokemon.name.capitalize()} est vaincu!", WIDTH // 2, HEIGHT // 2)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    break  # Fin du combat

        pygame.display.flip()

        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return None  

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not fire_moving:  
                    fire_moving = True  

                if event.key == pygame.K_1:  
                    playable_player_pokemon.attack_target(playable_enemy_pokemon, playable_player_pokemon.normal_attack)
                    playable_enemy_pokemon.attack_target(playable_player_pokemon, playable_enemy_pokemon.normal_attack)

                elif event.key == pygame.K_2:  
                    playable_player_pokemon.attack_target(playable_enemy_pokemon, playable_player_pokemon.special_attack)
                    playable_enemy_pokemon.attack_target(playable_player_pokemon, playable_enemy_pokemon.special_attack)

        pygame.time.delay(50)  

    return playable_player_pokemon  
