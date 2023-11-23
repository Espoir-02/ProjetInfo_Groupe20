
from source.view.Page_principale.connexion_view import  ConnexionController
from source.view.Page_principale.create_account import CreationCompte_view
from source.view.Page_principale.mode_invite_view import Mode_invite_view
from InquirerPy import inquirer
import inquirer


class Start_view:
    def __init__(self):
        self.__questions = [
            inquirer.List('choice', message='Choisissez une option:', choices=["Se connecter", "S'inscrire", "Continuer en mode invité"])]


    def display(self):
        choice = inquirer.prompt(self.__questions)['choice']

        if choice == "Se connecter":
            return ConnexionController()

        elif choice == "S'inscrire":
            return CreationCompte_view()

        elif choice == "Continuer en mode invité":
            return Mode_invite_view()



    def make_choice(self):
        return self.display()
"""
from InquirerPy import prompt
from source.view.Page_principale.connexion_view import ConnexionController
from source.view.Page_principale.create_account import CreationCompte_view
from source.view.Page_principale.mode_invite_view import Mode_invite_view
from source.assets_graphiques.ascii import afficher_ascii_art


class Start_view:
    def __init__(self):
        self.__questions = [
            {
                'type': 'checkbox',
                'name': 'choice',
                'message': 'Choisissez une option:',
                'choices': [
                    "Se connecter",
                    "S'inscrire",
                    "Continuer en mode invité"
                ]
            }
        ]
    
    def display(self):
        afficher_ascii_art()
        
    def make_choice(self):
        answers = prompt(self.__questions)
        choices = answers['choice']

        for choice in choices:
            if choice == "Se connecter":
                return ConnexionController()
            elif choice == "S'inscrire":
                return CreationCompte_view()
            elif choice == "Continuer en mode invité":
                return Mode_invite_view()
            else:
                print("Option invalide. Veuillez réessayer.")"""