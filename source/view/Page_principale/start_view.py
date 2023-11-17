import random
import source.data # supposition pour l'instant, nom à changer selon Espoir
from source.view.Page_principale.connexion_view import ConnexionView
from source.view.Page_principale.create_account import CreationCompte_view
from source.view.Page_principale.mode_invite_view import Mode_invite_view
from InquirerPy import inquirer

# from source.business_object.utilisateur.  --> il faut importer une méthode vérification de connexion pour un utilisateur quelconque
        # cette méthode est dans la classe DatabaseUtilisateur

class Start_view:
    def __init__(self):
        self.__questions = [
            inquirer.List('choice', message='Choisissez une option:', choices=["Se connecter", "S'inscrire", "Continuer en mode invité"])
        ]

    def display(self):
        answers = inquirer.prompt(self.__questions)
        return self.make_choice(answers['choice'])

    def make_choice(self, choice):
        if choice == "Se connecter":
            return Connexion_view()

        elif choice == "S'inscrire":
            return CreationCompte_view()

        elif choice == "Continuer en mode invité":
            return Mode_invite_view()
