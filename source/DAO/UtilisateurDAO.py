class UtilisateurDAO:

    def create_compte(self, utilisateur):
        """Pour créer un utilisateur en base"""
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO utilisateur (nom, prénom, pseudo, mdp, professeur ) "
                    "     VALUES (%(nom)s, %(prenom)s,%(pseudo)s, %(mdp)s, %(professeur)s) "
                    "  RETURNING id_utilisateur;                           ",
                    {"nom": utilisateur.nom,
                    "prénom": utilisateur.prenom,
                    "pseudo": utilisateur.pseudo,
                    "mdp": utilisateur.mdp,
                    "professeur": utilisateur.professeur},
                )
                utilisateur.id = cursor.fetchone()["id_utilisateur"]  # on récupère l'ID généré à l'aide de cursor.fetchone()["id_utilisateur"]
                # et on l'assigne à utilisateur.id. Cela suppose que notre table a un champ id_utilisateur.
        return utilisateur

    def find_by_nom(self, nom, prenom):
        """Pour récupérer un utilisateur depuis ses noms et prénoms"""
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT *                          "
                    "  FROM utilisateur                      "
                    " WHERE nom = %(nom)s AND prénom = %(prenom)s    ",
                    {"nom": nom, "prénom": prenom}
                )
                utilisateur_bdd = cursor.fetchone()
                          
        utilisateur = None
        if utilisateur_bdd:
            utilisateur = Utilisateur(
                id=utilisateur_bdd["id_utilisateur"],
                pseudo=utilisateur_bdd["pseudo"],
                nom=utilisateur_bdd["nom"],
                prénom=utilisateur_bdd["prénom"],
            )
        return utilisateur

    def get_all_ids(self):
        """Pour récupérer une liste contenant les ID des utilisateurs"""
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id_utilisateur FROM utilisateur"
                )
                ids_utilisateurs = [row["id_utilisateur"] for row in cursor.fetchall()]
        return ids_utilisateurs

    def delete_utilisateur(self, id_utilisateur):
        """Pour supprimer un utilisateur de la base de données"""
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM utilisateur "
                    "WHERE id_utilisateur = %(id_utilisateur)s",
                    {"id_utilisateur": id_utilisateur}
                )