import json
import pygame

class Pokemon:
    def __init__(self, id, name, sprite_url, stats, types, evolution=None):
        self.id = id
        self.name = name
        self.sprite_url = sprite_url
        self.stats = stats  # Dictionnaire contenant les stats du Pokémon
        self.types = types  # Liste des types
        self.evolution = evolution  # Liste des évolutions possibles
        self.image = None  # Sprite de l'image, à charger
        self.xp = 0
        self.level = 1

    def load_sprite(self):
        """ Charge l'image à partir du sprite URL """
        try:
            self.image = pygame.image.load(self.sprite_url)  # Charger l'image via URL ou fichier local
        except Exception as e:
            print(f"Erreur de chargement de l'image : {e}")
            self.image = None

    def gain_xp(self, xp):
        """ Gagne de l'expérience """
        self.xp += xp
        if self.xp >= 100:  # Exemple simple pour le niveau
            self.level_up()

    def level_up(self):
        """ Gère l'évolution du niveau """
        self.level += 1
        self.xp = 0  # Réinitialisation de l'XP après un niveau

def load_pokemon_from_json(file_path):
    """ Charge les Pokémon depuis un fichier JSON """
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    pokemons = []
    for poke_data in data:
        # Créer un objet Pokemon pour chaque Pokémon
        pokemon = Pokemon(
            id=poke_data["id"],
            name=poke_data["name"],
            sprite_url=poke_data["sprite"],  # URL du sprite à charger
            stats=poke_data["stats"],
            types=[type_info["name"] for type_info in poke_data["apiTypes"]],
            evolution=poke_data.get("apiEvolutions", [])
        )
        pokemons.append(pokemon)

    return pokemons
