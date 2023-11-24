from source.services.service_admin import ServiceAdmin
from inquirer import prompt, List


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
