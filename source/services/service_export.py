from source.DAO.dbconnection import DBConnection
from source.DAO.utilitaire_dao import UtilitaireDAO
from source.exception.exceptions import IdUtilisateurInexistantError
from source.exception.exceptions import IdStageInexistantError

class ExporteurStage:
    @staticmethod
    def exporter_donnees(id_utilisateur, id_stage, chemin_fichier_sortie):
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM base_projetinfo.stage "
                    "WHERE id_stage = %(id_stage)s",
                    {"id_stage": id_stage},
                )

                # Récupération des résultats
                resultats = cursor.fetchall()
                print(resultats)

                 # Écriture des résultats dans un fichier texte
                try:
                    with open(chemin_fichier_sortie, 'w') as fichier_sortie:
                        for resultat in resultats:
                            print("Seul:", resultat)
                            ligne = ', '.join(str(colonne) for colonne in resultat)
                            print("Ma ligne:", ligne)
                            fichier_sortie.write(f"{ligne}\n")  # Écriture des résultats dans un fichier texte
                except Exception as e:
                    print("Erreur lors de l'écriture dans le fichier :", str(e))


       # print(f"Les données ont été exportées avec succès vers {chemin_fichier_sortie}.")

# Remplacez ces valeurs par les informations spécifiques de l'utilisateur
id_utilisateur = 18
id_stage = 746
chemin_fichier_sortie = f'{id_utilisateur}_fichierExport.csv'

# Exporter les données pour cet utilisateur
ExporteurStage.exporter_donnees(id_utilisateur, id_stage, chemin_fichier_sortie)
