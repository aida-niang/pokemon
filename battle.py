import pygame
import random
from utils import load_sprite, pokemon_choices
from settings import *
from save_manager import save_game, get_player_level

background = pygame.image.load('assets/background/bg1.jpg')

def draw_health_bar(x, y, health, max_health):
    """Draws a health bar for Pokémon."""
    bar_width = 150
    bar_height = 15
    fill = (health / max_health) * bar_width
    pygame.draw.rect(screen, RED, (x, y, bar_width, bar_height))
    pygame.draw.rect(screen, GREEN, (x, y, fill, bar_height))

def battle(player_pokemon, enemy_pokemon_list, player_name):
    """Simulates a Pokémon battle with movement and multiple enemies."""
    player_health = 100  # Initialize player health
    enemy_index = 0  # Track the current enemy Pokémon
    player_level = get_player_level(player_name)  # Load the player's level

    # Player Pokémon position
    player_x = WIDTH // 4 - 75
    player_y = HEIGHT // 2 - 75
    speed = 10  # Speed of movement

    running = True
    while running:
        # Get the current enemy Pokémon
        if enemy_index >= len(enemy_pokemon_list):
            print("🎉 You defeated all enemies! You win!")
            draw_text("You defeated all enemies!", WIDTH // 2, HEIGHT // 2)
            pygame.display.flip()
            pygame.time.delay(2000)
            break  # Exit battle loop

        enemy_pokemon = enemy_pokemon_list[enemy_index]
        enemy_health = 100  # Reset enemy health for each new Pokémon
        player_health = 100  # Reset player health at the start of each fight

        # Load evolved Pokémon if the player is level 5 
        if player_level == 5:
            evolved_pokemon = next((p for p in pokemon_choices if p['name'] == player_pokemon['name']), None)
            if evolved_pokemon:
                print(f"🎉 {player_pokemon['name']} evolved into {evolved_pokemon['name']}!")
                player_pokemon = evolved_pokemon  
                player_sprite = load_sprite(player_pokemon)  
        else:
            player_sprite = load_sprite(player_pokemon)

        # Set random positions for player and enemy Pokémon to prevent overlap
        player_offset_x = random.randint(-50, 50)
        player_offset_y = random.randint(-50, 50)
        enemy_offset_x = random.randint(-50, 50)
        enemy_offset_y = random.randint(-50, 50)

        while enemy_health > 0 and player_health > 0:
            screen.fill(WHITE)

            # Load Pokémon Sprites
            player_sprite = load_sprite(player_pokemon)
            enemy_sprite = load_sprite(enemy_pokemon)

            if player_sprite:
                player_sprite = pygame.transform.scale(player_sprite, (150, 150))
                screen.blit(player_sprite, (player_x + player_offset_x, player_y + player_offset_y))

            if enemy_sprite:
                enemy_sprite = pygame.transform.scale(enemy_sprite, (150, 150))
                screen.blit(enemy_sprite, (3 * WIDTH // 4 - 75 + enemy_offset_x, HEIGHT // 2 - 75 + enemy_offset_y))

            # Display names
            draw_text(player_pokemon["name"].capitalize(), WIDTH // 4, HEIGHT - 100)
            draw_text(enemy_pokemon["name"].capitalize(), 3 * WIDTH // 4, HEIGHT - 100)

            # Draw health bars
            draw_health_bar(WIDTH // 4 - 75, HEIGHT - 130, player_health, 100)
            draw_health_bar(3 * WIDTH // 4 - 75, HEIGHT - 130, enemy_health, 100)

            draw_text(f"Level: {player_level}", WIDTH // 2, HEIGHT - 20)
            draw_text("Arrow Keys: Move | SPACE: Attack", WIDTH // 2, HEIGHT - 50)

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
                    elif event.key == pygame.K_SPACE:  # Attack action
                        damage = random.randint(15, 25)  # Random attack damage
                        enemy_health -= damage
                        print(f"{player_pokemon['name']} attacked! Enemy health: {enemy_health}")

                    if enemy_health <= 0:
                        print(f"{enemy_pokemon['name']} is defeated! 🎉")
                        player_level += 1  # Increment the player's level

                        # Reset player health to 100 after winning
                        player_health = 100

                        # Save game progress (save full Pokémon data instead of just name)
                        save_game(player_name, enemy_pokemon, player_level)

                        break  # Exit inner loop to load next enemy

                    # Enemy attacks back
                    damage = random.randint(15, 25)
                    player_health -= damage
                    print(f"Enemy {enemy_pokemon['name']} attacked! Player health: {player_health}")

                    if player_health <= 0:
                        print(f"{player_pokemon['name']} is defeated! 💥")
                        draw_text(f"{player_pokemon['name'].capitalize()} is defeated!", WIDTH // 2, HEIGHT // 2)
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        return enemy_pokemon  # Enemy wins

            pygame.time.delay(50)  # Reduce delay for smoother movement

    return player_pokemon  # Player wins if all enemies are defeated
