from InquirerPy import inquirer
from source.services.service_utilisateur import ServiceUtilisateur
from source.view.Page_option.menu_view import Menu_view
from source.business_object.utilisateur.utilisateur2 import Utilisateur
from source.view.session_view import Session
import inquirer

class CreationCompte_view:

    def display(self):
        "Méthode récoltant les informations de l'utilisateur"
        # Les questions du formulaire InquirerPy
        questions = [
            inquirer.Text("nom", message="Nom:"),  
            inquirer.Text("prenom", message="Prénom:"),  
            inquirer.Text("pseudo", message="Pseudo:"),  
            inquirer.Password("mot_de_passe", message="Mot de passe:"), #mdp caché
            inquirer.List("type_utilisateur", message="Type utilisateur", choices=["administrateur", "professeur", "eleve"]),]

        answers = inquirer.prompt(questions, raise_keyboard_interrupt=True)

        # Appelez la méthode creer_compte avec les réponses de l'utilisateur pour créer le compte
        self.creer_compte(answers)

    def creer_compte(self, answers):
        # Récupérez les réponses aux questions du formulaire
        nom = answers["nom"]
        prenom = answers["prenom"]
        pseudo = answers["pseudo"]
        mot_de_passe = answers["mot_de_passe"]
        type_utilisateur = answers["type_utilisateur"] 

        if not (nom and prenom and pseudo and mot_de_passe and type_utilisateur):
            print("Veuillez remplir toutes les informations obligatoires.")
            return self.display()

        # Créez un objet Utilisateur avec les informations fournies par l'utilisateur
        utilisateur = Utilisateur(nom=nom, prenom=prenom, pseudo=pseudo, mot_de_passe=mot_de_passe, type_utilisateur=type_utilisateur)


        utilisateur_service = ServiceUtilisateur()

        nouvel_utilisateur = utilisateur_service.creer_utilisateur(utilisateur)

        if nouvel_utilisateur:
            Session().user_id = nouvel_utilisateur.id
            Session().user_type = nouvel_utilisateur.type_utilisateur
            Session().user_pseudo = nouvel_utilisateur.pseudo
            print("Compte créé avec succès. ID de l'utilisateur :" , nouvel_utilisateur.id)
            return Menu_view().display()

        else:
            choices = [
                "Réessayer",
                "Revenir au menu précédent"
            ]
            questions = [inquirer.List('choice', message='Choisir une option:', choices=choices)]

            answers = inquirer.prompt(questions)

            if answers['choice'] == 'Réessayer':
                vue = CreationCompte_view()
                return vue.display()
            elif answers['choice'] == "Revenir au menu précédent":
                from source.view.Page_principale.start_view import Start_view
                start_view=Start_view()
                return start_view.display()
            

    def make_choice(self):
        return self.display()

if __name__ == "__main__":
    vue = CreationCompte_view()
    vue.display()