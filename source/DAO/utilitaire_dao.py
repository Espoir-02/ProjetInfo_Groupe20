from source.DAO.dbconnection import DBConnection


class UtilitaireDAO:
    @staticmethod
    def check_user_exists(id_utilisateur):
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT COUNT(*) FROM base_projetinfo.utilisateur "
                    "WHERE id_utilisateur = %(id_utilisateur)s",
                    {"id_utilisateur": id_utilisateur},
                )
                count = cursor.fetchone()[0]
                return count > 0

    def check_stage_exists(id_stage):
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT COUNT(*) FROM base_projetinfo.stage "
                    "WHERE id_stage = %(id_stage)s",
                    {"id_stage": id_stage},
                )
                count = cursor.fetchone()[0]
                return count > 0

    @staticmethod
    def check_pseudo_exists(pseudo):
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT COUNT(*) FROM base_projetinfo.utilisateur "
                    "WHERE pseudo = %(pseudo)s",
                    {"pseudo": pseudo},
                )
                count = cursor.fetchone()[0]
                return count > 0
