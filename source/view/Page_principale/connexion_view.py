from InquirerPy import inquirer
from source.services.service_utilisateur import ServiceUtilisateur
from source.services.service_connexion import ConnexionService
from source.view.Page_option.menu_view import Menu_view
from source.view.session_view import Session
import inquirer


class ConnexionView:
    def demander_pseudo_mot_de_passe(self):
        questions = [
            inquirer.Text("pseudo", message="Pseudo:"),
            inquirer.Password("mot_de_passe", message="Mot de passe:\n"),
        ]

        answers = inquirer.prompt(questions, raise_keyboard_interrupt=True)
        pseudo = answers["pseudo"]
        mot_de_passe = answers["mot_de_passe"]
        return pseudo, mot_de_passe

    def afficher_message(self, message):
        print(message)


class ConnexionController:
    MAX_TENTATIVES = 3  # Nombre maximum d'essais autorisés

    CHOIX_REESSAYER = "Réessayer\n"
    CHOIX_MENU_PRECEDENT = "Revenir au menu précédent\n"

    def __init__(self):
        self.utilisateur_service = ServiceUtilisateur()
        self.connexion_service = ConnexionService()
        self.connexion_view = ConnexionView()

    def display(self):
        print("Bienvenue sur la page de connexion")
        for tentative in range(self.MAX_TENTATIVES):
            pseudo, mot_de_passe = self.connexion_view.demander_pseudo_mot_de_passe()

            if self.connexion_service.verifier_identifiants(pseudo, mot_de_passe):
                self.connexion_view.afficher_message("Connexion réussie!\n")
                self.gerer_connexion_reussie(pseudo)
                return
            else:
                self.connexion_view.afficher_message("Identifiants incorrects.\n")
                choix = self.afficher_options_erreur_connexion()

                if choix == self.CHOIX_MENU_PRECEDENT:
                    # Sortir de la boucle, revenir au menu précédent.
                    from source.view.Page_principale.start_view import Start_view

                    Start_view().make_choice()

        self.connexion_view.afficher_message(
            "Nombre maximum d'essais atteint. Retour au menu précédent.\n"
        )
        from source.view.Page_principale.start_view import Start_view

        return Start_view().make_choice()

    def afficher_options_erreur_connexion(self):
        choices = [self.CHOIX_REESSAYER, self.CHOIX_MENU_PRECEDENT]
        questions = [
            inquirer.List("choice", message="Choisir une option:", choices=choices)
        ]
        answers = inquirer.prompt(questions)
        return answers["choice"]

    def gerer_connexion_reussie(self, pseudo):
        type_utilisateur = self.connexion_service.get_type_utilisateur(pseudo)

        Session().user_id = self.utilisateur_service.find_id_by_pseudo(pseudo)
        Session().user_type = type_utilisateur
        Session().user_pseudo = pseudo

        menu_view = Menu_view()
        menu_view.display()

    def make_choice(self):
        return self.display()


if __name__ == "__main__":
    connexion_controller = ConnexionController()
    connexion_controller.display()
