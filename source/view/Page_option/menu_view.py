from InquirerPy import inquirer
from source.view.Page_option.recherche_stage_view import Recherche_Stage_View
from source.view.Page_option.historique_view import HistoriqueView
from source.view.Page_option.Liste_envie_view import Liste_envie_view 
from source.view.Page_option.proposition_prof_view import Proposition_prof_view
from source.view.Page_option.liste_eleves_view import ListeElevesView
from source.services.service_utilisateur import UtilisateurService  
from source.view.Page_option.admin_view import AdminView
from source.view.session_view import Session 
import inquirer

class Menu_view:
    def __init__(self):
        self.utilisateur_service = UtilisateurService()

    def display(self):
        pseudo = Session().user_pseudo
        type_utilisateur = Session().user_type
        id_professeur= Session().user_id
        id_eleve = Session().user_id
        

        while True:

            choices = ['Rechercher un stage', 'Accéder à son historique', 'Exit']

            if type_utilisateur in ['professeur', 'eleve', 'administrateur']:
                choices.append("Accéder à sa liste d'envie")
        
            if type_utilisateur == 'eleve':
                choices.append("Accéder à la liste de propositions du professeur")

            if type_utilisateur == 'professeur':
                choices.append("Accéder à la liste d'élèves")

            if type_utilisateur== 'administrateur':
                choices.append("Accéder aux fonctions administrateur")

            questions = [inquirer.List('choice', message='Choisir une option:', choices=choices)]

            answers = inquirer.prompt(questions)

            if answers['choice'] == 'Rechercher un stage':
                return Recherche_Stage_View()
        
            elif answers['choice'] == 'Accéder à son historique':
                return HistoriqueView()

            elif (type_utilisateur in ['professeur', 'eleve', 'administrateur']) and (answers['choice'] == "Accéder à sa liste d'envie"):
                liste_envie_view= Liste_envie_view(id_eleve)
                print(id)
                return liste_envie_view.display()
    
            elif (type_utilisateur == 'eleve') and (answers['choice'] == "Accéder à la liste de propositions du professeur"):
                return Proposition_prof_view()

            elif (type_utilisateur == 'professeur') and (answers['choice'] == "Accéder à la liste d'élèves"):
                liste_eleves_view = ListeElevesView(id_professeur)
                return liste_eleves_view.display()

            elif(type_utilisateur == 'administrateur') and (answers['choice']== 'Accéder aux fonctions administrateur'):
                admin_view= AdminView()
                return admin_view.display()

            else:
                return Menu_view()

    def make_choice(self):
        return self.display()

if __name__ == "__main__":
    connexion_menu = Menu_view()
    connexion_menu.display()