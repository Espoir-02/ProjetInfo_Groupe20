from source.services.service_admin import ServiceAdmin
from inquirer import prompt, List


class AdminView:
    def __init__(self):
        self.admin_service = ServiceAdmin()

    def afficher_menu(self):
        return [
            List('choix',
                 message="Choisissez une option",
                 choices=[
                     'Consulter la liste de tous les utilisateurs',
                     'Supprimer un utilisateur',
                     'Consulter la liste de tous les stages',
                     'Supprimer un stage',
                     'Quitter et revenir au menu principal'
                 ]),
        ]

    def display(self):
        while True:
            reponse = prompt(self.afficher_menu())

            choix = reponse['choix']

            if choix == 'Consulter la liste de tous les utilisateurs':
                self.admin_service.obtenir_liste_utilisateurs()
            elif choix == 'Supprimer un utilisateur':
                id_utilisateur = int(input("Entrez l'ID de l'utilisateur à supprimer : "))
                self.admin_service.supprimer_utilisateur(id_utilisateur)
            elif choix == 'Consulter la liste de tous les stages':
                self.admin_service.obtenir_liste_stages()
            elif choix == 'Supprimer un stage':
                id_stage = int(input("Entrez l'ID du stage à supprimer : "))
                self.admin_service.supprimer_stage(id_stage)
            elif choix == 'Quitter et revenir au menu principal':
                print("Retour au menu principal !")
                menu_view = Menu_view()
                menu_view.display()
                break
            else:
                print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    vue_admin = AdminView()
    vue_admin.display()