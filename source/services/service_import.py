from source.DAO.ImportDAO import ImporteurStageDAO


class ImporteurStage:
    @staticmethod
    def importer_donnees(id_utilisateur, chemin_fichier_entree):
        importer = ImporteurStageDAO()
        importer.importer_donnees(id_utilisateur, chemin_fichier_entree)

# Remplacez ces valeurs par les informations spécifiques de l'utilisateur
#id_utilisateur = "id_utilisateur"
#chemin_fichier_entree = f"chemin/vers/{id_utilisateur}_fichier.txt"


