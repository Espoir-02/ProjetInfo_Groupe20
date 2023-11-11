from InquirerPy import inquirer
from menu_view import Menu_view


# cette classe DatabaseUtilisateur est temporaire en attendant de faire le lien entre Utilisateur et la vue.
# cette classe permet de s'inscrire et de vérifier que pseudo et mdp sont bons
class DatabaseUtilisateur:
    def __init__(self):
        # Initialisez votre base de données ou connectez-vous à la base de données ici
        pass

    def verify_credentials(self, pseudo, mot_de_passe):
        # Recherchez dans votre base de données si les informations d'authentification sont correctes
        # Supposons que vous ayez une table `utilisateurs` avec des colonnes `pseudo` et `mot_de_passe`
        # Remplacez cela avec votre logique spécifique à votre base de données
        utilisateur = self.rechercher_utilisateur_dans_base_de_donnees(pseudo)

        # Si l'utilisateur n'est pas trouvé dans la base de données, retournez False
        if utilisateur is None:
            return False

        # Vérifiez si le mot de passe correspond
        if utilisateur["mot_de_passe"] == mot_de_passe:
            return True
        else:
            return False

    def rechercher_utilisateur_dans_base_de_donnees(self, pseudo):
        # Implémentez la recherche de l'utilisateur dans votre base de données ici
        # Recherchez l'utilisateur par pseudo dans votre table `utilisateurs`
        # Retournez None si l'utilisateur n'est pas trouvé, sinon retournez l'enregistrement de l'utilisateur
        pass


class Connexion_view:
    def __init__(self):
        self.database = (
            DatabaseUtilisateur()
        )  # Supposons que vous ayez une classe pour gérer la base de données des utilisateurs

    def display(self):
        while True:
            # Demande le pseudo et le mot de passe à l'utilisateur
            questions = [
                inquirer.Text("pseudo", message="Entrez votre pseudo:"),
                inquirer.Password("password", message="Entrez votre mot de passe:"),
            ]
            answers = inquirer.prompt(questions)

            # Vérifie les informations d'authentification dans la base de données
            pseudo = answers["pseudo"]
            password = answers["password"]
            if self.database.verify_credentials(pseudo, password):
                print("Connexion réussie!")
                # Redirige vers le menu principal
                return Menu_view().menu_view()
            else:
                print("Erreur d'authentification. Veuillez réessayer.")
