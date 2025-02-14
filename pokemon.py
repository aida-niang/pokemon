# pokemon.py
import random

class Pokemon:
    def __init__(self, name, types, hp, attack, defense, speed, moves):
        self.name = name
        self.types = types
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.moves = moves  # List of moves (each move is a dict with name, type, power, accuracy)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0

    def attack_opponent(self, opponent, move):
        # Calculate damage based on attack and defense, considering type effectiveness
        base_damage = (self.attack - opponent.defense) + move['power']
        # Apply type effectiveness
        damage = base_damage * self.type_effectiveness(opponent, move['type'])
        opponent.take_damage(damage)
        print(f"{self.name} used {move['name']}! It dealt {damage} damage to {opponent.name}.")

    def type_effectiveness(self, opponent, move_type):
        # This function checks if the attack type is super effective, not very effective, or neutral
        effectiveness_chart = {
            'Fire': {'Grass': 2, 'Water': 0.5, 'Fire': 1, 'Electric': 1},
            'Water': {'Fire': 2, 'Water': 1, 'Grass': 0.5, 'Electric': 1},
            'Electric': {'Water': 2, 'Fire': 1, 'Grass': 1, 'Electric': 1},
            'Grass': {'Fire': 0.5, 'Water': 2, 'Electric': 1, 'Grass': 1},
            # Add other types here...
        }
        
        effectiveness = 1  # Default neutral effectiveness
        for attack_type in self.types:
            if attack_type in effectiveness_chart and move_type in effectiveness_chart[attack_type]:
                effectiveness *= effectiveness_chart[attack_type].get(move_type, 1)

        return effectiveness

    def choose_move(self):
        # Choose a random move from the list (can be improved with AI or player input)
        return random.choice(self.moves)
