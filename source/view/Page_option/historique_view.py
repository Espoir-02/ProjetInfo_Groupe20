from InquirerPy import inquirer
from source.services.service_utilisateur import ServiceUtilisateur
from source.services.service_historique import HistoriqueService
from source.services.service_liste_envie import ListeEnvieService
from source.services.service_suggestion_eleve import ServiceSuggestion
from source.services.service_liste_eleves import ListeElevesService
from source.services.service_stage import StageService
from source.view.session_view import Session
from source.services.service_export import ExporteurStage
from source.exception.exceptions import UtilisateurInexistantError
import inquirer


class HistoriqueView:
    def __init__(self):
        self.historique_service = HistoriqueService()
        self.id_utilisateur = Session().user_id
        self.liste_envie_service = ListeEnvieService()
        self.liste_eleves_service = ListeElevesService()
        self.stage_service = StageService()
        self.export = ExporteurStage()
        self.suggestions_service = ServiceSuggestion()
        self.utilisateur_service = ServiceUtilisateur()
        self.type_utilisateur = Session().user_type

    def afficher_menu(self):
        menu_options = [
            "Consulter l'historique",
            "Vider l'historique",
            "Revenir au menu principal",
            "Exporter l'historique"
        ]

        return [
            inquirer.List(
                "choix", message="Choisissez une option", choices=menu_options
            )
        ]

    def choisir_stage(self, liste_historique_courant):
        if not liste_historique_courant:
            print("\n")
        else:
            choix_stage = [
                f"{historique['id_stage']} - {historique['titre']}"
                for historique in liste_historique_courant
            ] + ["Retour au menu"]
            questions = [
                inquirer.List(
                    "selection", message="Sélectionner un stage:", choices=choix_stage
                )
            ]
            answers = inquirer.prompt(questions)

            selected_stage_str = answers["selection"].split(" - ")[0]

            if selected_stage_str == "Retour au menu":
                self.display()
            else:
                selected_stage = int(selected_stage_str)
                return selected_stage

    def consulter_historique(self):
        liste_historique_courant = self.historique_service.get_all_historique_by_id(
            self.id_utilisateur
        )
        selected_stage = self.choisir_stage(liste_historique_courant)

        if selected_stage is not None:
            stage = self.stage_service.find_stage_by_id(selected_stage)
            print("Informations sur le stage :")
            print(f"   ID du stage : {stage['id_stage']}")
            print(f"   Titre : {stage['titre']}")
            print(f"   Lien : {stage['lien']}")
            print(f"   Domaine : {stage['domaine']}")
            print(f"   Salaire : {stage['salaire']}")
            print(f"   Date de publication : {stage['date_publication']}")
            print(f"   Période : {stage['periode']}")
            print(f"   Niveau d'études : {stage['niveau_etudes']}")
            print(f"   Entreprise : {stage['entreprise']}")
            print(f"   Lieu : {stage['lieu']}")

            menu_options = ["Retour au menu principal"]

            if self.type_utilisateur == "professeur":
                menu_options.insert(0, "Proposer ce stage à un élève")

            if self.type_utilisateur in ["eleve", "professeur", "administrateur"]:
                menu_options.insert(0, "Ajouter ce stage à votre liste d'envies")

            question = inquirer.List(
                "choix_option", message="Choisissez une option", choices=menu_options
            )
            answer = inquirer.prompt([question])

            selected_option = answer["choix_option"]

            if selected_option == "Ajouter ce stage à votre liste d'envies":
                self.liste_envie_service.ajouter_stage_a_liste_envie(
                    self.id_utilisateur, selected_stage
                )
                print("Le stage a été ajouté à votre liste d'envies.")
            elif selected_option == "Proposer ce stage à un élève":
                liste_eleves = self.liste_eleves_service.get_liste_eleves(
                    self.id_utilisateur
                )

                id_eleve = self.choisir_eleve_menu(liste_eleves)

                if id_eleve is not None:
                    self.suggestions_service.create_suggestion(
                        id_eleve, selected_stage, self.id_utilisateur
                    )
                    print(f"Le stage a été proposé à l'élève sélectionné.")
                else:
                    print("Aucun élève sélectionné.")
            elif selected_option == "Retour au menu principal":
                print("Retour au menu principal...")
            else:
                print("Option invalide. Veuillez réessayer.")
    
    def choisir_eleve_menu(self, liste_eleves):
        choix_eleve = [
            f"{eleve['nom']} {eleve['prenom']}" for eleve in liste_eleves
        ] + ["Retour au menu"]

        questions = [
            inquirer.List(
                "selection_eleve",
                message="Sélectionner un élève:",
                choices=choix_eleve
            )
        ]

        answers = inquirer.prompt(questions)
        selected_eleve_str = answers["selection_eleve"]

        if selected_eleve_str == "Retour au menu":
            return None
        else:
            selected_eleve = [eleve for eleve in liste_eleves if f"{eleve['nom']} {eleve['prenom']}" == selected_eleve_str][0]
            return selected_eleve["id_eleve"]

    def display(self):
        while True:
            reponse = inquirer.prompt(self.afficher_menu())
            choix = reponse["choix"]

            if choix == "Consulter l'historique":
                self.consulter_historique()
            elif choix == "Vider l'historique":
                self.historique_service.vider_historique(self.id_utilisateur)
            elif choix == "Revenir au menu principal":
                from source.view.Page_option.menu_view import Menu_view
                menu_view = Menu_view()
                return menu_view.display()
            elif choix == "Exporter l'historique":
                chemin_sortie = input("Entrez le chemin du fichier de sortie (ex. sortie.txt) : ")
                self.export.exporter_historique(self.id_utilisateur, chemin_sortie)
            else:
                print("Option invalide. Veuillez réessayer.")


if __name__ == "__main__":
    historique_view = HistoriqueView()
    historique_view.display()
