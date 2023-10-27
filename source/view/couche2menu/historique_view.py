from InquirerPy import inquirer
from source.view.couche2menu.recherche_stage_view import Recherche_Stage_View
from HistoriqueDAO import HistoriqueDAO



class HistoriqueView:
    def __init__(self,id_historique):
        self.id_historique = id_historique

    def display(self):
        historique_courant = self.id_historique.get_all_historique_by_id(self.id_historique)  
        # "Récupère l'historique de l'utilisateur actuel à partir de l'ID de l'historique"

        # Affiche une liste de choix pour sélectionner un stage
        choices = [f'Stage {stage["id_stage"]}' for stage in historique_courant]  
        choices.append('Exit') 

        questions = [inquirer.List('selectionner_votre_option', message='Choose a option:', choices=choices)]  # Prépare la question à poser à l'utilisateur
        answers = inquirer.prompt(questions)

        if answers['choice'] == "selectionner_votre_option":
            # Redirige vers la vue Stage avec un certain id
            return #### a mettre
    
        else:
            # Termine l'application
            return 'Exit'