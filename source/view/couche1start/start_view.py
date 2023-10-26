from InquirerPy import inquirer
import random
from source.business_object.stage_recherche.recherche import Recherche
from source.DAO.UtilisateurDAO import UtilisateurDAO
from source.business_object.listes.historique import Historique
from source.view.couche2menu.recherche_stage_view import Recherche_Stage_View
from source.business_object.Base_de_donnees import DatabaseUtilisateur # supposition pour l'instant, nom à changer selon Espoir
# from source.business_object.utilisateur.  --> il faut importer une méthode vérification de connexion pour un utilisateur quelconque
        # cette méthode est dans la classe DatabaseUtilisateur

class Start_view:
    def display(self):
        # Propose à l'utilisateur de se connecter
        questions = [inquirer.List('choice', message = 'Choose an option:', choices=["Se connecter","S'inscrire","Continuer en mode invité"])]
        answers = inquirer.prompt(questions)

        if answers['choice'] == "Se connecter":
            # Redirige vers la vue Connexion
            return "Connexion_view"
        
        elif answers['choice'] == "S'inscrire":
            # Redirige vers la vue Inscription
            return 'CreateCompte_view'
    
        elif answers['choice'] == "Continuer en mode invité":
            # Redirige vers la vue Continuer en mode invité
            return 'Mode_invite_view'