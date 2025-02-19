import json
import pygame
import random

class Pokemon:
    def __init__(self, id, name, sprite_url, stats, types, resistances, evolution=None):
        self.id = id
        self.name = name
        self.sprite_url = sprite_url
        self.stats = stats
        self.max_hp = stats.get("HP")
        self.types = types  
        self.resistances = resistances
        self.evolution = evolution  # List of possible evolutions
        self.normal_attack = {"name": "Attaque normale",
                              "strength": 20,
                              "type": "Normal",
                              "accuracy": 80}
        self.special_attack = {"name": "Attaque spéciale",
                               "strength": 35,
                               "type": "Plante",
                               "accuracy": 60}
        self.image = None  # Sprite image to be loaded
        self.xp = 0
        self.level = 1

    def load_sprite(self):
        """ Load sprite from URL or local path """
        try:
            self.image = pygame.image.load(self.sprite_url)
        except Exception as e:
            print(f"Error loading image: {e}")
            self.image = None

    def gain_xp(self, xp):
        """ Gain experience points """
        self.xp += xp
        while self.xp >= 100:  # Example level-up threshold
            self.xp -= 100
            self.level_up()

    def level_up(self):
        """ Handle leveling up and potential evolution """
        self.level += 1
        self.xp = 0  # Reset XP after leveling up
        print(f"{self.name} leveled up to level {self.level}!")
        if self.evolution and self.level >= self.evolution.get('level', 100):  # Check if evolution condition is met
            self.evolve()

    def evolve(self):
        """ Handle evolution logic """
        if self.evolution:
            self.name = self.evolution["name"]
            self.id = self.evolution["id"]
            self.stats = self.evolution["new_stats"]
            self.evolution = self.evolution.get("next_evolution", None)  # Set next evolution if available
            print(f"{self.name} evolved!")

    def attack_target(self, target, attack):
        """ Attack a target and apply damage """
        if random.randint(1, 100) > attack['accuracy']:
            print(f"{self.name} uses {attack['name']}, but the attack misses!")
            return
        
        attack_stat = self.stats['attack']
        defense_stat = target.stats['defense']
        base_damage = ((2 * attack_stat / (defense_stat + 1)) * attack['strength']) / 2
        
        type_multiplier = 1
        for resistance in target.resistances:
            if resistance['name'] == attack['type']:
                type_multiplier = resistance['damage_multiplier']
                break
        
        final_damage = max(1, int(base_damage * type_multiplier))  # Ensure at least 1 damage
        target.stats['HP'] -= final_damage
        target.stats['HP'] = max(0, target.stats['HP'])  # Avoid negative HP
        
        print(f"{self.name} uses {attack['name']} on {target.name}!")
        print(f"Damage dealt: {final_damage} (x{type_multiplier} due to resistances)")
        print(f"{target.name}'s remaining HP: {target.stats['HP']}")
        
        if target.stats['HP'] == 0:
            print(f"{target.name} is knocked out!")

def load_pokemon_from_json(file_path):
    """ Load Pokémon data from a JSON file """
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    pokemons = []
    for poke_data in data:
        # Create a Pokemon object for each entry in the JSON data
        pokemon = Pokemon(
            id=poke_data["id"],
            name=poke_data["name"],
            sprite_url=poke_data["sprite"],  # Sprite URL or local file
            stats=poke_data["stats"],
            types=[type_info["name"] for type_info in poke_data["apiTypes"]],
            resistances=poke_data.get("resistances", []),  # Assuming resistances in the JSON
            evolution=poke_data.get("apiEvolutions", None)
        )
        pokemons.append(pokemon)

    return pokemons
