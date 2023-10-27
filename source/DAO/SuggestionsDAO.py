from source.DAO.dbconnection import DBConnection
from source.exception.exceptions import IdStageInexistantError


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
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO liste_suggestions (id_eleve, id_stage, id_professeur) "
                    "VALUES (%(id_eleve)s, %(id_stage)s)",
                    {
                        "id_élève": id_eleve,
                        "id_stage": id_stage,
                        "id_professeur": id_professeur
                    }
                )

    def get_suggestions_by_id(self, id_utilisateur):
        """Récupère la liste de suggestions d'un élève à partir de son identifiant.

        Parameters
        --------
        id_utilisateur: int
            l'identifiant de l'élève

        Returns
        ------
        list of dict
            La liste de suggestions de l'élève.
            Chaque suggestion est sous forme de liste.

        Examples
        --------
        >>> mes_suggestions = SuggestionsDAO() 
        >>> id_utilisateur = 123  
        >>> suggestions=mes_suggestions.get_suggestions_by_id(id_utilisateur)
        print(suggestions)
        # La liste de suggestions de l'élève avec l'identifiant 123 est renvoyée.
        """
        if not isinstance(id_utilisateur, int):
            raise TypeError("l'identifiant de l'utilisateur est un entier numérique")
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "FROM liste_suggestions"
                    "WHERE id_utilisateur= %(id_utilisateur)s",
                    {"id_utilisateur": id_utilisateur})

                liste_suggestions = cursor.fetchall()
                if not liste_suggestions:
                    print("La liste de suggestions est vide")
        return liste_suggestions

    def delete_suggestion(self, id_utilisateur, id_stage):
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
        if not isinstance(id_utilisateur, int):
            raise TypeError("l'identifiant de l'utilisateur est un entier numérique")
        if not isinstance(id_stage, int):
            raise TypeError("l'identifiant du stage est un entier numérique")
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM suggestion "
                    "WHERE id_utilisateur = %(id_utilisateur)s AND id_stage = %(id_stage)s",
                    {"id_utilisateur": id_utilisateur, "id_stage": id_stage}
                )
                if cursor.rowcount == 0:
                    raise IdStageInexistantError(id_stage)
