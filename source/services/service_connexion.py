from source.DAO.utilisateur_dao import UtilisateurDAO
from source.DAO.utilitaire_dao import UtilitaireDAO


class ConnexionService:
    def __init__(self):
        self.utilisateur_dao = UtilisateurDAO()

    def verifier_identifiants(self, pseudo, mot_de_passe):
        if UtilitaireDAO.check_pseudo_exists(pseudo):
            mot_de_passe_bdd = self.utilisateur_dao.find_mdp(pseudo)
            return mot_de_passe == mot_de_passe_bdd
        return False

    def get_type_utilisateur(self, pseudo):
        return self.utilisateur_dao.get_type_utilisateur(pseudo)
