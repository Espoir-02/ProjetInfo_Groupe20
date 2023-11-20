from source.DAO.ListeEnvieDAO import ListeEnvieDAO
from source.DAO.utilitaire_dao import UtilitaireDAO
from source.exception.exceptions import IdStageInexistantError
from prettytable import PrettyTable

class ListeEnvieService:
    def __init__(self):
        self.liste_envie_dao = ListeEnvieDAO()
        self.utilitaire_dao = UtilitaireDAO()

    def ajouter_stage_a_liste_envie(self, id_eleve, id_stage):
        return self.liste_envie_dao.update_liste_envie(id_eleve, id_stage)

    def supprimer_stage_de_liste_envie(self, id_eleve, id_stage):
        try:
            if not self.utilitaire_dao.check_stage_exists(id_stage):
                raise IdStageInexistantError(id_stage)

            print("Stage supprimé avec succès de la liste d'envie")
            return self.liste_envie_dao.delete_liste_envie(id_eleve, id_stage)
        except IdStageInexistantError as e:
            print(f"Erreur lors de la suppression du stage dans la liste d'envie : {e}")

    def vider_liste_envie_eleve(self, id_eleve):
        print("Liste d'envie supprimée avec succès")
        return self.liste_envie_dao.delete_all_liste_envie(id_eleve)

    def get_liste_envie_eleve(self, id_eleve):
        liste_envie= self.liste_envie_dao.get_liste_envie_by_id(id_eleve)
        if liste_envie:
            table = PrettyTable()
            table.field_names = ["ID Stage", "Titre", "Lien", "Domaine"]

            # Ajustez la largeur maximale des colonnes
            MAX_WIDTH = 50
            for envie in liste_envie:
                table.add_row([
                    envie["id_stage"],
                    ListeEnvieService.truncate_text(envie["titre"], MAX_WIDTH),
                    ListeEnvieService.truncate_text(envie["lien"], MAX_WIDTH),
                    ListeEnvieService.truncate_text(envie["domaine"], MAX_WIDTH),
                ])

            print(table)
        else:
            print("La liste d'envies est vide.")

    @staticmethod
    def truncate_text(text, max_width):
        """Tronque le texte si sa longueur dépasse la largeur maximale."""
        return (text[:max_width] + '...') if len(text) > max_width else text

    
        