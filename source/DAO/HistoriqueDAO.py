from source.DAO.dbconnection import DBConnection
from source.DAO.utilitaire_dao import UtilitaireDAO
from source.exception.exceptions import IdUtilisateurInexistantError
from source.exception.exceptions import IdStageInexistantError


class HistoriqueDAO:
    def update_historique(self, id_utilisateur, id_stage):
        """Met à jour l'historique de l'utilisateur avec un nouveau stage consulté.

        Parameters
        ---------
        id_utilisateur: int
            L'identifiant de l'utilisateur
        id_stage : int
            L'identifiant du stage consulté

        Examples
        --------
        >>> mes_historique = HistoriqueDAO()
        >>> id_utilisateur = 123
        >>> id_stage = 96
        >>> mes_historiques.update_historique(id_utilisateur, id_stage)
        """
        if not isinstance(id_utilisateur, int):
            raise TypeError("l'identifiant de l'utilisateur est un entier numérique")
        if not isinstance(id_stage, int):
            raise TypeError("l'identifiant du stage est un entier numérique")
        if not UtilitaireDAO.check_user_exists(id_utilisateur):
            raise IdUtilisateurInexistantError(id_utilisateur)
        if not UtilitaireDAO.check_stage_exists(id_stage):
            raise IdStageInexistantError(id_stage)

        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO base_projetinfo.historique (id_utilisateur, id_stage) "
                    "VALUES (%(id_utilisateur)s, %(id_stage)s)",
                    {"id_utilisateur": id_utilisateur, "id_stage": id_stage},
                )

    def get_all_historique_by_id(self, id_utilisateur):
        """Récupère tout l'historique d'un utilisateur à partir de l'identifiant.

        Parameters
        ----------
        id_utilisateur : int
            L'identifiant de l'utilisateur.

        Returns
        -------
        list of dict
            Une liste contenant les recherches qui constituent l'historique.
            Chaque recherche est représentée sous forme de dictionnaire.

        Examples
        --------
        >>> mes_historique = HistoriqueDAO()
        >>> id_utilisateur = 123
        >>> historique = mes_historiques.get_all_historique_by_id(id_utilisateur)
        >>> print(historique)
        # Résultat : Liste des recherches dans l'historique
        """
        if not isinstance(id_utilisateur, int):
            raise TypeError("l'identifiant de l'utilisateur est un entier numérique")
        if not UtilitaireDAO.check_user_exists(id_utilisateur):
            raise IdUtilisateurInexistantError(id_utilisateur)

        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT stage.id_stage, stage.titre, stage.lien, stage.domaine "
                    "FROM base_projetinfo.historique AS le "
                    "JOIN base_projetinfo.stage AS stage ON le.id_stage = stage.id_stage "
                    "WHERE id_utilisateur= %(id_utilisateur)s",
                    {"id_utilisateur": id_utilisateur},
                )
                historique = cursor.fetchall()
                if not historique:
                    print("L'historique' est vide")
                result_list = []
                for recherche in historique:
                    hist_dict = {
                        "id_stage": recherche[0],
                        "titre": recherche[1],
                        "lien": recherche[2],
                        "domaine": recherche[3],
                    }
                    result_list.append(hist_dict)
        return result_list
