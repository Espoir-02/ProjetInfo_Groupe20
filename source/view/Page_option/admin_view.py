from source.services.service_admin import ServiceAdmin


class AdminView:
    def __init__(self):
        self.admin_service = ServiceAdmin()

    def afficher_menu(self):
        print("1. Consulter la liste de tous les utilisateurs")
        print("2. Supprimer un utilisateur")
        print("3. Consulter la liste de tous les stages")
        print("4. Supprimer un stage")
        print("5. Quitter et revenir au menu principal")

    def executer(self):
        while True:
            self.afficher_menu()
            choix = input("Choisissez une option : ")

            if choix == "1":
                self.admin_service.obtenir_liste_utilisateurs()
            elif choix == "2":
                id_utilisateur = int(
                    input("Entrez l'ID de l'utilisateur à supprimer : ")
                )
                self.admin_service.supprimer_utilisateur(id_utilisateur)
            elif choix == "3":
                self.admin_service.obtenir_liste_stages()
            elif choix == "4":
                id_stage = int(input("Entrez l'ID du stage à supprimer : "))
                self.admin_service.supprimer_stage(id_stage)
            elif choix == "5":
                print("Retour au menu principal !")
                from source.view.Page_option.menu_view import Menu_view
                return Menu_view()
                # Pas sur que ça fonctionne. A priori besoin du pseudo pour repasser sur le menu principal
                break
            else:
                print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    vue_admin = AdminView()
    vue_admin.executer()