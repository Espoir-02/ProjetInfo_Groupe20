from source.DAO.utilisateur_dao import UtilisateurDAO
from source.DAO.StageDAO import StageDAO
from prettytable import PrettyTable


class ServiceAdmin:
    def __init__(self):
        self.utilisateur_dao = UtilisateurDAO()
        self.stage_dao = StageDAO()

    def supprimer_utilisateur(self, id_utilisateur):
        print("Utilisateur supprimé avec succès.")
        return self.utilisateur_dao.delete_utilisateur(id_utilisateur)
        

    def obtenir_liste_utilisateurs(self):
        liste = self.utilisateur_dao.get_all_utilisateurs()
        if liste:
            table = PrettyTable()
            table.field_names = ["ID Utilisateur", "Nom", "Prénom", "Pseudo", "Mot de passe", "Type Utilisateur"]

            for utilisateur in liste:
                table.add_row([
                    utilisateur["id_utilisateur"],
                    utilisateur["nom"],
                    utilisateur["prenom"],
                    utilisateur["pseudo"],
                    utilisateur["mot_de_passe"],
                    utilisateur["type_utilisateur"]
                ])

            print(table)
        else:
            print("La liste d'utilisateurs est vide.")
    

    def supprimer_stage(self, id_stage):
        print("Stage supprimé avec succès")
        return self.stage_dao.delete_stage(id_stage)
        

    def obtenir_liste_stages(self):
        liste = self.stage_dao.get_all_stages()
        print(liste)
