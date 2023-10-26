from InquirerPy import inquirer
from source.DAO.UtilisateurDAO import UtilisateurDAO

class CreateCompte_view:
    def display(self):
        # Demander le type :
        type = [inquirer.List('choice', message = 'En tant que:', choices=["Eleve","Professeur","Administrateur"])]
        answers_type = inquirer.prompt(type)

        # Demander le nom : à complèter

        # Demande le prénom : à complèter

        # Demander le pseudo : à complèter

        # Demander le mot de passe : à complèter

        # Création de l'identifiant aléatoire :
        id_authentifie = UtilisateurDAO.create_compte(Utilisateur(type,nom,prenom,pseudo,mdp)) # demander à Marc-Adrien pour relier Utilisateur et DAO (couche métier)
        
        return "Menu_view", id_authentifie