from source.DAO.dbconnection import DBConnection
from source.exception.exceptions import IdUtilisateurInexistantError
from source.business_object.utilisateur.utilisateur2 import Utilisateur


class UtilisateurDAO:
    def create_compte(self, utilisateur):
        """Pour créer un utilisateur en base.

        Parameters
        ---------
        utilisateur : Utilisateur
            L'objet utilisateur à créer.

        Returns
        ------
        Utilisateur
            L'utilisateur créé avec un ID attribué

        Examples
        --------
        >>> mes_utilisateurs = UtilisateurDAO()
        >>> nouvel_utilisateur = Utilisateur(nom="Millepertuis", prenom="Iris", pseudo= "Milliris", mot_de_passe= "Motdepasse123", type_utilisateur = "eleve")
        >>> utilisateur_cree = mes_utilisateurs.create_compte(nouvel_utilisateur)
        >>> print(utilisateur_cree.id)
        6
        """

        if utilisateur.type_utilisateur == "invité":
            # Utilisateur invité, ne stocker que l'information minimale
            with DBConnection().connection as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO base_projetinfo.utilisateur (type_utilisateur)"
                        " VALUES (%(type_utilisateur)s)"
                        " RETURNING id_utilisateur;",
                        {"type_utilisateur": utilisateur.type_utilisateur},
                    )
                    utilisateur.id = cursor.fetchone()[0]
            return utilisateur

        else:
            try:
                # Vérifier la longueur du mot de passe
                if len(utilisateur.mot_de_passe) < 8:
                    raise ValueError(
                        "Le mot de passe doit contenir au moins 8 caractères."
                    )

                # Vérifier si le pseudo existe déjà dans la base de données
                with DBConnection().connection as conn:
                    with conn.cursor() as cursor:
                        cursor.execute(
                            "SELECT COUNT(*) FROM base_projetinfo.utilisateur WHERE pseudo = %(pseudo)s",
                            {"pseudo": utilisateur.pseudo},
                        )
                        if cursor.fetchone()[0] > 0:
                            raise ValueError("Ce pseudo est déjà utilisé.")
                            return None

                        cursor.execute(
                            "INSERT INTO base_projetinfo.utilisateur (nom, prenom, pseudo, mot_de_passe, type_utilisateur)"
                            "     VALUES (%(nom)s, %(prenom)s,%(pseudo)s, %(mot_de_passe)s, %(type_utilisateur)s)"
                            "  RETURNING id_utilisateur;                           ",
                            {
                                "nom": utilisateur.nom,
                                "prenom": utilisateur.prenom,
                                "pseudo": utilisateur.pseudo,
                                "mot_de_passe": utilisateur.mot_de_passe,
                                "type_utilisateur": utilisateur.type_utilisateur,
                            },
                        )
                        utilisateur.id = cursor.fetchone()[
                            0
                        ]  # on récupère l'ID généré à l'aide de cursor.fetchone()["id_utilisateur"]
                return utilisateur
            except ValueError as e:
                print(f"Erreur lors de la création du compte : {e}")
                return None

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

        Examples
        -------
        >>> mes_utilisateurs = UtilisateurDAO()
        >>> utilisateur = mes_utilisateurs.find_by_nom("Millepertuis", "Iris")
        >>> print(utilisateur)
        {'id_utilisateur': 6, 'pseudo': 'Milliris', 'nom': 'Millepertuis', 'prénom': 'Iris'}
        """
        if not isinstance(nom, str):
            raise TypeError("le nom de l'utilisateur est une chaîne de caractères")
        if not isinstance(prenom, str):
            raise TypeError("le prénom de l'utilisateur est une chaîne de caractères")
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT *                          "
                    "  FROM base_projetinfo.utilisateur                      "
                    " WHERE nom = %(nom)s AND prenom = %(prenom)s    ",
                    {"nom": nom, "prenom": prenom},
                )
                utilisateur_bdd = cursor.fetchone()

        utilisateur_dict = None
        if utilisateur_bdd:
            utilisateur_dict = {
                "id_utilisateur": utilisateur_bdd[0],
                "pseudo": utilisateur_bdd[1],
                "nom": utilisateur_bdd[2],
                "prénom": utilisateur_bdd[3],
            }
        return utilisateur_dict

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

        Examples
        -------
        >>> mes_utilisateurs = UtilisateurDAO()
        >>> mdp = mes_utilisateurs.find_mdp("Milliris")
        >>> print(mdp)
        "MotDePasse123"
        """
        if not isinstance(pseudo, str):
            raise TypeError("le pseudo de l'utilisateur est une chaîne de caractères")
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT mot_de_passe "
                    "FROM base_projetinfo.utilisateur "
                    "WHERE pseudo = %(pseudo)s",
                    {"pseudo": pseudo},
                )
                mot_de_passe = cursor.fetchone()
                if mot_de_passe is None:
                    print("Le pseudo n'existe pas")
                else:
                    mot_de_passe = mot_de_passe[0]
        return mot_de_passe

    def find_id_by_pseudo(self, pseudo):
        """Pour récupérer l'identifiant d'un utilisateur à partir du pseudo.

        Parameters
        ---------
        pseudo : str
            Le pseudo de l'utilisateur

        Returns
        ------
        int
            L'identifiant de l'utilisateur

        >>> mes_utilisateurs = UtilisateurDAO()
        >>> id = mes_utilisateurs.find_id_by_pseudo("Milliris")
        >>> print(id)
        6
        """
        if not isinstance(pseudo, str):
            raise TypeError("le pseudo de l'utilisateur est une chaîne de caractères")
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id_utilisateur "
                    "FROM base_projetinfo.utilisateur "
                    "WHERE pseudo = %(pseudo)s",
                    {"pseudo": pseudo},
                )
                id_utilisateur = cursor.fetchone()
                if id_utilisateur is None:
                    print("Le pseudo n'existe pas")
                else:
                    id_utilisateur = id_utilisateur[
                        0
                    ]  # Extrait le mot de passe du tuple
        return id_utilisateur

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

        Examples
        -------
        >>> mes_utilisateurs = UtilisateurDAO()
        >>> utilisateur = mes_utilisateurs.find_by_id(6)
        >>> print(utilisateur)
        {'id_utilisateur': 6, 'pseudo': 'Milliris', 'nom': 'Millepertuis', 'prénom': 'Iris'}
        """
        if not isinstance(id_utilisateur, int):
            raise TypeError("l'identifiant de l'utilisateur est un entier numérique")

        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT *                          "
                    "  FROM base_projetinfo.utilisateur                      "
                    " WHERE id_utilisateur = %(id_utilisateur)s",
                    {"id_utilisateur": id_utilisateur},
                )
                utilisateur_bdd = cursor.fetchone()

        if utilisateur_bdd is None:
            raise IdUtilisateurInexistantError(id_utilisateur)
        if utilisateur_bdd:
            utilisateur_dict = {
                "id_utilisateur": utilisateur_bdd[0],
                "pseudo": utilisateur_bdd[1],
                "nom": utilisateur_bdd[2],
                "prénom": utilisateur_bdd[3],
            }
        return utilisateur_dict

    def get_all_utilisateurs(self):
        """Pour récupérer une liste contenant tous les utilisateurs.

        Returns
        -------
        list of dict
            La liste contenant les informations sur chaque utilisateur

        Examples
        -------
        >>> mes_utilisateurs = UtilisateurDAO()
        >>> liste=mes_utilisateurs.get_all_utilisateurs()
        >>> print(liste)
        #Affiche la liste de tous les utilisateurs avec leurs informations associées
        """
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM base_projetinfo.utilisateur")
                columns = [col[0] for col in cursor.description]
                result = [dict(zip(columns, row)) for row in cursor.fetchall()]

        if not result:
            print("Aucun utilisateur trouvé dans la base de données.")
        return result

    def get_type_utilisateur(self, pseudo):
        """Pour récupérer le type de l'utilisateur à partir de son pseudo

        Parameters
        ----------
        pseudo: str
            Le pseudo de l'utilisateur

        Returns
        -------
        str
            Le type de l'utilisateur (élève, professeur, administrateur, invité)

        Examples
        -------
        >>> mes_utilisateurs = UtilisateurDAO()
        >>> type_utilisateur = mes_utilisateurs.get_type_utilisateur(Milliris)
        >>> print(type_utilisateur)
        "elève"
        """
        if not isinstance(pseudo, str):
            raise TypeError("le pseudo de l'utilisateur est une chaîne de caractères")
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT type_utilisateur "
                    "FROM base_projetinfo.utilisateur "
                    "WHERE pseudo = %(pseudo)s",
                    {"pseudo": pseudo},
                )
                type_utilisateur = cursor.fetchone()
                if type_utilisateur is None:
                    print("Le pseudo n'existe pas")
                else:
                    type_utilisateur = type_utilisateur[0]
        return type_utilisateur

    def update_utilisateur(self, pseudo, nouveau_mdp):
        """Pour mettre à jour le mot de passe d'un utilisateur.

        Parameters
        ----------
        pseudo : str
            Le pseudo de l'utilisateur

        Examples
        ------
        >>> mes_utilisateurs = UtilisateurDAO()
        >>> pseudo= 'Milliris'
        >>> nouveau_mdp = "MotDePasse456"
        >>> mes_utilisateurs.update_utilisateur(Milliris, nouveau_mdp)
        >>> mdp_maj = mes_utilisateurs.find_mdp("Milliris")
        >>> print(mdp_maj)
        "MotDePasse456"
        """
        if not isinstance(pseudo, str):
            raise TypeError("le pseudo de l'utilisateur est une chaîne de caractères")
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE base_projetinfo.utilisateur "
                    "SET mot_de_passe = %(nouveau_mdp)s "
                    "WHERE pseudo = %(pseudo)s",
                    {"nouveau_mot_de_passe": nouveau_mdp, "pseudo": pseudo},
                )

                if cursor.rowcount == 0:
                    print("Le pseudo n'existe pas")

    def delete_utilisateur(self, id_utilisateur):
        """Pour supprimer un utilisateur de la base de données.

        Parameters
        ---------
        id_utilisateur : int
            L'identifiant de l'utilisateur à supprimer

        Examples
        --------
        >>> mes_utilisateurs = UtilisateurDAO()
        >>> id_utilisateur_a_supprimer = 6
        >>> mes_utilisateurs.delete_utilisateur(id_utilisateur_a_supprimer)
        """
        if not isinstance(id_utilisateur, int):
            raise TypeError("l'identifiant de l'utilisateur est un entier numérique")
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM base_projetinfo.utilisateur "
                    "WHERE id_utilisateur = %(id_utilisateur)s",
                    {"id_utilisateur": id_utilisateur},
                )
                if cursor.rowcount == 0:
                    raise IdUtilisateurInexistantError(id_utilisateur)


nouvel_utilisateur_invite = Utilisateur(type_utilisateur="invité")
utilisateur = UtilisateurDAO()

oi = utilisateur.create_compte(nouvel_utilisateur_invite)
print(oi.id)
