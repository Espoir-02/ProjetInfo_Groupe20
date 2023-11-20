from source.DAO.dbconnection import DBConnection
from source.DAO.utilitaire_dao import UtilitaireDAO
from source.exception.exceptions import IdStageInexistantError
from source.exception.exceptions import IdEleveInexistantError


class ListeEnvieDAO:
    def update_liste_envie(self, id_eleve, id_stage):
        """Met à jour la liste d'envie avec un nouveau stage consulté.

        Parameters
        ----------
        id_eleve: int
            L'identifiant de l'élève à qui appartient la liste
        id_stage : int
            L'identifiant du stage à ajouter

        Examples
        --------
        >>> ma_liste = ListeEnvieDAO()
        >>> id_eleve = 1
        >>> id_stage = 10
        >>> ma_liste.update_liste_envie(id_eleve, id_stage)
        """
        if not isinstance(id_eleve, int):
            raise TypeError("l'identifiant de l'élève est un entier numérique")
        if not isinstance(id_stage, int):
            raise TypeError("l'identifiant du stage est un entier numérique")
        if not UtilitaireDAO.check_user_exists(id_eleve):
            raise IdEleveInexistantError(id_eleve)
        if not UtilitaireDAO.check_stage_exists(id_stage):
            raise IdStageInexistantError(id_stage)

        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO base_projetinfo.liste_envie (id_eleve, id_stage) "
                    "VALUES (%(id_eleve)s, %(id_stage)s)",
                    {"id_eleve": id_eleve, "id_stage": id_stage},
                )

    def get_liste_envie_by_id(self, id_eleve):
        """Pour récupérer la liste d'envie d'un élève à partir de son identifiant.

        Parameters
        ---------
        id_eleve : int
            L'identifiant de l'élève

        Returns
        -------
        list of dict
        La liste d'envie de l'utilisateur.
        Chaque envie est sous forme de liste

        Examples
        --------
        >>> ma_liste = ListeEnvieDAO()
        >>> id_eleve = 1
        >>> liste =ma_liste.get_liste_envie_by_id(id_eleve)
        >>> print(liste)
        # La liste des envies de l'utilisateur
        """
        if not isinstance(id_eleve, int):
            raise TypeError("l'identifiant de l'élève est un entier numérique")
        if not UtilitaireDAO.check_user_exists(id_eleve):
            raise IdEleveInexistantError(id_eleve)

        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT stage.id_stage, stage.titre, stage.lien, stage.domaine "
                    "FROM base_projetinfo.liste_envie AS le "
                    "JOIN base_projetinfo.stage AS stage ON le.id_stage = stage.id_stage "
                    "WHERE le.id_eleve = %(id_eleve)s ",
                    {"id_eleve": id_eleve},
                )

                liste_envie = cursor.fetchall()
                if not liste_envie:
                    print("La liste d'envies est vide")
                result_list = []
                for envie in liste_envie:
                    envie_dict = {
                        "id_stage": envie[0],
                        "titre": envie[1],
                        "lien": envie[2],
                        "domaine": envie[3],
                    }
                    result_list.append(envie_dict)
        return result_list

    def delete_liste_envie(self, id_eleve, id_stage):
        """Pour supprimer un stage de la liste d'envies d'un élève.

        Parameters
        ---------
        id_eleve: int
            L'identifiant de l'élève à qui appartient la liste
        id_stage : int
            Le stage à supprimer

        Examples
        --------
        >>> ma_liste = ListeEnvieDAO()
        >>> id_eleve = 1
        >>> id_stage = 10
        >>> ma_liste.delete_liste_envie(id_eleve, id_stage)
        """
        if not isinstance(id_eleve, int):
            raise TypeError("l'identifiant de l'élève est un entier numérique")
        if not isinstance(id_stage, int):
            raise TypeError("l'identifiant du stage est un entier numérique")
        if not UtilitaireDAO.check_user_exists(id_eleve):
            raise IdEleveInexistantError(id_eleve)
        if not UtilitaireDAO.check_stage_exists(id_stage):
            raise IdStageInexistantError(id_stage)

        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM base_projetinfo.liste_envie "
                    "WHERE id_eleve = %(id_eleve)s AND id_stage = %(id_stage)s",
                    {"id_eleve": id_eleve, "id_stage": id_stage},
                )

    def delete_all_liste_envie(self, id_eleve):
        """Pour vider la liste d'envies d'un élève.

        Parameters
        ---------
        id_eleve: int
            L'identifiant de l'élève dont la liste d'envies doit être vidée.

        Examples
        --------
        >>> ma_liste = ListeEnvieDAO()
        >>> id_eleve = 6
        >>> ma_liste.delete_all_liste_envie(id_eleve)
        """
        if not isinstance(id_eleve, int):
            raise TypeError("L'identifiant de l'élève doit être un entier numérique")
        if not UtilitaireDAO.check_user_exists(id_eleve):
            raise IdEleveInexistantError(id_eleve)

        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM base_projetinfo.liste_envie "
                    "WHERE id_eleve = %(id_eleve)s",
                    {"id_eleve": id_eleve},
                )