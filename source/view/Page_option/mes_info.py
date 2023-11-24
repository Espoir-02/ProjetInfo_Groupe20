from source.view.session_view import Session
from source.services.service_utilisateur import ServiceUtilisateur
import inquirer

class MesInfos:
    def display(self):
        service = ServiceUtilisateur()
        nom,prenom = service.information(Session().user_id)
        print(f'Nom : {nom} \nPrénom : {prenom}')

        choices = ['Modifier mes informations', "Retour au menu"]
        questions = [inquirer.List('choice', message='Choisir une option:', choices=choices)]

        answers = inquirer.prompt(questions)

        if answers['choice'] == 'Modifier mes informations':
            from source.view.Page_option.maj_utilisateur_view import MajUtilisateurView
            maj_utilisateur_view = MajUtilisateurView(Session().user_pseudo)
            return maj_utilisateur_view.display()
        else:
            from source.view.Page_option.menu_view import Menu_view
            return Menu_view().display()


    def make_choice(self):
        return display()