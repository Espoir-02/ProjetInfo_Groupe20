from source.DAO.HistoriqueDAO import HistoriqueDAO
from source.DAO.utilisateur_dao import UtilisateurDAO
from source.view.couche3sousmenu.detail_stage_view import detail_stage_view_eleve, detail_stage_view_prof
from InquirerPy import inquirer
from source.DAO.StageDAO import StageDAO

class HistoriqueService:
    def __init__(self):
        self.historique_dao = HistoriqueDAO()

    def get_all_historique_by_id(self, id_utilisateur):
        """
        Récupère tout l'historique d'un utilisateur à partir de son identifiant.

        Parameters
        ----------
        id_utilisateur : int
            L'identifiant de l'utilisateur.

        Returns
        -------
        list of dict
            Une liste contenant les recherches qui constituent l'historique.
            Chaque recherche est représentée sous forme de dictionnaire.
        """
        return self.historique_dao.get_all_historique_by_id(id_utilisateur)

    def ajouter_stage_a_historique(self, id_utilisateur,stage_id):
        """
        Ajoute un stage à l'historique de l'utilisateur.

        Parameters:
        - stage_id: int
          L'identifiant du stage à ajouter à l'historique.

        Returns:
        - bool
          True si le stage a été ajouté avec succès, False sinon.
        """
        # Ajouter le stage à l'historique de l'utilisateur en utilisant le DAO
        return self.utilisateur_dao.update_historique(id_utilisateur, stage_id)
       
