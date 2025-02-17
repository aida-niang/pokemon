import pygame
import random
from utils import load_sprite
from settings import *

def draw_health_bar(x, y, health, max_health):
    bar_width = 150
    bar_height = 15
    fill = (health / max_health) * bar_width
    pygame.draw.rect(screen, RED, (x, y, bar_width, bar_height))
    pygame.draw.rect(screen, GREEN, (x, y, fill, bar_height))

def battle(player_pokemon, enemy_pokemon): #display pokemon battle
    player_health = 100  # Initialize player health
    enemy_health = 100  # Initialize enemy health
    running = True

    while running:
        screen.fill(WHITE)

        # Load Pokémon Sprites
        player_sprite = load_sprite(player_pokemon)
        enemy_sprite = load_sprite(enemy_pokemon)

        if player_sprite:
            player_sprite = pygame.transform.scale(player_sprite, (150, 150))
            screen.blit(player_sprite, (WIDTH // 4 - 75, HEIGHT // 2 - 75))

        if enemy_sprite:
            enemy_sprite = pygame.transform.scale(enemy_sprite, (150, 150))
            screen.blit(enemy_sprite, (3 * WIDTH // 4 - 75, HEIGHT // 2 - 75))

        # Display names
        draw_text(player_pokemon["name"].capitalize(), WIDTH // 4, HEIGHT - 100)
        draw_text(enemy_pokemon["name"].capitalize(), 3 * WIDTH // 4, HEIGHT - 100)

        # Draw health bars
        draw_health_bar(WIDTH // 4 - 75, HEIGHT - 130, player_health, 100)
        draw_health_bar(3 * WIDTH // 4 - 75, HEIGHT - 130, enemy_health, 100)

        draw_text("Press SPACE to Attack", WIDTH // 2, HEIGHT - 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Attaque
                    # Player's attack on enemy
                    damage = random.randint(15, 25)  # Random attack damage
                    enemy_health -= damage
                    print(f"{player_pokemon['name']} attacked! Enemy health: {enemy_health}")

                    if enemy_health <= 0:
                        print(f"{enemy_pokemon['name']} is defeated! 🎉")
                        draw_text(f"{enemy_pokemon['name'].capitalize()} is defeated!", WIDTH // 2, HEIGHT // 2)
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        running = False

                    # Enemy attacks
                    if enemy_health > 0:
                        damage = random.randint(15, 25)
                        player_health -= damage
                        print(f"Enemy {enemy_pokemon['name']} attacked! Player health: {player_health}")

                        if player_health <= 0:
                            print(f"{player_pokemon['name']} is defeated! 💥")
                            draw_text(f"{player_pokemon['name'].capitalize()} is defeated!", WIDTH // 2, HEIGHT // 2)
                            pygame.display.flip()
                            pygame.time.delay(2000)
                            running = False

        pygame.time.delay(500)  