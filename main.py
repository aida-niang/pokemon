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

pygame.quit()
