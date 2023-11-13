from source.dao.utilisateur_dao import UtilisateurDAO


class UtilisateurService:
    def __init__(self):
        self.utilisateur_dao = UtilisateurDAO()

    def verifier_identifiants(self, pseudo, mot_de_passe):
        if self.utilisateur_dao.check_pseudo_exists(pseudo):
            mot_de_passe_bdd = self.utilisateur_dao.find_mdp(pseudo)
            return mot_de_passe == mot_de_passe_bdd
        return False

    def get_type_utilisateur(self, pseudo):
        return self.utilisateur_dao.get_type_utilisateur(pseudo)

