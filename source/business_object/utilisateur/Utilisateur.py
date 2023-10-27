class Utilisateur:
    def __init__(self, nom, prenom, pseudo, mdp, type_utilisateur):
        self.nom = nom
        self.prenom = prenom
        self.pseudo = pseudo
        self.mdp = mdp
        self.type_utilisateur = type_utilisateur
        self.id = None  # L'ID sera attribué lors de la création du compte
