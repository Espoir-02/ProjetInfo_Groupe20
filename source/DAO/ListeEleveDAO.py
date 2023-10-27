from source.DAO.dbconnection import DBConnection
from source.exception.exceptions import IdEleveInexistantError


class ListeElevesDAO:
    def update_liste_eleve(self, eleve, id_prof):
        """Pour ajouter un élève à la liste d'élèves d'un professeur en particulier.

        Parameters
        ----------
        eleve: Eleve
            L'élève qui va être ajouté
        id_prof : int
            L'identifiant du professeur à qui appartient la liste

         Examples
        --------
        >>> ma_liste = ListeElevesDAO()  
        >>> eleve = Eleve(nom="Millepertuis", prenom="Iris", id_eleve=6)  
        >>> id_prof = 456  
        >>> ma_liste.update_liste_eleve(eleve, id_prof)
        ----------
        """
        if not isinstance(id_prof, int):
            raise TypeError("l'identifiant du professeur est un entier numérique")
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
        """Pour supprimer un élève de la liste d'élèves d'un professeur donné.
        
        Parameters
        ----------
        id_eleve : int
            L'identifiant de l'élève à supprimer.
        id_prof : int
            L'identifiant du professeur à qui appartient la liste

         Examples
        --------
        >>> ma_liste = ListeEleveDAO()  # Instanciation de votre DAO
        >>> id_eleve = 6
        >>> id_prof = 456 
        >>> ma_liste.delete_liste_eleve(id_eleve, id_prof)
        """
        if not isinstance(id_prof, int):
            raise TypeError("l'identifiant du professeur est un entier numérique")
        if not isinstance(id_eleve, int):
            raise TypeError("l'identifiant de l'élève est un entier numérique")
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
        >>> ma_liste = ListeEleveDAO()  
        >>> id_prof = 456  
        >>> liste_eleves = ma_liste.get_liste_eleve_by_id(id_prof)
        >>> for eleve in liste_eleves:
        ...     print(f"Nom: {eleve['nom']}, Prénom: {eleve['prénom']}")
        """
        if not isinstance(id_prof, int):
            raise TypeError("l'identifiant du professeur est un entier numérique")
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
