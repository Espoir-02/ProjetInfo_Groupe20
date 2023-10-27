from source.DAO.dbconnection import DBConnection


class EntrepriseDAO:
    def create_stage(self, entreprise):
        """Pour entrer une entreprise dans la base de données.

        Parameters
        ---------
        entreprise: Entreprise
            L'objet entreprise à créer.

        Returns
        -------
        Entreprise
            L'objet entreprise créé avec un ID attribué
        """
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO entreprise (dénomination, ville, région, pays, email, domaine ) "
                    "     VALUES (%(denomination)s, %(ville)s,%(region)s, %(pays)s, %(email)s, %(domaine)s) "
                    "  RETURNING id_entreprise;                           ",
                    {
                        "dénomination": entreprise.denomination,
                        "ville": entreprise.ville,
                        "région": entreprise.region,
                        "pays": entreprise.pays,
                        "email": entreprise.email,
                        "domaine": entreprise.domaine
                    },
                )
                entreprise.id = cursor.fetchone()["id_entreprise"]  # on récupère l'ID généré à l'aide de cursor.fetchone()["id_stage"]
                # et on l'assigne à entreprise.id. Cela suppose que notre table a un champ id_entreprise.
        return entreprise
