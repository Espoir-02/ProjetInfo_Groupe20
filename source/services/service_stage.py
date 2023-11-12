from utilisateur_DAO import UtilisateurDAO
from utilitaire_DAO import UtilitaireDAO
from service_utilisateur import UtilisateurService
from source.business_object.stage_recherche.stage import StageBO
from source.business_object.utilisateur.utilisateur2 import UtilisateurBO

class StageService:
    def __init__(self, utilisateur_service: UtilisateurService, utilisateur_dao: UtilisateurDAO, 
    utilitaire_dao: UtilitaireDAO, source.business_object.stage_recherche.stage: StageBO,
    source.business_object.utilisateur.utilisateur2: UtilisateurBO )
        self.utilisateur_service = utilisateur_service
        self.utilisateur_dao = utilisateur_dao
        self.utilitaire_dao = utilitaire_dao
        self.StageBO = StageBO
        self.UtilisateurBO = UtilisateurBO

   