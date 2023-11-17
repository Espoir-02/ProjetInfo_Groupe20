from source.DAO.dbconnection import DBConnection
from source.DAO.utilitaire_dao import UtilitaireDAO
from source.exception.exceptions import IdUtilisateurInexistantError
from source.exception.exceptions import IdStageInexistantError

class ImporteurStage:
    @staticmethod
    def importer_donnees(id_utilisateur, id_stage, chemin_fichier_entree):
        try:
            # Établir la connexion à la base de données
            with DBConnection().connection as conn:
                with conn.cursor() as cursor:
                    # Exécuter la requête SQL pour récupérer les données du stage spécifié
                    cursor.execute(
                        "SELECT * FROM base_projetinfo.stage "
                        "WHERE id_stage = %(id_stage)s",
                        {"id_stage": id_stage},
                    )

                    # Récupération des résultats
                    resultats = cursor.fetchall()

                    # Fermeture de la connexion à la base de données
                    cursor.close()
                    conn.close() 

            # Écriture des résultats dans un fichier texte
            with open(chemin_fichier_entree, 'w') as fichier_entree:
                for resultat in resultats:
                    ligne = ', '.join(str(colonne) for colonne in resultat)
                    fichier_entree.write(f"{ligne}\n")

            print(f"Les données ont été importées avec succès depuis la base de données vers {chemin_fichier_entree}.")

        except IdStageInexistantError:
            print(f"L'ID de stage {id_stage} n'existe pas dans la base de données.")
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

# Remplacez ces valeurs par les informations spécifiques de l'utilisateur
id_utilisateur = 'id_utilisateur'
id_stage = 'id_stage'
chemin_fichier_entree = f'chemin/vers/{id_utilisateur}_fichier.txt'

# Importer les données pour cet utilisateur
ImporteurStage.importer_donnees(id_utilisateur, id_stage, chemin_fichier_entree)