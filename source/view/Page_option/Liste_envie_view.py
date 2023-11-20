from source.business_object.listes.voeux import Voeux
from InquirerPy import inquirer
from source.services.service_liste_envie import ListeEnvieService
from source.view.session_view import Session
from source.view.Page_detail.detail_stage_view import detail_stage_view_eleve
from source.view.Page_detail.detail_stage_view import detail_stage_view_prof
import inquirer

class ListeEnvieView:
    def __init__(self, id_eleve):
        self.id_eleve = id_eleve
        self.service_liste_envie = ListeEnvieService()

    def afficher_menu(self):
        return [
            inquirer.List('choix',
                          message="Choississez une option",
                          choices=[
                              'Consulter la liste d\'envies',
                              'Supprimer un stage de la liste',
                              'Revenir au menu principal'
                          ])
        ]
 

    def display(self):
        while True:
            reponse = inquirer.prompt(self.afficher_menu())
            choix = reponse['choix']

            if choix == 'Consulter la liste d\'envies':
                self.service_liste_envie.get_liste_envie_eleve(self.id_eleve)
            elif choix == 'Supprimer un stage de la liste':
                id_stage = int(input("Entrez l'ID du stage à supprimer : "))
                self.service_liste_envie.supprimer_stage_de_liste_envie(self.id_eleve, id_stage)
            elif choix == 'Revenir au menu principal':
                print("Au revoir !")
                menu_view = Menu_view()
                menu_view.display()
                break
            else:
                print("Option invalide. Veuillez réessayer.")



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

if __name__ == "__main__":
    id_eleve = Session().user_id
    liste_envie_view = ListeEnvieView(id_eleve=id_eleve)
    liste_envie_view.display()