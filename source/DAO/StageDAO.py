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
                    "INSERT INTO base_projetinfo.stage (titre, lien, domaine, salaire, date_publication, periode, niveau_etudes, entreprise) "
                    "     VALUES (%(titre)s, %(lien)s,%(domaine)s, %(salaire)s, %(date_publication)s, %(periode)s, %(niveau_etudes)s, %(entreprise)s) "
                    "  RETURNING id_stage;                           ",
                    {
                        "titre": stage.titre,
                        "lien": stage.lien,
                        "domaine": stage.domaine,
                        "salaire": stage.salaire,
                        "date_publication": stage.date_publication,
                        "periode": stage.periode,
                        "niveau_etudes": stage.niveau_etudes,
                        "entreprise": stage.entreprise,
                    },
                )
                stage.id = cursor.fetchone()[
                    0
                ]  # on récupère l'ID généré à l'aide de cursor.fetchone()["id_stage"]
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
                    "  FROM base_projetinfo.stage                      "
                    " WHERE id_stage = %(id_stage)s",
                    {"id_stage": id_stage},
                )
                stage_bdd = cursor.fetchone()

        stage_dict = None
        if stage_bdd:
            stage_dict = {
                "id-stage": stage_bdd[0],
                "titre": stage_bdd[1],
                "lien": stage_bdd[2],
                "domaine": stage_bdd[3],
                "date_publication": stage_bdd[4],
                "salaire": stage_bdd[5],
                "periode": stage_bdd[6],
                "niveau_etudes": stage_bdd[7],
                "entreprise": stage_bdd[8],
            }
        return stage_dict
