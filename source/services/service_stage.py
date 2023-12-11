from source.DAO.utilitaire_dao import UtilitaireDAO
from source.DAO.StageDAO import StageDAO



class StageService:
    def __init__(self):
        self.stage_dao = StageDAO()
        self.utilitaire_dao = UtilitaireDAO()

    def create_stage(self, stage):
        return self.stage_dao.create_stage(stage)

    def find_stage_by_id(self, id_stage):
        return self.stage_dao.find_stage_by_id(id_stage)

    def signaler_stage(self, id_stage, id_utilisateur):
        return self.stage_dao.update_liste_signal(id_stage, id_utilisateur)

