from InquirerPy import inquirer
from source.services.service_liste_envie import ListeEnvieService
from source.view.session_view import Session
from source.services.service_stage import StageService
from source.services.service_utilisateur import ServiceUtilisateur
from source.services.service_suggestion_eleve import ServiceSuggestion
import inquirer


class ListeEnvieView:
    def __init__(self, id_utilisateur):
        self.service_liste_envie = ListeEnvieService()
        self.stage_service = StageService()
        self.utilisateur_service = ServiceUtilisateur()
        self.suggestions_service = ServiceSuggestion()
        self.type_utilisateur = Session().user_type
        self.id_utilisateur = Session().user_id

    def afficher_menu(self):
        menu_options = [
            'Consulter la liste d\'envies',
            'Supprimer un stage de la liste',
            'Vider la liste d\'envie',
            'Revenir au menu principal'
        ]

        if (Session().user_type == 'professeur'):
            menu_options.append('Proposer un stage à partir de la liste d\'envies')

        return [
            inquirer.List('choix', message="Choisissez une option", choices=menu_options)
        ]

    def consulter_liste_envies(self):
        liste_envie_courant = self.service_liste_envie.get_liste_envie_eleve(self.id_utilisateur)

        if not liste_envie_courant:
            print("La liste d'envies est vide.")
        else:
            choix_stage = [f"{envie['id_stage']} - {envie['titre']}" for envie in liste_envie_courant] + ["Retour au menu"]
            questions = [inquirer.List('selection', message='Sélectionner un stage:', choices=choix_stage)]
            answers = inquirer.prompt(questions)

            selected_stage = int(answers['selection'].split(' - ')[0])# Pour récupérer l'ID du stage sélectionné

            if selected_stage == "Retour au menu":
                self.display()
            else:
                stage =self.stage_service.find_stage_by_id(selected_stage)
                print(stage)
                
    def proposer_stage(self):
        liste_envie_courant = self.service_liste_envie.get_liste_envie_eleve(self.id_utilisateur)

        if not liste_envie_courant:
            print("La liste d'envies est vide.")
        else:
            choix_stage = [f"{envie['id_stage']} - {envie['titre']}" for envie in liste_envie_courant] + ["Retour au menu"]
            questions = [inquirer.List('selection', message='Sélectionner le stage à suggérer:', choices=choix_stage)]
            answers = inquirer.prompt(questions)

            selected_stage = int(answers['selection'].split(' - ')[0])# Pour récupérer l'ID du stage sélectionné

            if selected_stage == "Retour au menu":
                self.display()
            else:
                try :
                    nom_eleve =input("Entrez le nom de l'élève : ")
                    prenom_eleve = input("Entrez le prénom de l'élève :")
                    eleve= self.utilisateur_service.trouver_utilisateur_par_nom(nom_eleve, prenom_eleve)

                    if eleve is not None:
                        id_eleve = eleve.get("id_utilisateur")
                        self.suggestions_service.create_suggestion(id_eleve, selected_stage, self.id_utilisateur)
                    else:
                        print("Aucun utilisateur trouvé avec les nom et prénom spécifiés.")
                except UtilisateurInexistantError as e:
                    print(f"Erreur : {e}")


    def display(self):
        while True:
            reponse = inquirer.prompt(self.afficher_menu())
            choix = reponse['choix']

            if choix == 'Consulter la liste d\'envies':
                self.consulter_liste_envies()
            elif choix == 'Supprimer un stage de la liste':
                id_stage = int(input("Entrez l'ID du stage à supprimer : "))
                self.service_liste_envie.supprimer_stage_de_liste_envie(self.id_utilisateur, id_stage)
            elif choix == 'Vider la liste d\'envie':
                confirmation = inquirer.confirm(message="Êtes-vous sûr de vouloir vider la liste d'envies?")
                if confirmation:
                    self.service_liste_envie.vider_liste_envie_eleve(self.id_utilisateur)
                else:
                    print("Opération annulée.")
            elif choix == 'Proposer un stage à partir de la liste d\'envies':
                self.proposer_stage()
            elif choix == 'Revenir au menu principal':
                break
            else:
                print("Option invalide. Veuillez réessayer.")


if __name__ == "__main__":
    id_utilisateur = Session().user_id
    liste_envie_view = ListeEnvieView(id_utilisateur=id_utilisateur)
    liste_envie_view.display()
