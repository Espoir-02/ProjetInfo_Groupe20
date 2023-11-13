from InquirerPy import inquirer
from source.DAO.UtilisateurDAO import UtilisateurDAO
from menu_view import Menu_view

class Mode_invite_view:
    def display(self):
        # Pas besoin de demander le type, nom, prénom, pseudo, mdp puisqu'il est anonyme
        # On crée juste l'identifiant aléatoire :
        utilisateur_dao = UtilisateurDAO()
        id_non_authentifie = utilisateur_dao.create_compte(Utilisateur()) # on met rien dedans, juste crée un id aléatoire

        return Menu_view().menu_view(), id_non_authentifie