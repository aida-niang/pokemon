import pygame
import requests
import random
from io import BytesIO

pygame.init()

WIDTH, HEIGHT = 800, 600

WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokémon depuis API")

#api_url = "https://pokebuildapi.fr/api/v1/pokemon/Gruikui" # "https://pokeapi.co/api/v2/pokemon/pikachu"
#team_url = "https://pokebuildapi.fr/api/v1/random/team"
get_pokedex = "https://pokebuildapi.fr/api/v1/pokemon/generation/1"

response = requests.get(get_pokedex)
if response.status_code == 200:
    data = response.json()
    #data["encountered"] = True
    sprite_url = data[4]["sprite"]
    index_aleatoire = random.randint(0, len(data) - 1)
    ennemy_url = data[index_aleatoire]["sprite"]
else:
    print("Erreur lors de la récupération des données JSON")
    sprite_url = None

if sprite_url:
    image_response = requests.get(sprite_url)
    pokemon_sprite = pygame.image.load(BytesIO(image_response.content))
else:
    print("Impossible de charger le sprite")
    pokemon_sprite = None

if ennemy_url:
    image_ennemy_response = requests.get(ennemy_url)
    enemy_sprite = pygame.image.load(BytesIO(image_ennemy_response.content))
else:
    print("Impossible de charger le sprite")
    enemy_sprite = None

if pokemon_sprite:
    pokemon_sprite = pygame.transform.scale(pokemon_sprite, (250, 250)) 

if enemy_sprite:
    enemy_sprite = pygame.transform.scale(enemy_sprite, (250, 250))

margin_bottom = 140 
pokemon_x = 80 
pokemon_y = HEIGHT - (pokemon_sprite.get_height() + margin_bottom) if pokemon_sprite else 0

margin_top = 10
enemy_x = WIDTH - enemy_sprite.get_width() if enemy_sprite else WIDTH
enemy_y = margin_top

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    if pokemon_sprite:
        screen.blit(pokemon_sprite, (pokemon_x, pokemon_y))
    if enemy_sprite:
        screen.blit(enemy_sprite, (enemy_x, enemy_y))

    pygame.display.flip()

pygame.quit()
