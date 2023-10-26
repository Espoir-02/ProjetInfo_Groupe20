from stage import *

class detail_stage_view(AbstractView):
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
        
"Je m'appelle Enzo"