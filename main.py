import pygame
from utils import load_pokemon, load_sprite

pygame.init()

# Load Pokémon
pokemon_list = load_pokemon()
current_index = 0
opponent_index = 1  # Assume an opponent exists at index 1 for simplicity

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokémon Battle")

def draw_pokemon_battle(index1, index2):
    """Displays both Pokémon on the screen during battle."""
    screen.fill((255, 255, 255))  # White background

    # Load the first Pokémon (attacker)
    pokemon1 = pokemon_list[index1]
    sprite1 = load_sprite(pokemon1)
    if sprite1:
        sprite1 = pygame.transform.scale(sprite1, (150, 150))  # Resize if needed
        screen.blit(sprite1, (WIDTH // 4 - 75, HEIGHT // 2 - 75))  # Left side for attacker

    # Load the second Pokémon (defender)
    pokemon2 = pokemon_list[index2]
    sprite2 = load_sprite(pokemon2)
    if sprite2:
        sprite2 = pygame.transform.scale(sprite2, (150, 150))  # Resize if needed
        screen.blit(sprite2, (3 * WIDTH // 4 - 75, HEIGHT // 2 - 75))  # Right side for defender

    # Display Pokémon names
    font = pygame.font.Font(None, 36)
    text1 = font.render(pokemon1["name"].capitalize(), True, (0, 0, 0))
    screen.blit(text1, (WIDTH // 4 - text1.get_width() // 2, HEIGHT - 100))

    text2 = font.render(pokemon2["name"].capitalize(), True, (0, 0, 0))
    screen.blit(text2, (3 * WIDTH // 4 - text2.get_width() // 2, HEIGHT - 100))

    pygame.display.flip()

# Game loop
running = True
while running:
    draw_pokemon_battle(current_index, opponent_index)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                current_index = (current_index + 1) % len(pokemon_list)
            elif event.key == pygame.K_LEFT:
                current_index = (current_index - 1) % len(pokemon_list)

pygame.quit()
