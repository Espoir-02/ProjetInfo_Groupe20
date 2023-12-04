import csv
from source.DAO.dbconnection import DBConnection

class ImporteurStageDAO:
    @staticmethod
    def importer_donnees(id_utilisateur, chemin_fichier_entree):
        try:
            with DBConnection().connection as conn:
                with open(chemin_fichier_entree, "r") as fichier_entree:
                    lecteur_csv = csv.reader(fichier_entree)
                    
                    # Lire la première ligne pour obtenir les noms de colonnes
                    colonnes = next(lecteur_csv)

                with conn.cursor() as cursor:
                    for ligne in lecteur_csv:
                        # Ligne est une liste de valeurs, chaque valeur correspond à une colonne dans le fichier CSV
                        donnees = ligne
                        
                        # Ajoutez l'identifiant de l'utilisateur aux données
                        donnees.insert(0, id_utilisateur)

                        # Utilisez une requête SQL fixe avec des paramètres
                        noms_colonnes = ", ".join([f"info{i}" for i in range(1, len(donnees))])
                        valeurs_parametres = ", ".join(["%s" for _ in range(len(donnees))])

                        query = (
                            f"INSERT INTO base_projetinfo.stage_import "
                            "(id_utilisateur, {noms_colonnes}) "
                            f"VALUES (%s, {valeurs_parametres})"
                        )

                        # Exécutez la requête avec les données
                        cursor.execute(query, donnees)

                    conn.commit()

            print(
                f"Les données ont été importées avec succès depuis la base de données vers {chemin_fichier_entree}."
            )

        except Exception as e:
            print(f"Une erreur s'est produite : {e}")


    @staticmethod
    def get_liste_stages_importes(id_utilisateur):
        """Pour récupérer la liste des stages importés par un utilisateur à partir de son identifiant.

        Parameters
        ----------
        id_utilisateur : int
            L'identifiant de l'utilisateur

        Returns
        -------
        list of dict
            La liste des stages importés par l'utilisateur.
            Chaque stage est représenté sous forme de dictionnaire.

        Examples
        --------
        >>> ma_liste_importee = ImporteurStageDAO()
        >>> id_utilisateur = 1
        >>> liste_stages_importes = ma_liste_importee.get_liste_stages_importes(id_utilisateur)
        >>> print(liste_stages_importes)
        # La liste des stages importés par l'utilisateur
        """
        if not isinstance(id_utilisateur, int):
            raise TypeError("L'identifiant de l'utilisateur doit être un entier numérique")

        try:
            with DBConnection().connection as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM base_projetinfo.stage_import WHERE id_utilisateur = %(id_utilisateur)s",
                        {"id_utilisateur": id_utilisateur},
                    )

                    stages_importes = cursor.fetchall()
                    if not stages_importes:
                        print("La liste des stages importés est vide")
                    
                    result_list = []
                    for stage in stages_importes:
                        stage_dict = {
                            "id_stage": stage[0],
                        }
                        # Ajoute les colonnes info au dictionnaire si elles ne sont pas vides
                        for i in range(1, min(len(stage), 11)):
                            if stage[i]:
                                stage_dict[f"info{i}"] = stage[i]
                        
                        result_list.append(stage_dict)
                    
            return result_list

        except Exception as e:
            print(f"Une erreur s'est produite lors de la récupération des stages importés : {e}")
            return None 
