from InquirerPy import inquirer
from source.DAO.UtilisateurDAO import UtilisateurDAO

class CreateCompte_view:
    def display(self):
        # Demander le type :
        type = [inquirer.List('choice', message = 'En tant que:', choices=["Eleve","Professeur","Administrateur"])]
        answers_type = inquirer.prompt(type)

        # Demander le nom :
        nom = [inquirer.List('choice', message = 'Quel est ton nom:', choices=["Eleve","Professeur","Administrateur"])]
        answers_nom = inquirer.prompt(nom)

        # Demander le nom en utilisant une question de type 'input':
        nom = [inquirer.Text('nom', message='Quel est ton nom ?')]
        answers_nom = inquirer.prompt(nom)
        # Récupérer la réponse de l'utilisateur:
        nom_utilisateur = answers_nom['nom']

        # Demande le prénom :
        prenom = [inquirer.Text('prenom', message='Quel est ton prenom ?')]
        answers_prenom = inquirer.prompt(prenom)
        # Récupérer la réponse de l'utilisateur:
        prenom_utilisateur = answers_prenom['prenom']

        # Demander le pseudo :
        pseudo = [inquirer.Text('pseudo', message='Quel est ton pseudo ?')]
        answers_pseudo = inquirer.prompt(pseudo)
        # Récupérer la réponse de l'utilisateur:
        pseudo_utilisateur = answers_pseudo['pseudo']

        # Demander le mot de passe :
        mdp = [inquirer.Text('mdp', message='Quel est ton mdp ?')]
        answers_mdp = inquirer.prompt(mdp)
        # Récupérer la réponse de l'utilisateur:
        mdp_utilisateur = answers_mdp['mdp']

        # Création de l'identifiant aléatoire :
        id_authentifie = UtilisateurDAO.create_compte(Utilisateur(type,nom_utilisateur,prenom_utilisateur,pseudo_utilisateur,mdp_utilisateur)) 
                # demander à Marc-Adrien pour relier Utilisateur et DAO (couche métier)
        
        return "Menu_view", id_authentifie