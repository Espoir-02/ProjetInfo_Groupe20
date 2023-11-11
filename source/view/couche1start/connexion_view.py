from InquirerPy import inquirer
from source.view.couche2menu.menu_view import Menu_view
from source.dao.utilisateur_dao import UtilisateurDAO


class ConnexionView:
    def demander_pseudo_mot_de_passe(self):
        pseudo = input("Entrez votre pseudo : ")
        mot_de_passe = input("Entrez votre mot de passe : ")
        return pseudo, mot_de_passe

    def afficher_message(self, message):
        print(message)


class ConnexionController:
    def __init__(self):
        self.utilisateur_dao = UtilisateurDAO()
        self.connexion_view = ConnexionView()

    def display(self):
        while True:
            # Demande le pseudo et le mot de passe à l'utilisateur
            pseudo, mot_de_passe = self.connexion_view.demander_pseudo_mot_de_passe()

            # Vérifie si le pseudo existe dans la base de données
            if self.utilisateur_dao.check_pseudo_exists(pseudo):
                mot_de_passe_bdd = self.utilisateur_dao.find_mdp(pseudo)

                if mot_de_passe == mot_de_passe_bdd:
                    self.connexion_view.afficher_message("Connexion réussie!")
                    # Redirection vers le menu principal
                    Menu_view().menu_view()
                    break
                else:
                    self.connexion_view.afficher_message(
                        "Mot de passe incorrect. Veuillez réessayer."
                    )
            else:
                self.connexion_view.afficher_message(
                    "Pseudo incorrect. Veuillez réessayer."
                )


if __name__ == "__main__":
    connexion_controller = ConnexionController()
    connexion_controller.display()
