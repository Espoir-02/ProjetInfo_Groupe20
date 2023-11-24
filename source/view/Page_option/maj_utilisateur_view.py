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
                choices=[
                    "Modifier le pseudo",
                    "Modifier le mot de passe",
                    "Quitter et revenir au menu principal",
                ],
            ),
        ]

    def display(self):
        while True:
            reponse = prompt(self.afficher_menu())
            choix = reponse["choix"]

            if choix == "Modifier le pseudo":
                nouveau_pseudo = self.valider_pseudo()
                if nouveau_pseudo == "":
                    print("Modification du pseudo annulée. Retour au menu principal.")
                    continue
                else:
                    self.utilisateur_service.maj_pseudo(self.id, nouveau_pseudo)

            elif choix == "Modifier le mot de passe":
                nouveau_mdp = self.demander_nouveau_mdp()
                try:
                    self.utilisateur_service.maj_mdp(self.pseudo, nouveau_mdp)
                    print("Mot de passe mis à jour avec succès.")
                except ValueError as e:
                    print(f"Erreur lors de la modification du mot de passe : {e}")

            elif choix == "Quitter et revenir au menu principal":
                menu_view = Menu_view()
                menu_view.display()
                break

            else:
                print("Option invalide. Veuillez réessayer.")

    def demander_nouveau_mdp(self):
        while True:
            mdp1 = inquirer.password("Entrez le nouveau mot de passe : ")

            if not mdp1:
                print("Le mot de passe ne peut pas être vide. Veuillez réessayer.")
                continue

            if len(mdp1) < 8:
                print(
                    "Le mot de passe est trop court (au moins 8 caractères). Veuillez réessayer."
                )
                continue

            mdp2 = inquirer.password("Confirmez le nouveau mot de passe : ")

            if mdp1 == mdp2:
                return mdp1
            else:
                print("Les mots de passe ne correspondent pas. Veuillez réessayer.")

    def valider_pseudo(self):
        while True:
            nouveau_pseudo = input(
                "Entrez le nouveau pseudo (appuyez sur 'Entrée' pour quitter) : "
            )

            if nouveau_pseudo == "":
                return ""

            if not nouveau_pseudo.isalnum():
                print("Le pseudo ne doit contenir que des lettres et des chiffres.")
                continue
            else:
                return nouveau_pseudo


if __name__ == "__main__":
    pseudo = Session().user_pseudo
    vue_maj_utilisateur = MajUtilisateurView(pseudo=pseudo)
    vue_maj_utilisateur.display()
