from InquirerPy import inquirer
from source.services.service_utilisateur import UtilisateurService
from source.view.Page_option.menu_view import Menu_view
from source.view.session_view import Session


class Mode_invite_view:
    def display(self):
        print("Vous êtes connecté en mode invité")
    
    def make_choice(self):
        #Pas besoin de demander le type, nom, prénom, pseudo, mdp puisqu'il est anonyme
        #On crée juste l'identifiant aléatoire
        utilisateur_service = UtilisateurService()  # noqa: E999
        id_non_authentifie = utilisateur_service.creer_compte_anonyme() # On met rien dedans, juste crée un id aléatoire (unique ?) 

        Session().user_id = id_non_authentifie

        return Menu_view()