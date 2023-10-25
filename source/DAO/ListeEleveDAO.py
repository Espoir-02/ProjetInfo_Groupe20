from dbconnection import DBConnection


class ListeEleves:
    def update_liste_eleve(self, eleve, id_prof):
        """Pour ajouter un élève à la liste d'élèves d'un professeur en particulier"""
        with DBConnection().connection as conn:
            with conn.cursor as cursor:
                cursor.execute(
                    "INSERT INTO liste_eleves(nom, prénom, id_élève, id_prof)"
                    "VALUES (%(nom)s, %(prénom)s, %(id_eleve)s, %(id_prof)s)",
                    {
                        "nom": eleve.nom,
                        "prénom": eleve.prenom,
                        "id_élève": eleve.id_eleve,
                        "id_prof": id_prof,
                    },
                )

    def delete_eleve(self, id_eleve, id_prof):
        """Pour supprimer un élève de la liste d'élèves d'un professeur donné"""
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM liste_eleves "
                    "WHERE id_élève = %(id_eleve)s AND id_prof=%(id_prof)s",
                    {"id_élève": id_eleve, "id_prof": id_prof},
                )
                if cursor.rowcount == 0:
                    raise IdEleveInexistantError(id_eleve)

    def get_liste_eleve_by_id(self, id_prof):
        """Pour obtenir la liste d'élève du professeur"""
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT *"
                    "WHERE id_prof= %(id_prof)s",
                    {"id_prof": id_prof}
                )
                liste_eleves = cursor.fetchall()
                if not liste_eleves:
                    print("La liste d'élèves est vide")
            return liste_eleves

# il faut rajouter ce qui se passe si l'identifiant n'existe pas
# ou si erreur, etc