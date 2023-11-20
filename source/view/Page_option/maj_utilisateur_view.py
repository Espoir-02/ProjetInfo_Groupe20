from source.services.service_utilisateur import ServiceUtilisateur
from source.view.session_view import Session
from source.view.Page_option.menu_view import Menu_view
from inquirer import prompt, List, Text
import inquirer


class MajUtilisateurView:
    def __init__(self, pseudo):
        self.pseudo = Session().user_id
        self.id = Session().user_id
        self.utilisateur_service = ServiceUtilisateur()

    def afficher_menu(self):
        return [
            List(
                "choix",
                message="Choisissez une option",
                choices=["Modifier le pseudo", "Modifier le mot de passe", "Quitter et revenir au menu principal"],
            ),
        ]

    def display(self):
        while True:
            reponse = prompt(self.afficher_menu())
            choix = reponse["choix"]

            if choix == "Modifier le pseudo":
                nouveau_pseudo = input("Entrez le nouveau pseudo : ")
                self.utilisateur_service.maj_pseudo(self.id, nouveau_pseudo)
                print("Pseudo mis à jour avec succès.")
            elif choix == "Modifier le mot de passe":
                nouveau_mdp = self.demander_nouveau_mdp()
                self.utilisateur_service.maj_mdp(self.pseudo, nouveau_mdp)
                print("Mot de passe mis à jour avec succès.")
            elif choix == "Quitter":
                menu_view = Menu_view()
                menu_view.display()
                break
                
            else:
                print("Option invalide. Veuillez réessayer.")

    def demander_nouveau_mdp(self):
        while True:
            mdp1 = inquirer.password("Entrez le nouveau mot de passe : ")
            if len(mdp1) >= 8:
                mdp2 = inquirer.password("Confirmez le nouveau mot de passe : ")

                if mdp1 == mdp2:
                    return mdp1
                else:
                    print("Les mots de passe ne correspondent pas. Veuillez réessayer.")
            else:
                print(
                    "Le mot de passe est trop court (au moins 8 caractères). Annulation de la modification du mot de passe."
                )
                return None


if __name__ == "__main__":
    pseudo = Session().user_pseudo
    vue_maj_utilisateur = MajUtilisateurView(pseudo=pseudo)
    vue_maj_utilisateur.display()
