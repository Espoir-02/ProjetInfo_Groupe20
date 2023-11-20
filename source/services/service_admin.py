from source.DAO.utilisateur_dao import UtilisateurDAO
from source.DAO.utilitaire_dao import UtilitaireDAO
from source.exception.exceptions import IdUtilisateurInexistantError, IdStageInexistantError
from source.DAO.StageDAO import StageDAO
from prettytable import PrettyTable


class ServiceAdmin:
    def __init__(self):
        self.utilisateur_dao = UtilisateurDAO()
        self.utilitaire_dao = UtilitaireDAO()
        self.stage_dao = StageDAO()

    def supprimer_utilisateur(self, id_utilisateur):
        try:
            if not self.utilitaire_dao.check_user_exists(id_utilisateur):
                raise IdUtilisateurInexistantError(id_utilisateur)

            print("Utilisateur supprimé avec succès.")
            return self.utilisateur_dao.delete_utilisateur(id_utilisateur)
        except IdUtilisateurInexistantError as e:
            print(f"Erreur lors de la suppression de l'utilisateur : {e}")
        
        

    def obtenir_liste_utilisateurs(self):
        liste = self.utilisateur_dao.get_all_utilisateurs()
        if liste:
            table = PrettyTable()
            table.field_names = ["ID Utilisateur", "Nom", "Prénom", "Pseudo", "Mot de passe", "Type Utilisateur"]

            for utilisateur in liste:
                table.add_row([
                    utilisateur["id_utilisateur"],
                    utilisateur["nom"],
                    utilisateur["prenom"],
                    utilisateur["pseudo"],
                    utilisateur["mot_de_passe"],
                    utilisateur["type_utilisateur"]
                ])

            print(table)
        else:
            print("La liste d'utilisateurs est vide.")
    

    def supprimer_stage(self, id_stage):
        try:
            if not self.utilitaire_dao.check_stage_exists(id_stage):
                raise IdStageInexistantError(id_stage)

            print("Stage supprimé avec succès.")
            return self.stage_dao.delete_stage(id_stage)
        except IdStageInexistantError as e:
            print(f"Erreur lors de la suppression du stage : {e}")

        

    def obtenir_liste_stages(self):
        liste_stages = self.stage_dao.get_all_stages()
        if liste_stages:
            table = PrettyTable()
            table.field_names = [
                "ID Stage", "Titre", "Lien", "Domaine", "Salaire", 
                "Date de Publication", "Période", "Niveau d'Études", 
                "Entreprise", "Lieu"
            ]

            # Ajustez la largeur maximale des colonnes
            max_width=20
            for stage in liste_stages:
                table.add_row([
                    stage["id_stage"],
                    ServiceAdmin.truncate_text(stage["titre"], 20),
                    ServiceAdmin.truncate_text(stage["lien"], 20),
                    ServiceAdmin.truncate_text(stage["domaine"], max_width),
                    ServiceAdmin.truncate_text(stage["salaire"], max_width),
                    ServiceAdmin.truncate_text(stage["date_publication"], max_width),
                    ServiceAdmin.truncate_text(stage["periode"], max_width),
                    ServiceAdmin.truncate_text(stage["niveau_etudes"], max_width),
                    ServiceAdmin.truncate_text(stage["entreprise"], max_width),
                    ServiceAdmin.truncate_text(stage["lieu"], max_width),
                ])

            print(table)
        else:
            print("Aucun stage trouvé dans la base de données.")

    @staticmethod
    def truncate_text(text, max_width):
        """Tronque le texte si sa longueur dépasse la largeur maximale."""
        if text is None:
            return ""
        return (text[:max_width] + '...') if len(text) > max_width else text
