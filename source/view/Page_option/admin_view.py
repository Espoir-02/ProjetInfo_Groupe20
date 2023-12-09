from source.services.service_admin import ServiceAdmin
from inquirer import prompt, List
import inquirer


class AdminView:
    def __init__(self):
        self.admin_service = ServiceAdmin()

    def afficher_menu(self):
        return [
            List(
                "choix",
                message="Choisissez une option",
                choices=[
                    "Consulter la liste de tous les utilisateurs",
                    "Supprimer un utilisateur",
                    "Consulter la liste de tous les stages",
                    "Consulter la liste des stages signalés",
                    "Supprimer un stage",
                    "Quitter et revenir au menu principal",
                ],
            ),
        ]

    def supprimer_utilisateur(self):
        while True:
            id_utilisateur = input(
                "Entrez l'ID de l'utilisateur à supprimer (ou appuyez sur Entrée pour annuler) : "
            )

            if not id_utilisateur.strip():
                print("L'ID de l'utilisateur ne peut pas être vide.")
                return  # Annuler l'opération si l'ID est vide

            try:
                id_utilisateur = int(id_utilisateur)
                break  # Sortir de la boucle si la conversion en entier réussit
            except ValueError:
                print(
                    "L'ID de l'utilisateur doit être un nombre entier. Veuillez réessayer."
                )

        self.admin_service.supprimer_utilisateur(id_utilisateur)

    def choisir_signal(self, liste_signals):
        if not liste_signals:
            print("\nLa liste des stages signalés est vide.")
        else:
            choix_stage = [
                f"{signal['id_stage']} - {signal['titre']}"
                for signal in liste_signals
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

    def afficher_signal(self):
        liste_signals = self.admin_service.obtenir_stages_signal()

        selected_stage = self.choisir_signal(liste_signals)

        if selected_stage is not None:
            stage = next((signal for signal in liste_signals if signal['id_stage'] == selected_stage), None)
            if stage:
                print("Informations sur le stage signalé :")
                print(f"   ID du stage : {stage['id_stage']}")
                print(f"   Titre : {stage['titre']}")
                print(f"   Lien : {stage['lien']}")
                print(f"   ID de l'utilisateur : {stage['id_utilisateur']}")

                choix_options = [
                    "Supprimer le stage de la base de données",
                    "Retirer le stage de la liste des stages signalés",
                    "Retour"
                ]

                questions = [
                    inquirer.List(
                        "choix_option", message="Choisissez une option:", choices=choix_options
                    )
                ]

                reponse_options = inquirer.prompt(questions)
                choix_option = reponse_options["choix_option"]

                if choix_option == "Supprimer le stage de la base de données":
                    self.admin_service.supprimer_stage(selected_stage)
                    print(f"Le stage avec l'ID {selected_stage} a été supprimé de la base de données.")
                elif choix_option == "Retirer le stage de la liste des stages signalés":
                    self.admin_service.supprimer_signal(selected_stage)
                    print(f"Le stage avec l'ID {selected_stage} a été retiré de la liste des stages signalés.")
                else:
                    print("Opération annulée.")

    def supprimer_stage(self):
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

        self.admin_service.supprimer_stage(id_stage)

    def display(self):
        while True:
            reponse = prompt(self.afficher_menu())

            choix = reponse["choix"]

            if choix == "Consulter la liste de tous les utilisateurs":
                self.admin_service.obtenir_liste_utilisateurs()
            elif choix == "Supprimer un utilisateur":
                self.supprimer_utilisateur()
            elif choix == "Consulter la liste de tous les stages":
                self.admin_service.obtenir_liste_stages()
            elif choix== "Consulter la liste des stages signalés":
                self.afficher_signal()
            elif choix == "Supprimer un stage":
                self.supprimer_stage()
            elif choix == "Quitter et revenir au menu principal":
                print("Retour au menu principal !")
                from source.view.Page_option.menu_view import Menu_view

                menu_view = Menu_view()
                menu_view.display()
                break
            else:
                print("Option invalide. Veuillez réessayer.")


if __name__ == "__main__":
    vue_admin = AdminView()
    vue_admin.display()
