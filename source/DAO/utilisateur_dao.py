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
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
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
        >>> id = mes_utilisateurs.find_id_by_mdp("Milliris")
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

        utilisateur_dict = None
        if utilisateur_bdd:
            utilisateur_dict = {
                "id_utilisateur": utilisateur_bdd[0],
                "pseudo": utilisateur_bdd[1],
                "nom": utilisateur_bdd[2],
                "prénom": utilisateur_bdd[3],
            }
        return utilisateur_dict

    def get_all_ids(self):
        """Pour récupérer une liste contenant les ID des utilisateurs"""
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id_utilisateur FROM base_projetinfo.utilisateur")
                ids_utilisateurs = [row["id_utilisateur"] for row in cursor.fetchall()]
        return ids_utilisateurs

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
