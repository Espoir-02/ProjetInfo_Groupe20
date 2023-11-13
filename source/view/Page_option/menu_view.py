from InquirerPy import inquirer
from source.view.Page_option.recherche_stage_view import Recherche_Stage_View
from source.view.Page_option.historique_view import HistoriqueView
from source.view.Page_option.Liste_envie_view import Liste_envie_view 
from source.view.Page_option.proposition_prof_view import Proposition_prof_view
from source.view.Page_option.liste_eleves_view import ListeEleveView
from service.utilisateur_service import UtilisateurService  


class Menu_view:
    def __init__(self):
        self.utilisateur_service = UtilisateurService()

    def display(self, pseudo):
        type_utilisateur = self.utilisateur_service.get_type_utilisateur(pseudo)

        choices = ['Rechercher un stage', 'Accéder à son historique', 'Exit']

        if type_utilisateur in ['professeur', 'eleve', 'administrateur']:
            choices.append("Accéder à sa liste d'envie")
        
        if type_utilisateur == 'eleve':
            choices.append("Accéder à la liste de propositions du professeur")

        if type_utilisateur == 'professeur':
            choices.append("Accéder à la liste d'élèves")

        questions = [inquirer.List('choice', message='Choisir une option:', choices=choices)]

        answers = inquirer.prompt(questions)

        if answers['choice'] == 'Rechercher un stage':
            return Recherche_Stage_View().recherche_stage_view()
        
        elif answers['choice'] == 'Accéder à son historique':
            return HistoriqueView().historique_view()
        
        elif (type_utilisateur in ['professeur', 'eleve', 'administrateur']) and (answers['choice'] == "Accéder à sa liste d'envie"):
            return Liste_envie_view().liste_envie_view()
    
        elif (type_utilisateur == 'eleve') and (answers['choice'] == "Accéder à la liste de propositions du professeur"):
            return Proposition_prof_view().proposition_prof_view()

        elif (type_utilisateur == 'professeur') and (answers['choice'] == "Accéder à la liste d'élèves"):
            return ListeEleveView().liste_eleves_view()

        else:
            return 'Exit'
