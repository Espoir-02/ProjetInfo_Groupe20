from source.DAO.ListeEnvieDAO import ListeEnvieDAO
from source.DAO.utilitaire_dao import UtilitaireDAO
from source.exception.exceptions import IdStageInexistantError
from prettytable import PrettyTable

class ListeEnvieService:
    def __init__(self):
        self.liste_envie_dao = ListeEnvieDAO()
        self.utilitaire_dao = UtilitaireDAO()

    def ajouter_stage_a_liste_envie(self, id_eleve, id_stage):
        if self.utilitaire_dao.check_envie_exists(id_eleve, id_stage):
            print("Le stage est déjà dans la liste d'envies.")
            return False
        else:
            print("Le stage a été ajouté à la liste d'envies avec succès.")
            success = self.liste_envie_dao.update_liste_envie(id_eleve, id_stage)
            return success 


    def supprimer_stage_de_liste_envie(self, id_eleve, id_stage):
        try:
            if not self.utilitaire_dao.check_stage_exists(id_stage):
                raise IdStageInexistantError(id_stage)

            succes = self.liste_envie_dao.delete_liste_envie(id_eleve, id_stage)
            if succes :
                print(f"Stages ID {id_stage} supprimé avec succès de la liste d'envie.")
            else:
                print("Erreur lors de la suppression de l'envie.")
        except IdStageInexistantError as e:
            print(f"Erreur lors de la suppression du stage dans la liste d'envie : {e}")



    def vider_liste_envie_eleve(self, id_eleve):
        if not self.utilitaire_dao.check_liste_envie_exists(id_eleve):
            print("La liste d'envie est déjà vide.")
            return False
        else :
            print("Liste d'envie vidée avec succès")
            succes = self.liste_envie_dao.delete_all_liste_envie(id_eleve)
            return succes



    def get_liste_envie_eleve(self, id_eleve):
        return self.liste_envie_dao.get_liste_envie_by_id(id_eleve)

