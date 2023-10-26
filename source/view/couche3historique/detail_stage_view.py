from source.business_object.stage_recherche.stage import Stage
from source.view.abstract_view import AbstractView
from ListeEleveDAO import ListeEleves
from source.DAO.UtilisateurDAO import UtilisateurDAO
from InquirerPy import inquirer

class detail_stage_view_eleve(AbstractView):
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
        questions = [inquirer.List('choice', message='Choisir une option:', choices=['Retour en arrière', 'Quitter'])]
        answers = inquirer.prompt(questions)

        if answers['choice'] == 'Retour en arrière':
            # Retourne à la vue précédente
            return Liste_envie_view.liste_envie_view
        else:
            # Termine l'application
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
            # Accède à la liste de ses élèves
            id_prof = self.utilisateur_id
            liste_eleves = self.ListeEleveDAO.get_liste_eleve_by_id(id_prof)

            if liste_eleves:
                print("Liste d'élèves du professeur:", liste_eleves)
                # ici je ne sais pas si je fais une autre fenetre pour qu'il puisse choisir un eleve et lui proposer le stage
            else:
                print("La liste d'élèves est vide.")
        
        elif answers['choice'] == 'Retour en arrière':
            # Retourne à la vue précédente
            return Liste_envie_view.liste_envie_view
        else:
            # Termine l'application
            return 'Exit'
