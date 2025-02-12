import pygame
import random
import json
from pokemon import Pokemon
from combat import Combat
from pokedex import Pokedex

pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon Battle")

# Chargement des Pokémon depuis un fichier JSON
def load_pokemons():
    with open("pokemon.json", "r") as file:
        return json.load(file)

pokemons_data = load_pokemons()
pokedex = Pokedex()


def main():
    running = True
    clock = pygame.time.Clock()
    

    player_pokemon = Pokemon.from_dict(random.choice(pokemons_data))
    enemy_pokemon = Pokemon.from_dict(random.choice(pokemons_data))
    
    combat = Combat(player_pokemon, enemy_pokemon, pokedex)
    
    while running:
        screen.fill((255, 255, 255))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    combat.attaquer()
        

        font = pygame.font.Font(None, 36)
        text = font.render(f"{player_pokemon.nom} VS {enemy_pokemon.nom}", True, (0, 0, 0))
        screen.blit(text, (WIDTH // 3, HEIGHT // 2))
        
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()

if __name__ == "__main__":
    main()
