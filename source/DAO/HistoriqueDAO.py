class HistoriqueDAO:

    def update_historique(self, id_utilisateur, id_stage):
        """Met à jour l'historique de l'utilisateur avec un nouveau stage consulté."""
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO historique (id_utilisateur, id_stage) "
                    "VALUES (%(id_utilisateur)s, %(id_stage)s)",
                    {"id_utilisateur": id_utilisateur, "id_stage": id_stage}
                )

    def get_all_historique_by_id(self, id_historique):
        """Récupère tout l'historique d'un utilisateur à partir de l'identifiant."""
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "FROM historique"
                    "WHERE id_historique= %(id_historique)s",
                    {"id_historique": id_historique})
                historique = cursor.fetchall()
                if not historique:
                    print("L'historique' est vide")
        return historique