from source.DAO.utilisateur_dao import UtilisateurDAO
from source.DAO.StageDAO import StageDAO


class ServiceAdmin:
    def __init__(self):
        self.utilisateur_dao = UtilisateurDAO()
        self.stage_dao = StageDAO()

    def supprimer_utilisateur(self, id_utilisateur):
        return self.utilisateur_dao.delete_utilisateur(id_utilisateur)
        print("Utilisateur supprimé avec succès.")

    def obtenir_liste_utilisateurs(self):
        liste = self.utilisateur_dao.get_all_utilisateurs()
        print(liste)

    def supprimer_stage(self, id_stage):
        return self.stage_dao.delete_stage(id_stage)
        print("Stage supprimé avec succès")

    def obtenir_liste_stages(self):
        liste = self.stage_dao.get_all_stages()
        print(liste)
