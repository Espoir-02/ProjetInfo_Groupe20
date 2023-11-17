from source.DAO.dbconnection import DBConnection
from source.DAO.utilitaire_dao import UtilitaireDAO
from source.exception.exceptions import IdUtilisateurInexistantError
from source.exception.exceptions import IdStageInexistantError


class ExporteurStage:
   
    def exporter_donnees(self, id_utilisateur, id_stage, chemin_fichier_sortie):
        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT *  FROM base_projetinfo.stage; "
                    "WHERE id_stage = %(id_stage)s",
                    {"id_stage": id_stage},
                )

        # Récupération des résultats
        resultats = cursor.fetchall()

        # Fermeture de la connexion à la base de données
        cursor.close()
        conn.close()            

        # Écriture des résultats dans un fichier texte
        with open(chemin_fichier_sortie, 'w') as fichier_sortie:
            for resultat in resultats:
                ligne = ', '.join(str(colonne) for colonne in resultat)
                fichier_sortie.write(f"{ligne}\n")

        print(f"Les données ont été exportées avec succès vers {chemin_fichier_sortie}.")


# Remplacez ces valeurs par les informations spécifiques de l'utilisateur
id_utilisateur = 'id_utilisateur'
id_stage=
chemin_fichier_sortie = f'chemin/vers/{id_utilisateur}_fichier.txt'

# Exporter les données pour cet utilisateur
ExporteurStage.exporter_donnees(id_utilisateur, id_stage, chemin_fichier_sortie)
