# battle.py
import random

class Battle:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def start(self):
        print(f"A battle begins between {self.pokemon1.name} and {self.pokemon2.name}!")

        while self.pokemon1.is_alive() and self.pokemon2.is_alive():
            # Determine turn order based on speed
            first, second = (self.pokemon1, self.pokemon2) if self.pokemon1.speed >= self.pokemon2.speed else (self.pokemon2, self.pokemon1)
            
            # Pokémon 1's turn
            move1 = first.choose_move()
            first.attack_opponent(second, move1)

            if second.is_alive():
                # Pokémon 2's turn
                move2 = second.choose_move()
                second.attack_opponent(first, move2)

        # Declare winner
        if self.pokemon1.is_alive():
            print(f"{self.pokemon1.name} wins!")
        else:
            print(f"{self.pokemon2.name} wins!")
