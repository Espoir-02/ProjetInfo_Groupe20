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
                          message="Choisissez une option",
                          choices=[
                              'Consulter la liste d\'envies',
                              'Supprimer un stage de la liste',
                              'Vider la liste d\'envie',
                              'Revenir au menu principal'
                          ])
        ]

    def consulter_liste_envies(self):
        liste_envie_courant = self.service_liste_envie.get_liste_envie_eleve(self.id_eleve)

        if not liste_envie_courant:
            print("La liste d'envies est vide.")
        else:
            choix_stage = [envie['id_stage'] for envie in liste_envie_courant] + ["Retour au menu"]
            selected_stage = inquirer.select(
                message='Sélectionner un stage:',
                choices=choix_stage
            ).execute()

            if selected_stage == "Retour au menu":
                self.display()
            else:
                if Session().user_type == "eleve":
                    detail_stage_view_eleve(selected_stage)
                else:
                    detail_stage_view_prof(selected_stage)

    def display(self):
        while True:
            reponse = inquirer.prompt(self.afficher_menu())
            choix = reponse['choix']

            if choix == 'Consulter la liste d\'envies':
                self.consulter_liste_envies()
            elif choix == 'Supprimer un stage de la liste':
                id_stage = int(input("Entrez l'ID du stage à supprimer : "))
                self.service_liste_envie.supprimer_stage_de_liste_envie(self.id_eleve, id_stage)
            elif choix == 'Vider la liste d\'envie':
                confirmation = inquirer.confirm(message="Êtes-vous sûr de vouloir vider la liste d'envies?")
                if confirmation:
                    self.service_liste_envie.vider_liste_envie_eleve(self.id_eleve)
                else:
                    print("Opération annulée.")
            elif choix == 'Revenir au menu principal':
                break
            else:
                print("Option invalide. Veuillez réessayer.")


if __name__ == "__main__":
    id_eleve = Session().user_id
    liste_envie_view = ListeEnvieView(id_eleve=id_eleve)
    liste_envie_view.display()
