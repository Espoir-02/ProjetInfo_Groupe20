from source.DAO.dbconnection import DBConnection
from source.exception.exceptions import IdStageInexistantError


class ListeEnvieDAO:
    def update_liste_envie(self, id_utilisateur, id_stage):
        """Met à jour la liste d'envie avec un nouveau stage consulté.

        Parameters
        ----------
        id_utilisateur: int
            L'identifiant de l'utilisateur à qui appartient la liste
        id_stage : int
            L'identifiant du stage à ajouter

        Examples
        --------
        >>> ma_liste = ListeEnvieDAO()
        >>> id_utilisateur = 1
        >>> id_stage = 10
        >>> ma_liste.update_liste_envie(id_utilisateur, id_stage)
        """
        if not isinstance(id_utilisateur, int):
            raise TypeError("l'identifiant de l'utilisateur est un entier numérique")
        if not isinstance(id_stage, int):
            raise TypeError("l'identifiant du stage est un entier numérique")

        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO liste_envie (id_utilisateur, id_stage) "
                    "VALUES (%(id_utilisateur)s, %(id_stage)s)",
                    {"id_utilisateur": id_utilisateur, "id_stage": id_stage}
                )

    def delete_liste_envie(self, id_utilisateur, id_stage):
        """Pour supprimer un stage de la liste d'envies d'un utilisateur.

        Parameters
        ---------
        id_utilisateur: int
            L'identifiant de l'utilisateur à qui appartient la liste
        id_stage : int
            Le stage à supprimer

        Examples
        --------
        >>> ma_liste = ListeEnvieDAO()
        >>> id_utilisateur = 1
        >>> id_stage = 10
        >>> ma_liste.delete_liste_envie(id_utilisateur, id_stage)
        """
        if not isinstance(id_utilisateur, int):
            raise TypeError("l'identifiant de l'utilisateur est un entier numérique")
        if not isinstance(id_stage, int):
            raise TypeError("l'identifiant du stage est un entier numérique")

        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM liste_envie "
                    "WHERE id_utilisateur = %(id_utilisateur)s AND id_stage = %(id_stage)s",
                    {"id_utilisateur": id_utilisateur, "id_stage": id_stage}
                )
                if cursor.rowcount == 0:
                    raise IdStageInexistantError(id_stage)

    def get_liste_envie_by_id(self, id_utilisateur):
        """Pour récupérer la liste d'envie d'un utilisateur à partir de son identifiant.

        Parameters
        ---------
        id_utilisateur : int
            L'identifiant de l'utilisateur

        Returns
        -------
        list of dict
        La liste d'envie de l'utilisateur.
        Chaque envie est sous forme de liste

        Examples
        --------
        >>> ma_liste = ListeEnvieDAO()
        >>> id_utilisateur = 1
        >>> ma_liste.get_liste_envie_by_id(id_utilisateur)
        10
        """
        if not isinstance(id_utilisateur, int):
            raise TypeError("l'identifiant de l'utilisateur est un entier numérique")

        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "FROM liste_envie"
                    "WHERE id_utilisateur= %(id_utilisateur)s",
                    {"id_utilisateur": id_utilisateur})

                liste_envie = cursor.fetchall()
                if not liste_envie:
                    print("La liste d'envie est vide")
        return liste_envie

# quand on récupère, on peut récupérer aussi la table stage associée à l'id pour avoir plus d'infos.
#  Amettre en oeuvre

