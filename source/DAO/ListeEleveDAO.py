from source.DAO.dbconnection import DBConnection
from source.exception.exceptions import IdEleveInexistantError
from source.DAO.utilitaire_dao import UtilitaireDAO
from source.exception.exceptions import IdProfesseurInexistantError


class ListeElevesDAO:
    def update_liste_eleve(self, id_eleve, id_professeur):
        """Pour ajouter un élève à la liste d'élèves d'un professeur en particulier.

        Parameters
        ----------
        id_eleve : int
            L'identifiant de l'élève qui va être ajouté
        id_professeur : int
            L'identifiant du professeur à qui appartient la liste

         Examples
        --------
        >>> ma_liste = ListeElevesDAO()
        >>> id_eleve = 6
        >>> id_professeur = 17
        >>> ma_liste.update_liste_eleve(id_eleve, id_professeur)
        ----------
        """
        if not isinstance(id_eleve, int):
            raise TypeError("l'identifiant de l'élève est un entier numérique")
        if not isinstance(id_professeur, int):
            raise TypeError("l'identifiant du professeur est un entier numérique")
        if not UtilitaireDAO.check_user_exists(id_eleve):
            raise IdEleveInexistantError(id_eleve)
        if not UtilitaireDAO.check_user_exists(id_professeur):
            raise IdProfesseurInexistantError(id_professeur)

        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                # Utiliser une requête JOIN pour récupérer nom et prenom de la table utilisateur
                cursor.execute(
                    "INSERT INTO base_projetinfo.liste_eleves(nom, prenom, id_eleve, id_professeur)"
                    "SELECT u.nom, u.prenom, %(id_eleve)s, %(id_professeur)s"
                    "FROM base_projetinfo.utilisateur u WHERE u.id_utilisateur = %(id_eleve)s",
                    {"id_eleve": id_eleve, "id_professeur": id_professeur},
                )

    def delete_eleve(self, id_eleve, id_professeur):
        """Pour supprimer un élève de la liste d'élèves d'un professeur donné.

        Parameters
        ----------
        id_eleve : int
            L'identifiant de l'élève à supprimer.
        id_prof : int
            L'identifiant du professeur à qui appartient la liste

         Examples
        --------
        >>> ma_liste = ListeElevesDAO()  # Instanciation de votre DAO
        >>> id_eleve = 6
        >>> id_prof = 456
        >>> ma_liste.delete_liste_eleve(id_eleve, id_prof)
        """
        if not isinstance(id_professeur, int):
            raise TypeError("l'identifiant du professeur est un entier numérique")
        if not isinstance(id_eleve, int):
            raise TypeError("l'identifiant de l'élève est un entier numérique")
        if not UtilitaireDAO.check_user_exists(id_eleve):
            raise IdEleveInexistantError(id_eleve)
        if not UtilitaireDAO.check_user_exists(id_professeur):
            raise IdProfesseurInexistantError(id_professeur)

        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM base_projetinfo.liste_eleves "
                    "WHERE id_eleve = %(id_eleve)s AND id_professeur=%(id_professeur)s",
                    {"id_eleve": id_eleve, "id_professeur": id_professeur},
                )
                if cursor.rowcount == 0:
                    raise IdEleveInexistantError(id_eleve)

    def get_liste_eleve_by_id(self, id_professeur):
        """Pour obtenir la liste d'élèves du professeur.

        Parameters
        ----------
        id_prof : int
            L'identifiant du professeur à qui appartient la liste.

        Returns
        -------
        list of dict
        Une liste contenant les enregistrements d'élèves.
        Chaque enregistrement est représenté sous forme de dictionnaire.

        Examples
        --------
        >>> ma_liste = ListeElevesDAO()
        >>> id_professeur = 456
        >>> liste_eleves = ma_liste.get_liste_eleve_by_id(id_professeur)
        # On obtient une liste de dictionnaire qui contient l'identifiant,
        # nom et prénom de chaque élève
        """
        if not isinstance(id_professeur, int):
            raise TypeError("l'identifiant du professeur est un entier numérique")
        if not UtilitaireDAO.check_user_exists(id_professeur):
            raise IdProfesseurInexistantError(id_professeur)

        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    " FROM base_projetinfo.liste_eleves "
                    "WHERE id_professeur= %(id_professeur)s",
                    {"id_professeur": id_professeur},
                )
                liste_eleves = cursor.fetchall()
                if not liste_eleves:
                    print("La liste d'élèves est vide")
                result_list = []
                for eleve in liste_eleves:
                    eleve_dict = {
                        "id_eleve": eleve[0],
                        "nom": eleve[2],
                        "prenom": eleve[3],
                    }
                    result_list.append(eleve_dict)
        return result_list


    def delete_all_liste(self, id_professeur):
        """Pour vider la liste d'élèves d'un professeur.

        Parameters
        ----------
        id_prof : int
            L'identifiant du professeur dont la liste d'élèves doit être vidée.

        Examples
        --------
        >>> ma_liste = ListeElevesDAO()
        >>> id_professeur = 456
        >>> ma_liste.delete_all_liste(id_professeur)
        """
        if not isinstance(id_professeur, int):
            raise TypeError("L'identifiant du professeur doit être un entier numérique")
        if not UtilitaireDAO.check_user_exists(id_professeur):
            raise IdProfesseurInexistantError(id_professeur)

        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM base_projetinfo.liste_eleves "
                    "WHERE id_professeur = %(id_professeur)s",
                    {"id_professeur": id_professeur},
                )

