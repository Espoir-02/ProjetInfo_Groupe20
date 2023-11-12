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

    def rechercher_stages_par_titre(self, titre):
     # Récupérer tous les stages (adaptez cela en fonction de la structure réelle de vos données)
    tous_les_stages_ids = [stage_id for stage_id in range(1, 1000)]  # Supposons que les stages ont des identifiants de 1 à 1000
    tous_les_stages = [self.stage_dao.find_stage_by_id(stage_id) for stage_id in tous_les_stages_ids]

    # Filtrer les stages par titre
    stages_trouves = [stage for stage in tous_les_stages if stage and titre.lower() in stage["titre"].lower()]

    return stages_trouves


    
