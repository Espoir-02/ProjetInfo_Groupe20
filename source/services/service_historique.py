from source.DAO.HistoriqueDAO import HistoriqueDAO
from source.DAO.utilisateur_dao import UtilisateurDAO
from source.DAO.StageDAO import StageDAO

class HistoriqueService:
    def __init__(self):
        self.historique_dao = HistoriqueDAO()

    def get_all_historique_by_id(self, id_utilisateur):
        return self.historique_dao.get_all_historique_by_id(id_utilisateur)

    def ajouter_stage_a_historique(self, id_utilisateur,stage_id):
        return self.utilisateur_dao.update_historique(id_utilisateur, stage_id)
       
