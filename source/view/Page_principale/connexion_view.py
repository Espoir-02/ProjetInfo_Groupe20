from InquirerPy import inquirer
from source.view.couche2menu.menu_view import Menu_view
from source.services.service_utilisateur import UtilisateurService


class ConnexionView:
    def demander_pseudo_mot_de_passe(self):
        pseudo = input("Entrez votre pseudo : ")
        mot_de_passe = input("Entrez votre mot de passe : ")
        return pseudo, mot_de_passe

    def afficher_message(self, message):
        print(message)


class ConnexionController:
    def __init__(self):
        self.utilisateur_service = UtilisateurService()
        self.connexion_view = ConnexionView()

    def display(self):
        while True:
            pseudo, mot_de_passe = self.connexion_view.demander_pseudo_mot_de_passe()

            if self.utilisateur_service.verifier_identifiants(pseudo, mot_de_passe):
                self.connexion_view.afficher_message("Connexion réussie!")
                self.gerer_connexion_reussie(pseudo)
                break
            else:
                self.connexion_view.afficher_message("Identifiants incorrects. Veuillez réessayer.")

    def gerer_connexion_reussie(self, pseudo):
        type_utilisateur = self.utilisateur_service.get_type_utilisateur(pseudo)
        menu_view = Menu_view()
        result = menu_view.display(type_utilisateur)

        if result == 'Exit':
            print("L'application se termine.")
        else:
            print(f"Redirection vers {result}...")

if __name__ == "__main__":
    connexion_controller = ConnexionController()
    connexion_controller.display()