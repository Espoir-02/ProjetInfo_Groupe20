from InquirerPy import inquirer
from source.DAO.utilisateur_dao import UtilisateurDAO
from source.view.couche2menu.menu_view import Menu_view
from source.business_object.utilisateur.utilisateur2 import Utilisateur

class CreationCompte_view:
    def creer_compte(self, answers):
        # Récupérez les réponses aux questions du formulaire
        nom = answers["nom"]
        prenom = answers["prenom"]
        pseudo = answers["pseudo"]
        mdp = answers["mdp"]
        type_utilisateur = answers["Type d'utilisateur"] # Remplacez par le type d'utilisateur approprié

        # Créez un objet Utilisateur avec les informations fournies par l'utilisateur
        utilisateur = Utilisateur(nom=nom, prenom=prenom, pseudo=pseudo, mdp=mdp, type_utilisateur=type_utilisateur)

        # Appelez la méthode create_compte de UtilisateurDAO pour créer le compte en base de données
        nouvel_utilisateur = UtilisateurDAO.create_compte(utilisateur)

        print("Compte créé avec succès. ID de l'utilisateur :", nouvel_utilisateur.id)
        return Menu_view().menu_view()

    def demande(self):
        # les questions du formulaire InquirerPy
        questions = [
            inquirer.Text("nom", message="Nom:"),  
            inquirer.Text("prenom", message="Prénom:"),  
            inquirer.Text("pseudo", message="Pseudo:"),  
            inquirer.Password("mdp", message="Mot de passe:"), #mdp caché
            inquirer.Text("type_utilisateur", message="Type utilisateur")]

        answers = inquirer.prompt(questions, raise_keyboard_interrupt=True)

        # Appelez la méthode creer_compte avec les réponses de l'utilisateur pour créer le compte
        self.creer_compte(answers)

if __name__ == "__main__":
    vue = CreationCompte_view()
    vue.demande()