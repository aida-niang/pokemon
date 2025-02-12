from pokemon import Pokemon
from pokedex import Pokedex

class Combat:
    def __init__(self, joueur, adversaire, pokedex):
        self.joueur = joueur
        self.adversaire = adversaire
        self.pokedex = pokedex

    def attaquer(self):
        degats = max(0, self.joueur.attaque - self.adversaire.defense)
        self.adversaire.pv -= degats
        print(f"{self.joueur.nom} attaque {self.adversaire.nom} !")
        if self.adversaire.pv <= 0:
            print(f"{self.adversaire.nom} est KO ! {self.joueur.nom} gagne !")
            self.pokedex.ajouter_pokemon(self.adversaire)
