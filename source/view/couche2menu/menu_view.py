from InquirerPy import inquirer
from recherche_stage_view import Recherche_Stage_View
from historique_view import HistoriqueView
from Liste_envie_view import Liste_envie_view 
from proposition_prof_view import Proposition_prof_view

class Menu_view:
    def display(self, type_utilisateur):
        # Affiche le menu principal
        choices = ['Rechercher un stage', 'Accéder à son historique', 'Exit']

        if type_utilisateur in ['professeur', 'eleve', 'administrateur']:
            choices.append("Accéder à sa liste d'envie")
        
        if type_utilisateur == 'eleve':
            choices.append("Accéder à la liste de proposition du professeur")

        questions = [inquirer.List('choice', message='Choose an option:', choices=choices)]

        answers = inquirer.prompt(questions)

        if answers['choice'] == 'Rechercher un stage':
            # Redirige vers la vue Stage
            return Recherche_Stage_View().recherche_stage_view()
        
        elif answers['choice'] == 'Accéder à son historique':
            # Redirige vers la vue Historique
            return HistoriqueView().historique_view()
        
        elif (type_utilisateur in ['professeur', 'eleve', 'administrateur']) and (answers['choice'] == "Accéder à sa liste d'envie"):
            # Redirige vers la vue Envies_View pour les utilisateurs authentifiés
            return Liste_envie_view().liste_envie_view()
    
        elif (type_utilisateur == 'eleve') and (answers['choice'] == "Accéder à la liste de proposition du professeur"):
            # Redirige vers la vue Liste de proposition du professeur
            return Proposition_prof_view().proposition_prof_view()

        else:
            # Termine l'application
            return 'Exit'