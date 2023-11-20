#from utilisateur_DAO import UtilisateurDAO
#from source.DAO.utilitaire_dao import UtilitaireDAO
#from service_utilisateur import UtilisateurService
#from source.business_object.stage_recherche.stage import StageBO
#from source.business_object.utilisateur.utilisateur2 import UtilisateurBO
from source.DAO.StageDAO import StageDAO

class StageService:
    def __init__(self):
        self.stage_dao = StageDAO()

    def create_stage(self, stage):
        return self.stage_dao.create_stage(stage)

    def find_stage_by_id(self, id_stage):
        return self.stage_dao.find_stage_by_id(id_stage)

   