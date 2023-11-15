from source.business_object.listes.voeux import Voeux
from InquirerPy import inquirer
from service_liste_envie import ListeEnvieService
from session_view import Session
from detail_stage_view import detail_stage_view_eleve
from detail_stage_view import detail_stage_view_prof

class Liste_envie_view:
    def __init__(self,id):
        self.id = id
    
    def display(self):
        #Récupère la liste d'envies
        service_liste_envie = ListeEnvieService()
        liste_envie_courant = service_liste_envie.get_liste_envie_eleve(id)

        #Affiche la liste d'envies
        for envie in liste_envie_courant:
            print(f"{envie['titre']} - {envie['domaine']} - {envie['id_stage']}")

        #Selectionner un stage en particulier dans la liste d'envies
        choix = [envie['id_stage'] for envie in liste_envie_courant] + ["Retour au menu"]
        questions = [inquirer.List('selection', message='Sélectionner un stage:', choices=choix)]
        answers = inquirer.prompt(questions)

        if answer == "Retour au menu":
            # Retourner à la vue du menu principal
            return MenuView()
        else:
            if Session().user_type == "eleve":
                return detail_stage_view_eleve(answers)
            else:
                return detail_stage_view_prof(answers)