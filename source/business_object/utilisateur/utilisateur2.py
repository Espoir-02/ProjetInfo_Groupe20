class Utilisateur:
    def __init__(self, nom, prenom, pseudo, mot_de_passe, type_utilisateur):
        self.nom = nom
        self.prenom = prenom
        self.pseudo = pseudo
        self.mot_de_passe = mot_de_passe
        self.type_utilisateur = type_utilisateur
        self.id = None  # L'ID sera attribué lors de la création du compte
