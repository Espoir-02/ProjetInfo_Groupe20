from source.DAO.dbconnection import DBConnection
from source.DAO.utilitaire_dao import UtilitaireDAO
from source.exception.exceptions import IdStageInexistantError
from prettytable import PrettyTable


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

        Examples
        -------
        >>> db = StageDAO()  #
        >>> nouveau_stage = Stage(titre="Pokémon stagiaire", lien="https://pokemon.com/stage", domaine="Pokemon",
        ...                        salaire= 'baies', date_publication="2023-11-02", periode="5 jours",
        ...                        niveau_etudes="Bac+3", entreprise="Evoli Inc.", lieu="Bourg-Palette")
        >>> stage_cree = db.create_stage(nouveau_stage)
        >>> print(stage_cree.id)
        415 # ID attribué au nouveau stage
        """
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO base_projetinfo.stage (titre, lien, domaine, salaire, date_publication, periode, niveau_etudes, entreprise, lieu) "
                    "     VALUES (%(titre)s, %(lien)s,%(domaine)s, %(salaire)s, %(date_publication)s, %(periode)s, %(niveau_etudes)s, %(entreprise)s, %(lieu)s) "
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
                        "lieu": stage.lieu,
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

        Examples
        -------
        >>> db = StageDAO()
        >>> stage_info = db.find_stage_by_id(415)
        >>> print(stage_info)
        {
            "id_stage": 415,
            "titre": "Pokémon stagiaire",
            "lien": "https://pokemon.com/stage",
            "domaine": "Pokemon",
            "date_publication": "2023-11-02",
            "salaire": 'baies',
            "periode": "5 jours",
            "niveau_etudes": "Bac+3",
            "entreprise": "Evoli Inc.",
            "lieu": "Bourg-Palette"
        }
        """
        if not isinstance(id_stage, int):
            raise TypeError("l'identifiant du stage est un entier numérique")
        if not UtilitaireDAO.check_stage_exists(id_stage):
            raise IdStageInexistantError(id_stage)
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
                "id_stage": stage_bdd[0],
                "titre": stage_bdd[1],
                "lien": stage_bdd[2],
                "domaine": stage_bdd[3],
                "date_publication": stage_bdd[4],
                "salaire": stage_bdd[5],
                "periode": stage_bdd[6],
                "niveau_etudes": stage_bdd[7],
                "entreprise": stage_bdd[8],
                "lieu": stage_bdd[9],
            }
        return stage_dict

    def find_stage_by_lieu(self, lieu):
        """Pour récupérer les informations des stages qui correspondent à un lieu donné.

        Parameters
        ---------
        lieu: str
            Le lieu qui intéresse l'utilisateur

        Returns
        -------
        list of dict
            Un dictionnaire qui contient toutes les informations des stages correspondants.

        Examples
        -------
        >>> db = StageDAO()
        >>> stage_info = db.find_stage_by_lieu('rennes)
        >>> print(stage_info)
        #La liste des stages dont le lieu est 'Rennes'.
        """
        if not isinstance(lieu, str):
            raise TypeError("Le lieu du stage est une chaîne de caractères")
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT *                          "
                    "  FROM base_projetinfo.stage                      "
                    " WHERE lieu = %(lieu)s",
                    {"lieu": lieu},
                )
                stage_bdd = cursor.fetchall()
                if not stage_bdd:
                    print("Aucun stage ne correspond au lieu demandé")
                result_list = []
                for stage in stage_bdd:
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
                        "lieu": stage_bdd[9],
                    }
                    result_list.append(stage_dict)
        return result_list

    def find_stage_by_domaine(self, domaine):
        """Pour récupérer les informations des stages qui correspondent à un domaine donné.

        Parameters
        ---------
        domaine: str
            Le domaine qui intéresse l'utilisateur

        Returns
        -------
        list of dict
            Un dictionnaire qui contient toutes les informations des stages correspondants.

        Examples
        -------
        >>> db = StageDAO()
        >>> stage_info = db.find_stage_by_domaine('jardinage')
        >>> print(stage_info)
        #La liste des stages dont le domaine est 'jardinage'.
        """
        if not isinstance(domaine, str):
            raise TypeError("Le domaine du stage est une chaîne de caractères")
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT *                          "
                    "  FROM base_projetinfo.stage                      "
                    " WHERE domaine = %(domaine)s",
                    {"domaine": domaine},
                )
                stage_bdd = cursor.fetchall()
                if not stage_bdd:
                    print("Aucun stage ne correspond au domaine demandé")
                result_list = []
                for stage in stage_bdd:
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
                        "lieu": stage_bdd[9],
                    }
                    result_list.append(stage_dict)
        return result_list

    def find_stage_by_entreprise(self, entreprise):
        """Pour récupérer les informations des stages qui correspondent à une entreprise donnée.

        Parameters
        ---------
        entreprise: str
            L'entreprise qui intéresse l'utilisateur

        Returns
        -------
        list of dict
            Un dictionnaire qui contient toutes les informations des stages correspondants.

        Examples
        -------
        >>> db = StageDAO()
        >>> stage_info = db.find_stage_by_entreprise('CactusGibus')
        >>> print(stage_info)
        #La liste des stages dont l'entreprise est 'CactusGibus'.
        """
        if not isinstance(entreprise, str):
            raise TypeError("L'entreprise du stage est une chaîne de caractères")
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT *                          "
                    "  FROM base_projetinfo.stage                      "
                    " WHERE entreprise = %(entreprise)s",
                    {"entreprise": entreprise},
                )
                stage_bdd = cursor.fetchall()
                if not stage_bdd:
                    print("Aucun stage ne correspond à l'entreprise demandée")
                result_list = []
                for stage in stage_bdd:
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
                        "lieu": stage_bdd[9],
                    }
                    result_list.append(stage_dict)
        return result_list

    def get_all_stages(self):
        """Pour récupérer une liste contenant tous les stages.

        Returns
        -------
        list of dict
            La liste contenant les informations sur chaque stage

        Examples
        -------
        >>> mes_stages = StageDAO()
        >>> liste=mes_stages.get_all_stages()
        >>> print(liste)
        #Affiche la liste de tous les stages avec leurs informations associées
        """
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM base_projetinfo.stage")
                columns = [col[0] for col in cursor.description]
                result = [dict(zip(columns, row)) for row in cursor.fetchall()]

        if not result:
            print("Aucun stage trouvé dans la base de données.")
        return result

    def delete_stage(self, id_stage):
        """Pour supprimer un stage de la base de données.

        Parameters
        ---------
        id_stage : int
            L'identifiant du stage à supprimer

        Examples
        --------
        >>> mes_stages = StageDAO()
        >>> id_stage_a_supprimer = 410
        >>> mes_stages.delete_stage(id_stage_a_supprimer)
        """
        if not isinstance(id_stage, int):
            raise TypeError("l'identifiant du stage est un entier numérique")
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM base_projetinfo.stage "
                    "WHERE id_stage = %(id_stage)s",
                    {"id_stage": id_stage},
                )
                if cursor.rowcount == 0:
                    raise IdStageInexistantError(id_stage)
