from InquirerPy import inquirer
from source.view.couche2menu.recherche_stage_view import Recherche_Stage_View

class HistoriqueView:
    def __init__(self,id_historique):
        self.id_historique = id_historique

    def display(self):
        # Récupère une liste de l'historique selon l'id_historique
        historique_courant = self.id_historique.get_historique()

        # Affiche une liste de choix pour sélectionner un Pokémon
        questions = [inquirer.List('select_stage', 'exit')]
        answers = inquirer.prompt(questions)

        if answers['choice'] == "select_stage":
            # Redirige vers la vue Stage avec un certain id
            return Recherche_Stage_View
    
        else:
            # Termine l'application
            return 'Exit'