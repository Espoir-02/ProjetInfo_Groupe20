from source.DAO.dbconnection import DBConnection
from source.exception.exceptions import IdStageInexistantError
from source.DAO.utilitaire_dao import UtilitaireDAO
from source.exception.exceptions import IdEleveInexistantError
from source.exception.exceptions import IdProfesseurInexistantError


class SuggestionsDAO:
    def create_suggestion(self, id_eleve, id_stage, id_professeur):
        """Met à jour la liste de suggestion d'un élève.

        Parameters
        ----------
        id_eleve: int
            L'identifiant de l'élève
        id_stage: int
            L'identifiant du stage suggéré
        id_professeur: int
            l'identifiant du professeur qui fait la suggestion

        Examples
        --------
        >>> mes_suggestions = SuggestionsDAO()
        >>> id_eleve = 123
        >>> id_stage = 456
        >>> id_professeur = 789
        >>> mes_suggestions.create_suggestion(id_eleve, id_stage, id_professeur)
        # La suggestion a été ajoutée à la liste de suggestions de l'élève.
        """
        if not isinstance(id_eleve, int):
            raise TypeError("l'identifiant de l'élève est un entier numérique")
        if not isinstance(id_stage, int):
            raise TypeError("l'identifiant du stage est un entier numérique")
        if not isinstance(id_professeur, int):
            raise TypeError("l'identifiant du professeur est un entier numérique")
        if not UtilitaireDAO.check_user_exists(id_eleve):
            raise IdEleveInexistantError(id_eleve)
        if not UtilitaireDAO.check_stage_exists(id_stage):
            raise IdStageInexistantError(id_stage)
        if not UtilitaireDAO.check_user_exists(id_professeur):
            raise IdProfesseurInexistantError(id_professeur)

        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO base_projetinfo.suggestion (id_eleve, id_stage, id_professeur) "
                    "VALUES (%(id_eleve)s, %(id_stage)s, %(id_professeur)s)",
                    {
                        "id_eleve": id_eleve,
                        "id_stage": id_stage,
                        "id_professeur": id_professeur,
                    },
                )

    def get_suggestions_by_id(self, id_eleve):
        """Récupère la liste de suggestions d'un élève à partir de son identifiant.

        Parameters
        --------
        id_eleve: int
            l'identifiant de l'élève

        Returns
        ------
        list of dict
            La liste de suggestions de l'élève.
            Chaque suggestion est sous forme de liste.

        Examples
        --------
        >>> mes_suggestions = SuggestionsDAO()
        >>> id_eleve = 123
        >>> suggestions=mes_suggestions.get_suggestions_by_id(id_eleve)
        print(suggestions)
        # La liste de suggestions de l'élève avec l'identifiant 123 est renvoyée.
        """
        if not isinstance(id_eleve, int):
            raise TypeError("l'identifiant de l'élève est un entier numérique")
        if not UtilitaireDAO.check_user_exists(id_eleve):
            raise IdEleveInexistantError(id_eleve)
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT stage.id_stage, stage.titre, stage.lien, stage.domaine, suggestion.id_professeur "
                    "FROM base_projetinfo.liste_envie AS le "
                    "JOIN base_projetinfo.stage AS stage ON le.id_stage = stage.id_stage "
                    "JOIN base_projetinfo.suggestion AS suggestion ON le.id_stage = suggestion.id_stage "
                    "WHERE le.id_eleve = %(id_eleve)s",
                    {"id_eleve": id_eleve},
                )

                liste_suggestions = cursor.fetchall()
                if not liste_suggestions:
                    print("La liste d'élèves est vide")
                result_list = []
                for suggestion in liste_suggestions:
                    suggestion_dict = {
                        "id_stage": suggestion[0],
                        "titre": suggestion[1],
                        "lien": suggestion[2],
                        "domaine": suggestion[3],
                        "id_professeur": suggestion[4],
                    }
                    result_list.append(suggestion_dict)
        return result_list

    def delete_suggestion(self, id_eleve, id_stage):
        """Pour supprimer un stage de la liste de suggestions d'un utilisateur.

        Parameters
        ---------
        id_utilisateur: int
            L'identifiant de l'élève à qui appartient la liste
        id_stage : int
            Le stage à supprimer

        Examples
        --------
        >>> mes_suggestions = SuggestionsDAO()
        >>> id_utilisateur = 123
        >>> id_stage = 456
        >>> mes_suggestions.delete_suggestion(id_utilisateur, id_stage)
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
                    "DELETE FROM base_projetinfo.suggestion "
                    "WHERE id_eleve = %(id_eleve)s AND id_stage = %(id_stage)s",
                    {"id_eleve": id_eleve, "id_stage": id_stage},
                )
