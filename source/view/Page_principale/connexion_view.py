from InquirerPy import inquirer
from source.services.service_utilisateur import ServiceUtilisateur
from source.services.service_connexion import ConnexionService
from source.view.Page_option.menu_view import Menu_view
from source.view.session_view import Session
import inquirer
import getpass

class ConnexionView:
    def demander_pseudo_mot_de_passe(self):
        questions = [  
            inquirer.Text("pseudo", message="Pseudo:"),  
            inquirer.Password("mot_de_passe", message="Mot de passe:")] #mdp caché]

        answers = inquirer.prompt(questions, raise_keyboard_interrupt=True)
        pseudo = answers["pseudo"]
        mot_de_passe = answers["mot_de_passe"]
        return pseudo, mot_de_passe
         
    def afficher_message(self, message):
        print(message)

class ConnexionController:

    def __init__(self):
        self.utilisateur_service = ServiceUtilisateur()
        self.connexion_service = ConnexionService()
        self.connexion_view = ConnexionView()


    def display(self):
        print("Bienvenue sur la page de connexion")
        while True:
            pseudo, mot_de_passe = self.connexion_view.demander_pseudo_mot_de_passe()

            if self.connexion_service.verifier_identifiants(pseudo, mot_de_passe):
                self.connexion_view.afficher_message("Connexion réussie!")
                self.gerer_connexion_reussie(pseudo)
                return
            else:
                self.connexion_view.afficher_message("Identifiants incorrects.")
                choices = [
                "Réessayer",
                "Revenir au menu précédent"
            ]
            questions = [inquirer.List('choice', message='Choisir une option:', choices=choices)]

            answers = inquirer.prompt(questions)

            if answers['choice'] == 'Réessayer':
                connexion = ConnexionView()
                return connexion.demander_pseudo_mot_de_passe()
            elif answers['choice'] == "Revenir au menu précédent":
                from source.view.Page_principale.start_view import Start_view
                start_view=Start_view()
                return start_view.display()

    def gerer_connexion_reussie(self, pseudo):
        type_utilisateur = self.connexion_service.get_type_utilisateur(pseudo)

        Session().user_id = self.utilisateur_service.find_id_by_pseudo(pseudo)
        Session().user_type = type_utilisateur
        Session().user_pseudo = pseudo

        menu_view = Menu_view()
        menu_view.display()


    def make_choice(self):
        return self.display()

if __name__ == "__main__":
    connexion_controller = ConnexionController()
    connexion_controller.display()