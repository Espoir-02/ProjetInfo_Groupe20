class Utilisateur:
    def __init__(self, type_utilisateur, nom=None, prenom=None, pseudo=None, mot_de_passe=None):
        self.nom = nom
        self.prenom = prenom
        self.pseudo = pseudo
        self.mot_de_passe = mot_de_passe
        self.type_utilisateur = type_utilisateur
        self.id = None  # L'ID sera attribué lors de la création du compte
