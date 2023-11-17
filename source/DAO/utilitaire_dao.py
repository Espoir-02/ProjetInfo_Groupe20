from source.DAO.dbconnection import DBConnection


class UtilitaireDAO:
    def __init__(self):
        pass

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
    @staticmethod
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
    def check_infos_stage_exists(nomstage, url2, domaine, periode , gratification, date_publication, etude, nomentreprise, lieu):
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT COUNT(*) FROM base_projetinfo.stage "
                    "WHERE titre = %(nomstage)s AND lien = %(url2)s AND "
                    "domaine = %(domaine)s AND "
                    "periode = %(periode)s AND salaire = %(gratification)s AND "
                    "date_publication = %(date_publication)s AND "
                    "niveau_etudes = %(etude)s AND "
                    "entreprise = %(nomentreprise)s AND lieu = %(lieu)s",
                    {
                        "nomstage": nomstage,
                        "url2": url2,
                        "domaine": domaine,
                        "periode": periode,
                        "gratification": gratification,
                        "date_publication": date_publication,
                        "etude": etude,
                        "nomentreprise": nomentreprise,
                        "lieu": lieu
                    },
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
