from InquirerPy import inquirer
from source.services.service_utilisateur import ServiceUtilisateur
from source.view.Page_option.menu_view import Menu_view
from source.business_object.utilisateur.utilisateur2 import Utilisateur
from source.view.session_view import Session
import inquirer

class CreationCompte_view:

    def __init__(self):
        self.utilisateur_service = ServiceUtilisateur()

    def display(self):
        while True:
            questions = [
                inquirer.Text("nom", message="Nom:"),  
                inquirer.Text("prenom", message="Prénom:"),  
                inquirer.Text("pseudo", message="Pseudo:"),  
                inquirer.Password("mot_de_passe", message="Mot de passe:"),  # mdp caché
                inquirer.Password("confirmer_mot_de_passe", message="Confirmer le mot de passe:"),
                inquirer.List("type_utilisateur", message="Type utilisateur", choices=["administrateur", "professeur", "eleve"]),
                inquirer.Confirm("recommencer", message="Voulez-vous recommencer la saisie ?", default=False)
            ]

            answers = inquirer.prompt(questions, raise_keyboard_interrupt=True)

            if answers["recommencer"]:
                continue  # Si l'utilisateur veut recommencer, retourner au début de la boucle
            else :
                self.creer_compte(answers)

            

    def creer_compte(self, answers):
        nom = answers["nom"]
        prenom = answers["prenom"]
        pseudo = answers["pseudo"]
        mot_de_passe = answers["mot_de_passe"]
        confirmer_mot_de_passe = answers["confirmer_mot_de_passe"]
        type_utilisateur = answers["type_utilisateur"]

        if self.informations_obligatoires_remplies(nom, prenom, pseudo, mot_de_passe, confirmer_mot_de_passe, type_utilisateur):
            if self.nom_et_prenom_valides(nom, prenom):
                if self.pseudo_valide(pseudo):
                    if self.mots_de_passe_correspondent(mot_de_passe, confirmer_mot_de_passe):
                        utilisateur = Utilisateur(nom=nom, prenom=prenom, pseudo=pseudo, mot_de_passe=mot_de_passe, type_utilisateur=type_utilisateur)
                        nouvel_utilisateur = self.utilisateur_service.creer_utilisateur(utilisateur)

                        if nouvel_utilisateur:
                            Session().user_id = nouvel_utilisateur.id
                            Session().user_type = nouvel_utilisateur.type_utilisateur
                            Session().user_pseudo = nouvel_utilisateur.pseudo
                            print("Compte créé avec succès. ID de l'utilisateur :", nouvel_utilisateur.id)
                            return Menu_view().display()

        self.afficher_options_erreur_creation_compte()

    def informations_obligatoires_remplies(self, nom, prenom, pseudo, mot_de_passe, confirmer_mot_de_passe, type_utilisateur):
        if not (nom and prenom and pseudo and mot_de_passe and confirmer_mot_de_passe and type_utilisateur):
            print("Veuillez remplir toutes les informations obligatoires.")
            return False
        return True

    def nom_et_prenom_valides(self, nom, prenom):
        if not (nom.isalpha() and prenom.isalpha()):
            print("Le nom et le prénom doivent contenir uniquement des caractères alphabétiques.")
            return False
        return True

    def pseudo_valide(self, pseudo):
        if not pseudo.isalnum():
            print("Le pseudo ne doit contenir que des lettres et des chiffres.")
            return False
        return True

    def mots_de_passe_correspondent(self, mot_de_passe, confirmer_mot_de_passe):
        if mot_de_passe != confirmer_mot_de_passe:
            print("Les mots de passe ne correspondent pas.")
            return False
        return True

    def afficher_options_erreur_creation_compte(self):
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
            return Start_view().make_choice()

    def make_choice(self):
        return self.display()

if __name__ == "__main__":
    vue = CreationCompte_view()
    vue.display()
