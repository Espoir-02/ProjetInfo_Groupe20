from source.services.service_suggestion_eleve import ServiceSuggestion
from source.services.service_stage import StageService
from source.services.service_historique import HistoriqueService
from source.services.service_liste_envie import ListeEnvieService
from source.view.session_view import Session
from source.services.service_export import ExporteurStage
from inquirer import prompt, List
import inquirer


class SuggestionEleveView:
    def __init__(self, id_eleve):
        self.id_eleve = id_eleve
        self.suggestions_eleves_service = ServiceSuggestion()
        self.stage_service = StageService()
        self.historique_service = HistoriqueService()
        self.liste_envie_service = ListeEnvieService()
        self.export = ExporteurStage()

    def afficher_menu(self):
        return [
            List(
                "choix",
                message="Choisissez une option",
                choices=[
                    "Consulter la liste de suggestions",
                    "Supprimer une suggestion",
                    "Vider la liste de suggestions",
                    "Exporter la liste de suggestions"
                    "Quitter et revenir au menu principal",
                ],
            ),
        ]

    def consulter_suggestions(self):
        try:
            liste_suggestions_courant = (
                self.suggestions_eleves_service.get_suggestions_by_id(self.id_eleve)
            )

            if not liste_suggestions_courant:
                print("La liste de suggestions est vide.")
            else:
                choix_stage = [
                    f"{suggestion['id_stage']} - {suggestion['titre']}"
                    for suggestion in liste_suggestions_courant
                ] + ["Retour au menu"]
                questions = [
                    inquirer.List(
                        "selection",
                        message="Sélectionner un stage:",
                        choices=choix_stage,
                    )
                ]
                answers = inquirer.prompt(questions)

                selected_stage_str = answers["selection"].split(" - ")[0]

                if selected_stage_str == "Retour au menu":
                    self.display()
                else:
                    selected_stage = int(selected_stage_str)
                    try:
                        stage = self.stage_service.find_stage_by_id(selected_stage)

                        if stage is not None:
                            self.historique_service.ajouter_stage_a_historique(
                                self.id_eleve, selected_stage
                            )
                            print("Informations sur le stage :")
                            print(f"   ID du stage : {stage['id_stage']}")
                            print(f"   Titre : {stage['titre']}")
                            print(f"   Lien : {stage['lien']}")
                            print(f"   Domaine : {stage['domaine']}")
                            print(f"   Salaire : {stage['salaire']}")
                            print(
                                f"   Date de publication : {stage['date_publication']}"
                            )
                            print(f"   Période : {stage['periode']}")
                            print(f"   Niveau d'études : {stage['niveau_etudes']}")
                            print(f"   Entreprise : {stage['entreprise']}")
                            print(f"   Lieu : {stage['lieu']}")

                            # Demander à l'utilisateur s'il souhaite ajouter le stage à sa liste d'envies
                            ajout_envie = inquirer.confirm(
                                message="Voulez-vous ajouter ce stage à votre liste d'envies?"
                            )
                            if ajout_envie:
                                self.liste_envie_service.ajouter_stage_a_liste_envie(
                                    self.id_eleve, selected_stage
                                )
                            else:
                                print(
                                    "Le stage n'a pas été ajouté à votre liste d'envies."
                                )
                        else:
                            print("Aucun stage trouvé avec l'ID spécifié.")
                    except Exception as e:
                        print(
                            f"Une erreur s'est produite lors de la recherche du stage : {e}"
                        )

        except Exception as e:
            print(
                f"Une erreur s'est produite lors de la récupération des suggestions : {e}"
            )

    def supprimer_suggestion(self):
        while True:
            id_stage = input(
                "Entrez l'ID du stage à supprimer (ou appuyez sur Entrée pour annuler) : "
            )

            if not id_stage.strip():
                print("L'ID du stage ne peut pas être vide.")
                return  # Annuler l'opération si l'ID est vide

            try:
                id_stage = int(id_stage)
                break  # Sortir de la boucle si la conversion en entier réussit
            except ValueError:
                print("L'ID du stage doit être un nombre entier. Veuillez réessayer.")

        self.suggestions_eleves_service.delete_suggestion(self.id_eleve, id_stage)

    def display(self):
        while True:
            reponse = prompt(self.afficher_menu())
            choix = reponse["choix"]

            if choix == "Consulter la liste de suggestions":
                self.consulter_suggestions()
                self.suggestions_eleves_service.get_suggestions_by_id(self.id_eleve)
            elif choix == "Supprimer une suggestion":
                self.supprimer_suggestion()
            elif choix == "Exporter la liste de suggestions":
                chemin_sortie = input("Entrez le chemin du fichier de sortie (ex. sortie.txt) : ")
                self.export.exporter_suggestions(self.id_eleve, chemin_sortie)
            elif choix == "Vider la liste de suggestions":
                confirmation = inquirer.confirm(
                    message="Êtes-vous sûr de vouloir vider la liste de suggestions ?"
                )
                if confirmation:
                    self.suggestions_eleves_service.vider_liste_suggestions(
                        self.id_eleve
                    )
                else:
                    print("Opération annulée.")
            elif choix == "Quitter et revenir au menu principal":
                print("Au revoir !")
                from source.view.Page_option.menu_view import Menu_view

                menu_view = Menu_view()
                return menu_view.display()
            else:
                print("Option invalide. Veuillez réessayer.")

    def make_choice(self):
        return self.display()


if __name__ == "__main__":
    id_eleve = Session().user_id
    suggestions_eleves = SuggestionEleveView(id_eleve=id_eleve)
    suggestions_eleves.display()
