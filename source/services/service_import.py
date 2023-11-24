from source.DAO.dbconnection import DBConnection
from source.DAO.utilitaire_dao import UtilitaireDAO
from source.exception.exceptions import IdUtilisateurInexistantError
from source.exception.exceptions import IdStageInexistantError


class ImporteurStage:
    @staticmethod
    def importer_donnees(id_utilisateur, chemin_fichier_entree):
        try:
            # Établir la connexion à la base de données
            with DBConnection().connection as conn:
                with open(chemin_fichier_entree, "r") as fichier_entree:
                    lignes = fichier_entree.readlines()

                with conn.cursor() as cursor:
                    for ligne in lignes:
                        valeurs = ligne.strip().split(", ")
                        id_utilisateur = valeurs[0]
                        cursor.execute(
                            "INSERT INTO base_projetinfo.stage_import (id_utilisateur, lieu, salaire) "  # rajouter d'autres colonnes
                            "VALUES (%s, %s, %s)",
                            (id_utilisateur, valeurs[1], valeurs[2]),
                        )

                    # Validation de la transaction
                    conn.commit()

                    # Fermeture de la connexion à la base de données
                    cursor.close()
                    conn.close()

            print(
                f"Les données ont été importées avec succès depuis la base de données vers {chemin_fichier_entree}."
            )

        except Exception as e:
            print(f"Une erreur s'est produite : {e}")


# Remplacez ces valeurs par les informations spécifiques de l'utilisateur
id_utilisateur = "id_utilisateur"
chemin_fichier_entree = f"chemin/vers/{id_utilisateur}_fichier.txt"

# Importer les données pour cet utilisateur
ImporteurStage.importer_donnees(id_utilisateur, chemin_fichier_entree)
