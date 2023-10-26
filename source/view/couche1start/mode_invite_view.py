from InquirerPy import inquirer
from source.DAO.UtilisateurDAO import UtilisateurDAO

class Mode_invite_view:
    def display(self):
        # Pas besoin de demander le type, nom, prénom, pseudo, mdp puisqu'il est anonyme
        # On crée juste l'identifiant aléatoire :
        id_non_authentifie = UtilisateurDAO.create_compte(Utilisateur()) # on met rien dedans, juste crée un id aléatoire

        return "Menu_view", id_non_authentifie