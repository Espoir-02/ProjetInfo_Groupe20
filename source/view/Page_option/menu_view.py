from source.view.Page_option.recherche_stage_view import Recherche_Stage_View
from source.view.Page_option.historique_view import HistoriqueView
from source.view.Page_option.Liste_envie_view import Liste_envie_view 
from source.view.Page_option.proposition_prof_view import Proposition_prof_view
from source.view.Page_option.suggestions_eleve_view import SuggestionEleveView
from source.view.Page_option.liste_eleves_view import ListeElevesView
from source.services.service_utilisateur import UtilisateurService  
from source.view.Page_option.admin_view import AdminView
from source.view.session_view import Session 
import inquirer

class Menu_view:
    def __init__(self):
        self.utilisateur_service = UtilisateurService()

    def display(self):
        """pseudo = Session().user_pseudo
        type_utilisateur = Session().user_type
        id_professeur= Session().user_id
        id_eleve = Session().user_id
        """

        while True:

            choices = ['Rechercher un stage', 'Accéder à son historique', 'Exit']

            if Session().user_type in ['professeur', 'eleve', 'administrateur']:
                choices.append("Accéder à sa liste d'envie")
        
            if Session().user_type == 'eleve':
                choices.append("Accéder à la liste de propositions du professeur")

            if Session().user_type == 'professeur':
                choices.append("Accéder à la liste d'élèves")

            if Session().user_type == 'administrateur':
                choices.append("Accéder aux fonctions administrateur")

            questions = [inquirer.List('choice', message='Choisir une option:', choices=choices)]

            answers = inquirer.prompt(questions)

            if answers['choice'] == 'Rechercher un stage':
                return Recherche_Stage_View().display()
        
            elif answers['choice'] == 'Accéder à son historique':
                return HistoriqueView().display()

            elif (Session().user_type in ['professeur', 'eleve', 'administrateur']) and (answers['choice'] == "Accéder à sa liste d'envie"):
                liste_envie_view= Liste_envie_view()
                return liste_envie_view.display()
    
            elif (Session().user_type == 'eleve') and (answers['choice'] == "Accéder à la liste de propositions du professeur"):
                return Proposition_prof_view()

            elif (Session().user_type  == 'eleve') and (answers['choice'] == "Accéder à la liste de suggestions du professeur"):
                suggestions_view = SuggestionEleveView(id_eleve)
                return suggestions_view.display()


            elif (Session().user_type == 'professeur') and (answers['choice'] == "Accéder à la liste d'élèves"):
                liste_eleves_view = ListeElevesView(id_professeur)
                return liste_eleves_view.display()

            elif(Session().user_type == 'administrateur') and (answers['choice']== 'Accéder aux fonctions administrateur'):
                admin_view= AdminView()
                return admin_view.display()

            else:
                return Menu_view()

    def make_choice(self):
        return self.display()

"""if __name__ == "__main__":
    connexion_menu = Menu_view()
    connexion_menu.display()"""