from source.DAO.utilisateur import UtilisateurDAO
from source.business_object.utilisateur.Utilisateur import Utilisateur

class UtilisateurService:
    def __init__(self):
        self.utilisateur_dao = UtilisateurDAO()

    def creer_compte(self, nom, prenom, pseudo, mot_de_passe, type_utilisateur):
        # Créer un nouvel utilisateur
        nouvel_utilisateur = Utilisateur(nom=nom, prenom=prenom, pseudo=pseudo, mot_de_passe=mot_de_passe, type_utilisateur=type_utilisateur)
        utilisateur_cree = self.utilisateur_dao.create_compte(nouvel_utilisateur)
        return utilisateur_cree

    def authentifier(self, pseudo, mot_de_passe):
        # Vérifier l'authentification de l'utilisateur
        mot_de_passe_utilisateur = self.utilisateur_dao.find_mdp(pseudo)
        if mot_de_passe_utilisateur and mot_de_passe == mot_de_passe_utilisateur:
            return True
        return False

    def recuperer_informations(self, pseudo):
        # Récupérer les informations de l'utilisateur
        utilisateur = self.utilisateur_dao.find_by_nom(pseudo)
        return utilisateur