from source.DAO.HistoriqueDAO import HistoriqueDAO
from source.DAO.utilisateur_dao import UtilisateurDAO
from source.DAO.utilitaire_dao import UtilitaireDAO
from source.DAO.StageDAO import StageDAO
from prettytable import PrettyTable


class HistoriqueService:
    def __init__(self):
        self.historique_dao = HistoriqueDAO()
        self.utilitaire_dao = UtilitaireDAO()

    def get_all_historique_by_id(self, id_utilisateur):
        return self.historique_dao.get_all_historique_by_id(id_utilisateur)

    def ajouter_stage_a_historique(self, id_utilisateur, stage_id):
        return self.historique_dao.update_historique(id_utilisateur, stage_id)

    def vider_historique(self, id_utilisateur):
        if not self.utilitaire_dao.check_historique_exists(id_utilisateur):
            print("L'historique est déjà vide.")
            return False
        else:
            print("Historique supprimé avec succès.")
            success = self.historique_dao.delete_all_historique_by_id(id_utilisateur)
            return success
