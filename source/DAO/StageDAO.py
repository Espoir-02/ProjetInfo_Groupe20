
from source.DAO.dbconnection import DBConnection


class StageDAO:
    def create_stage(self, stage):
        """Pour entrer un stage dans la base de données.
        
        Parameters
        ----------
        stage : Stage
            L'objet stage à créer.

        Returns
        ------
        Stage
            L'objet stage créé avec un id attribué
        """
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO stage (titre, lien, domaine, modalites, date_publication, date_début, date_fin, entreprise) "
                    "     VALUES (%(titre)s, %(lien)s,%(domaine)s, %(modalites)s, %(date_publication)s, %(date_debut)s, %(date_fin)s, %(entreprise)s) "
                    "  RETURNING id_stage;                           ",
                    {
                        "titre": stage.titre,
                        "lien": stage.lien,
                        "domaine": stage.domaine,
                        "modalités": stage.modalites,
                        "date_publication": stage.date_publication,
                        "date_début": stage.date_debut,
                        "date_fin": stage.date_fin,
                        "entreprise": stage.entreprise
                    },
                )
                stage.id = cursor.fetchone()["id_stage"]  # on récupère l'ID généré à l'aide de cursor.fetchone()["id_stage"]
                # et on l'assigne à stage.id. Cela suppose que notre table a un champ id_stage.
        return stage

    def find_stage_by_id(self, id_stage):
        """Pour récupérer les informations d'un stage depuis son identifiant.

        Parameters
        ---------
        id_stage: int
            L'identifiant du stage

        Returns
        -------
        dict
            Un dictionnaire qui contient toutes les informations du stage.
        """
        if not isinstance(id_stage, int):
            raise TypeError("l'identifiant du stage est un entier numérique")
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT *                          "
                    "  FROM stage                      "
                    " WHERE id_stage = %(id_stage)s",
                    {"id_stage": id_stage}
                )
                stage_bdd = cursor.fetchone()
             
        stage = None
        if stage_bdd:
            stage = Stage(
                id=stage_bdd["id_stage"],
                titre=stage_bdd["titre"],
                lien=stage_bdd["lien"],
                domaine=stage_bdd["domaine"],
                date_début=stage_bdd["date_début"],
                date_fin=stage_bdd["date_fin"],
                entreprise=stage_bdd["entreprise"],
            )
        return stage
