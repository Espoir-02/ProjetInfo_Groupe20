from InquirerPy import inquirer
from source.view.Page_option.menu_view import Menu_view
from source.services.service_utilisateur import ServiceUtilisateur
from source.services.service_connexion import ConnexionService
from source.view.session_view import Session

class ConnexionView:
    def demander_pseudo_mot_de_passe(self):
        pseudo = input("Entrez votre pseudo : ")
        mot_de_passe = input("Entrez votre mot de passe : ")
        return pseudo, mot_de_passe

    def afficher_message(self, message):
        print(message)


class ConnexionController:
    def __init__(self):
        self.utilisateur_service = ServiceUtilisateur()
        self.connexion_service = ConnexionService()
        self.connexion_view = ConnexionView()

    def display(self):
        print("Bienvenue sur la page de connexion")
        while True:
            pseudo, mot_de_passe = self.connexion_view.demander_pseudo_mot_de_passe()

            if self.connexion_service.verifier_identifiants(pseudo, mot_de_passe):
                self.connexion_view.afficher_message("Connexion réussie!")
                self.gerer_connexion_reussie(pseudo)
                break
            else:
                self.connexion_view.afficher_message("Identifiants incorrects. Veuillez réessayer.")

    def gerer_connexion_reussie(self, pseudo):
        type_utilisateur = self.connexion_service.get_type_utilisateur(pseudo)

        Session().user_id = self.utilisateur_service.find_id_by_pseudo(pseudo)
        Session().user_type = type_utilisateur
        Session().user_pseudo = pseudo

        menu_view = Menu_view()
        result = menu_view.display(type_utilisateur)

    

        if result == 'Exit':
            print("L'application se termine.")
        else:
            print(f"Redirection vers {result}...")

if __name__ == "__main__":
    connexion_controller = ConnexionController()
    connexion_controller.display()