from source.DAO.dbconnection import DBConnection


class UtilisateurDAO:
    def create_compte(self, utilisateur): # faut-il mettre plutôt "utilisateur()" car pour instancier un objet il faut mettre des parenthèses
        """Pour créer un utilisateur en base.
        
        Parameters
        ---------
        utilisateur : Utilisateur
            L'objet utilisateur à créer.
            
        Returns
        ------
        Utilisateur
            L'utilisateur créé avec un ID attribué
        """
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO utilisateur (nom, prénom, pseudo, mdp, type_utilisateur)"
                    "     VALUES (%(nom)s, %(prenom)s,%(pseudo)s, %(mdp)s, %(type_utilisateur)s)"
                    "  RETURNING id_utilisateur;                           ",
                    {
                        "nom": utilisateur.nom,
                        "prénom": utilisateur.prenom,
                        "pseudo": utilisateur.pseudo,
                        "mdp": utilisateur.mdp,
                        "type_utilisateur": utilisateur.type_utilisateur
                    },
                )
                utilisateur.id = cursor.fetchone()["id_utilisateur"]  # on récupère l'ID généré à l'aide de cursor.fetchone()["id_utilisateur"]
                # et on l'assigne à utilisateur.id. Cela suppose que notre table a un champ id_utilisateur.
        return utilisateur

    def find_by_nom(self, nom, prenom):
        """Pour récupérer un utilisateur depuis ses noms et prénoms.
        
        Parameters
        ---------
        nom : str
            Le nom de l'utilisateur
        prenom : str
            Le prénom de l'utilisateur
            
        Returns
        ------
        dict
            Les informations sur l'utilisateur
        """
        if not isinstance(nom, str):
            raise TypeError("le nom de l'utilisateur est une chaîne de caractères")
        if not isinstance(nom, str):
            raise TypeError("le prénom de l'utilisateur est une chaîne de caractères")
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


    def find_mdp(self, pseudo):
        """Pour récupérer le mot de passe d'un utilisateur à partir du pseudo.
        
        Parameters
        ---------
        pseudo : str
            Le pseudo de l'utilisateur
            
        Returns
        ------
        str
            Le mot de passe de l'utilisateur
        """
        if not isinstance(pseudo, str):
            raise TypeError("le pseudo de l'utilisateur est une chaîne de caractères")
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT mdp "
                    "FROM utilisateur "
                    "WHERE pseudo = %(pseudo)s",
                    {"pseudo": pseudo}
                )
                mdp = cursor.fetchone()
                if mdp is None:
                    print("Le pseudo n'existe pas")
        return mdp


    def find_by_id(self, id_utilisateur):
        """Pour récupérer un utilisateur depuis son identifiant.
        
        Parameters
        ---------
        id_utilisateur : int
            L'identifiant de l'utilisateur
            
        Returns
        -------
        dict
            Toutes les informations sur l'utilisateur, sauf le mot de passe.
        """
        if not isinstance(id_utilisateur, int):
            raise TypeError("l'identifiant de l'utilisateur est un entier numérique")
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT *                          "
                    "  FROM utilisateur                      "
                    " WHERE id_utilisateur = %(id_utilisateur)s",
                    {"id_utilisateur": id_utilisateur}
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
        """Pour supprimer un utilisateur de la base de données.
        
        Parameters
        ---------
        id_utilisateur : int
            L'identifiant de l'utilisateur à supprimer
        """
        if not isinstance(id_utilisateur, int):
            raise TypeError("l'identifiant de l'utilisateur est un entier numérique")
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM utilisateur "
                    "WHERE id_utilisateur = %(id_utilisateur)s",
                    {"id_utilisateur": id_utilisateur}
                )
                if cursor.rowcount == 0:
                    raise IdUtilisateurInexistantError(id_utilisateur)
