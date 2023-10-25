class StageDAO:
    def create_stage(self, stage):
        """Pour entrer un stage dans la base de données"""
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO stage (titre, lien, domaine, modalités, date_publication, date_début, date_fin, entreprise) "
                    "     VALUES (%(titre)s, %(lien)s,%(domaine)s, %(modalites)s, %(date_publication)s, %(date_debut)s, %(date_fin)s, %(entreprise)s) "
                    "  RETURNING id_stage;                           ",
                    {"titre": stage.titre,
                    "lien": stage.lien,
                    "domaine": stage.domaine,
                    "modalités": stage.modalites,
                    "date_publication":stage.date_publication,
                    "date_début": stage.date_debut,
                    "date_fin": stage.date_fin,
                    "entreprise":stage.entreprise},
                )
                stage.id = cursor.fetchone()["id_stage"]  # on récupère l'ID généré à l'aide de cursor.fetchone()["id_stage"]
                # et on l'assigne à stage.id. Cela suppose que notre table a un champ id_stage.
        return stage

    