from InquirerPy import inquirer
from source.view.couche2menu.menu_view import Menu_view

class Proposition_prof_view:
    def __init__(self,id_proposition):
        self.id_proposition = id_proposition
    
    def display(self):
        #Récupère la liste d'envies
        liste_envie_courant = self.id_historique.get_envie()

        #Affiche la liste d'envies
        print(liste_envie_courant)

        #Selectionner un stage en particulier dans la liste d'envies
        questions = [inquirer.List('selection_stage', message='Sélectionner un stage:', choices=liste_envie_courant)]
        answers = inquirer.prompt(questions)

        #Renvoie le pokemon sélectionné
        return 'Stage_detail_view', answers['selection_stage']