import pygame
import random
from utils import load_sprite, pokemon_choices, fetch_pokemon
from settings import *
from save_manager import save_game, get_player_level
from pokemon import Pokemon

# Load the background image
background = pygame.image.load('assets/images/background/bg1.jpg')

def draw_health_bar(x, y, health, max_health):
    """Draws a health bar for Pokémon."""
    bar_width = 150
    bar_height = 15
    fill = (health / max_health) * bar_width
    pygame.draw.rect(screen, RED, (x, y, bar_width, bar_height))  # Draw red background bar
    pygame.draw.rect(screen, GREEN, (x, y, fill, bar_height))  # Draw green health indicator

def battle(player_pokemon, enemy_pokemon_list, player_name, playable_player_pokemon, playable_enemy_pokemon):
    """Simulates a Pokémon battle with movement and multiple enemies."""
    enemy_index = 0  # Track the current enemy Pokémon
    player_level = get_player_level(player_name)  # Retrieve the player's current level

    # Player Pokémon initial position
    player_x = WIDTH // 4 - 75
    player_y = HEIGHT // 2 - 75
    speed = 10  # Player movement speed

    running = True
    while running:
        # Check if all enemies are defeated
        if enemy_index >= len(enemy_pokemon_list):
            print("🎉 You defeated all enemies! You win!")
            draw_text("You defeated all enemies!", WIDTH // 2, HEIGHT // 2)
            pygame.display.flip()
            pygame.time.delay(2000)
            break  # Exit battle loop

        """# Check for evolution every 2 levels
        evolution_stage = (player_level // 2)  # Determine evolution stage
        evolved_pokemon = next((p for p in pokemon_choices if p['id'] == player_pokemon['id'] + evolution_stage), None)
        if evolved_pokemon:
            print(f"🎉 {player_pokemon['name']} evolved into {evolved_pokemon['name']}!")
            player_pokemon = evolved_pokemon  # Update to evolved Pokémon"""


        # Set random positions for player and enemy Pokémon to prevent overlap
        player_offset_x = random.randint(-50, 50)
        player_offset_y = random.randint(-50, 50)
        enemy_offset_x = random.randint(-50, 50)
        enemy_offset_y = random.randint(-50, 50)

        while playable_enemy_pokemon.stats.get("HP") > 0 and playable_player_pokemon.stats.get("HP") > 0:
            screen.fill(WHITE)  # Clear screen

            # Load player and enemy sprites
            player_sprite = load_sprite(playable_player_pokemon)
            enemy_sprite = load_sprite(playable_enemy_pokemon)

            # Draw Pokémon sprites if available
            if player_sprite:
                player_sprite = pygame.transform.scale(player_sprite, (150, 150))
                screen.blit(player_sprite, (player_x + player_offset_x, player_y + player_offset_y))

            if enemy_sprite:
                enemy_sprite = pygame.transform.scale(enemy_sprite, (150, 150))
                screen.blit(enemy_sprite, (3 * WIDTH // 4 - 75 + enemy_offset_x, HEIGHT // 2 - 75 + enemy_offset_y))

            # Display Pokémon names
            draw_text(playable_player_pokemon.name.capitalize(), WIDTH // 4, HEIGHT - 100)
            draw_text(playable_enemy_pokemon.name.capitalize(), 3 * WIDTH // 4, HEIGHT - 100)

            # Draw health bars
            draw_health_bar(WIDTH // 4 - 75, HEIGHT - 130, playable_player_pokemon.stats.get("HP"), playable_player_pokemon.max_hp)
            draw_health_bar(3 * WIDTH // 4 - 75, HEIGHT - 130, playable_enemy_pokemon.stats.get("HP"), playable_enemy_pokemon.max_hp)

            # Display player level and controls
            draw_text(f"Level: {player_level}", WIDTH // 2, HEIGHT - 20)
            draw_text("Arrow Keys: Move | 1: Attaque normale | 2: Attaque spéciale", WIDTH // 2, HEIGHT - 50)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return None  # Exit the function
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player_x -= speed
                    elif event.key == pygame.K_RIGHT:
                        player_x += speed
                    elif event.key == pygame.K_UP:
                        player_y -= speed
                    elif event.key == pygame.K_DOWN:
                        player_y += speed
                    elif event.key == pygame.K_1:  # Attack action
                        playable_player_pokemon.attack_target(playable_enemy_pokemon, playable_player_pokemon.normal_attack)
                        if random.randint(0,1) == 0:
                            playable_enemy_pokemon.attack_target(playable_player_pokemon, playable_enemy_pokemon.normal_attack)
                        else:
                            playable_enemy_pokemon.attack_target(playable_player_pokemon, playable_enemy_pokemon.special_attack)

                    elif event.key == pygame.K_2:  # Attack action
                        playable_player_pokemon.attack_target(playable_enemy_pokemon, playable_player_pokemon.special_attack)
                        if random.randint(0,1) == 0:
                            playable_enemy_pokemon.attack_target(playable_player_pokemon, playable_enemy_pokemon.normal_attack)
                        else:
                            playable_enemy_pokemon.attack_target(playable_player_pokemon, playable_enemy_pokemon.special_attack)


                    if playable_enemy_pokemon.stats.get('HP') <= 0:
                        player_level += 1  # Increase player level

                        # Reset player health after winning
                        playable_player_pokemon.stats["HP"] = playable_player_pokemon.max_hp

                        # Save game progress (this should happen before starting a new battle)
                        save_game(player_name, playable_enemy_pokemon.name, player_level)

                        # Fetch a new enemy for the next battle
                        pokemon_list = fetch_pokemon()
                        enemy_id = random.randint(0, 150)
                        playable_enemy_pokemon = Pokemon(
                            pokemon_list[enemy_id].get('id'),
                            pokemon_list[enemy_id].get('name'),
                            pokemon_list[enemy_id].get('sprite'),
                            pokemon_list[enemy_id].get('stats'),
                            pokemon_list[enemy_id].get('apiTypes'),
                            pokemon_list[enemy_id].get('apiResistances')
                        )
                        continue

                   
                        """# Update evolution if level allows it
                        evolution_stage = (player_level // 2)  # Determine evolution stage
                        evolved_pokemon = next((p for p in pokemon_choices if p['id'] == playable_player_pokemon.id + evolution_stage), None)
                        if evolved_pokemon:
                            print(f"🎉 {player_pokemon['name']} evolved into {evolved_pokemon['name']}!")
                            playable_player_pokemon = evolved_pokemon  # Update to evolved Pokémon

                        break  # Exit loop to load next enemy"""

                    if playable_player_pokemon.stats.get("HP") <= 0:
                        print(f"{playable_player_pokemon.name} is defeated! 💥")
                        draw_text(f"{playable_player_pokemon.name.capitalize()} is defeated!", WIDTH // 2, HEIGHT // 2)
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        return playable_enemy_pokemon  # Enemy wins

            pygame.time.delay(50)  # Delay for smoother movement

    return playable_player_pokemon  # Player wins if all enemies are defeated