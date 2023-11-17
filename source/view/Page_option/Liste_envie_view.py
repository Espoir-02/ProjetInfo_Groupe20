from source.business_object.listes.voeux import Voeux
from InquirerPy import inquirer
from source.services.service_liste_envie import ListeEnvieService
from source.view.session_view import Session
from source.view.Page_detail.detail_stage_view import detail_stage_view_eleve
from source.view.Page_detail.detail_stage_view import detail_stage_view_prof
import inquirer

class Liste_envie_view:
    def __init__(self):
        self.id_eleve = Session().user_id
        self.service_liste_envie= ListeEnvieService()

    def display(self):
        while True:
            # Proposer trois choix à l'utilisateur
            questions = [
                inquirer.List('menu', message='Que souhaitez-vous faire ?', choices=[
                    "Consulter la liste d'envies",
                    "Supprimer un stage de la liste",
                    "Revenir au menu principal"
                ])
            ]
            user_choice = inquirer.prompt(questions)['menu']

            if user_choice == "Consulter la liste d'envies":
                # Récupérer et afficher la liste d'envies
                liste_envie_courant = self.service_liste_envie.get_liste_envie_eleve(self.id_eleve)
                print(liste_envie_courant)
                # Demander à l'utilisateur de sélectionner un stage
                #self.select_stage()
            elif user_choice == "Supprimer un stage de la liste":
                id_stage = int(input("Entrez l'ID du stage à supprimer : "))
                self.service_liste_envie.supprimer_stage_de_liste_envie( self.id_eleve, id_stage)
                print("Stage supprimé avec succès")
            elif user_choice == "Revenir au menu principal":
                from source.view.Page_option.menu_view import Menu_view
                menu_view=Menu_view()
                menu_view.display()

    """def select_stage(self):
        # Récupérer la liste d'envies
        liste_envie_courant = self.service_liste_envie.get_liste_envie_eleve(self.id_eleve)

        # Sélectionner un stage en particulier dans la liste d'envies
        choix = [envie['id_stage'] for envie in liste_envie_courant] + ["Retour au menu"]
        questions = [inquirer.List('selection', message='Sélectionner un stage:', choices=choix)]
        answers = inquirer.prompt(questions)

        if answers['selection'] == "Retour au menu":
            liste_envie_view= Liste_envie_view(id_eleve)
            return liste_envie_view.display()
            
        else:
            if Session().user_type == "eleve":
                return detail_stage_view_eleve(answers['selection'])
            else:
                return detail_stage_view_prof(answers['selection'])"""

"""if __name__ == "__main__":
    id_eleve = Session().user_id
    liste_envie_view = Liste_envie_view(id_eleve=id_eleve)
    liste_envie_view.display()"""