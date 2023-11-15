from source.business_object.stage_recherche.stage import Stage
from source.view.abstract_view import AbstractView
from source.DAO.ListeEleveDAO import ListeEleves
from source.DAO.utilisateur_dao import UtilisateurDAO
from source.DAO.SuggestionsDAO import SuggestionsDAO
from source.DAO.StageDAO import StageDAO
from source.view.Page_option.Liste_envie_view import Liste_envie_view
from source.view.Page_option.menu_view import Menu_view
from source.view.Page_option.proposition_prof_view import Proposition_prof_view 

from InquirerPy import inquirer

class detail_stage_view_invite(AbstractView):
    def __init__(self, stage):
        self.stage = stage


    def display(self, selection_stage):
        # Affiche les détails du stage sélectionné
        stage_details = self.stage.get_stage_details(stage_details)

        # Affiche les détails du stage et propose de retourner à la vue précédente
        print(f"Intitulé : {stage_details['nom']}")
        print(f"Durée: {stage_details['durée']}")
        print(f"Salaire: {stage_details['salaire']}")
        print(f"Type: {stage_details['type']}")
        print(f"Entreprise: {stage_details['entreprise']}")
        questions = [inquirer.List('choice', message='Choisir une option:', choices=['Retour au Menu', 'Quitter'])]
        answers = inquirer.prompt(questions)

        if answers['choice'] == 'Retour au Menu':
            # Retourne à la vue précédente
            return Menu_view()
        else:
            # Termine l'application
            return 'Exit'


class detail_stage_view_eleve(AbstractView):
    def __init__(self, stage):
        self.stage = stage

    def display(self, selection_stage):
        
        stage_details = self.stage.get_stage_details(stage_details)

       
        print(f"Intitulé : {stage_details['nom']}")
        print(f"Durée: {stage_details['durée']}")
        print(f"Salaire: {stage_details['salaire']}")
        print(f"Type: {stage_details['type']}")
        print(f"Entreprise: {stage_details['entreprise']}")
        questions = [inquirer.List('choice', message='Choisir une option:', choices=['Retour en arrière', 'Quitter'])]
        answers = inquirer.prompt(questions)

        if answers['choice'] == 'Retour en arrière':
            return Liste_envie_view().liste_envie_view()
        else:
            return 'Exit'

class detail_stage_view_prof(AbstractView):
    def __init__(self, stage):
        self.stage = stage

    def display(self, selection_stage):
        # Affiche les détails du stage sélectionné
        stage_details = self.stage.get_stage_details(stage_details)

        # Affiche les détails du Pokémon et propose de retourner à la vue précédente
        print(f"Intitulé : {stage_details['nom']}")
        print(f"Durée: {stage_details['durée']}")
        print(f"Salaire: {stage_details['salaire']}")
        print(f"Type: {stage_details['type']}")
        print(f"Entreprise: {stage_details['entreprise']}")
        questions = [inquirer.List('choice', message='Choisir une option:', choices=[
            'Proposer à mes élèves','Retour en arrière', 'Quitter'])]
        answers = inquirer.prompt(questions)

        if answers['choice'] == 'Proposer à mes élèves':
            return Proposition_prof_view(selection_stage)
       
        elif answers['choice'] == 'Retour en arrière':
            # Retourne à la vue précédente
            return Liste_envie_view.liste_envie_view
        else:
            # Termine l'application
            return 'Exit'