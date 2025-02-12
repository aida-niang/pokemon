class Pokemon:
    def __init__(self, nom, type_, pv, attaque, defense):
        self.nom = nom
        self.type_ = type_
        self.pv = pv
        self.attaque = attaque
        self.defense = defense

    @classmethod
    def from_dict(cls, data):
        return cls(data["nom"], data["type"], data["pv"], data["attaque"], data["defense"])