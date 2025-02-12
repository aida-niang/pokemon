import json

class Pokedex:
    def __init__(self):
        self.pokedex = self.charger_pokedex()

    def ajouter_pokemon(self, pokemon):
        if pokemon.nom not in self.pokedex:
            self.pokedex[pokemon.nom] = vars(pokemon)
            self.sauvegarder_pokedex()

    def sauvegarder_pokedex(self):
        with open("pokedex.json", "w") as file:
            json.dump(self.pokedex, file, indent=4)

    def charger_pokedex(self):
        try:
            with open("pokedex.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
