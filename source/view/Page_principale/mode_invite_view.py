from InquirerPy import inquirer
from service_utilisateur import UtilisateurService
from menu_view import Menu_view
from session_view import Session


class Mode_invite_view:
    def display(self):
        # Pas besoin de demander le type, nom, prénom, pseudo, mdp puisqu'il est anonyme
        # On crée juste l'identifiant aléatoire :
        utilisateur_service = UtilisateurService()
        id_non_authentifie = utilisateur_service.creer_compte_anonyme() # On met rien dedans, juste crée un id aléatoire (unique ?) 

        Session().user_id = id_non_authentifie

        return Menu_view().menu_view(), id_non_authentifie