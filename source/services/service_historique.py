from source.DAO.HistoriqueDAO import HistoriqueDAO
from source.DAO.utilisateur_dao import UtilisateurDAO
from source.DAO.StageDAO import StageDAO
from prettytable import PrettyTable

class HistoriqueService:
    def __init__(self):
        self.historique_dao = HistoriqueDAO()

    def get_all_historique_by_id(self, id_utilisateur):
        return self.historique_dao.get_all_historique_by_id(id_utilisateur)

    def ajouter_stage_a_historique(self, id_utilisateur,stage_id):
        return self.historique_dao.update_historique(id_utilisateur, stage_id)

    def vider_historique(self, id_utilisateur):
        print("Historique supprimé avec succès")
        return self.historique_dao.delete_all_historique_by_id(id_utilisateur)
