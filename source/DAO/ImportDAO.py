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
