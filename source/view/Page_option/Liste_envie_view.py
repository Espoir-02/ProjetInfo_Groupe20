from source.business_object.listes.voeux import Voeux
from InquirerPy import inquirer

class Liste_envie_view:
    def __init__(self,id_envie):
        self.id_envie = id_envie
    
    def display(self):
        #Récupère la liste d'envies
        liste_envie_courant = self.id_historique.get_proposition()

        #Affiche la liste d'envies
        print(liste_envie_courant)

        #Selectionner un stage en particulier dans la liste d'envies
        questions = [inquirer.List('selection_stage', message='Sélectionner un stage:', choices=liste_envie_courant)]
        answers = inquirer.prompt(questions)

        #Renvoie le pokemon sélectionné
        return , answers['selection_stage']