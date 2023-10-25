class SuggestionsDAO:
    def create_suggestion(self,eleve, stage, professeur) :
        """Met à jour la liste de suggestion d'un élève."""
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO liste_suggestions (id_élève, id_stage, id_professeur) "
                    "VALUES (%(id_eleve)s, %(id_stage)s)",
                    {"id_élève": eleve.id, 
                    "id_stage": stage.id, 
                    "id_professeur":professeur.id}
                )

    def get_suggestions_by_id(self, id_utilisateur):
        """Pour récupérer la liste de suggestions d'un élève à partir de son identifiant"""
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
        """Pour supprimer un stage de la liste de suggestions d'un utilisateur"""
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM liste_suggestions "
                    "WHERE id_utilisateur = %(id_utilisateur)s AND id_stage = %(id_stage)s",
                    {"id_utilisateur": id_utilisateur, "id_stage": id_stage}
                )
                if cursor.rowcount == 0:
                    raise IdStageInexistantError(id_stage)