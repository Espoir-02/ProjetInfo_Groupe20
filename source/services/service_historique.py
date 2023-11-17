from source.DAO.HistoriqueDAO import HistoriqueDAO
from source.DAO.utilisateur_dao import UtilisateurDAO
from source.DAO.StageDAO import StageDAO
from prettytable import PrettyTable

class HistoriqueService:
    def __init__(self):
        self.historique_dao = HistoriqueDAO()

    def get_all_historique_by_id(self, id_utilisateur):
        liste_historique = self.historique_dao.get_all_historique_by_id(id_utilisateur)
        if liste_historique:
            table = PrettyTable()
            table.field_names = ["ID Stage", "Titre", "Lien", "Domaine"]

            for recherche in liste_historique:
                table.add_row([recherche["id_stage"], recherche["titre"], recherche["lien"], recherche["domaine"]])

            print(table)
        else:
            print("L'historique est vide.")

    def ajouter_stage_a_historique(self, id_utilisateur,stage_id):
        return self.utilisateur_dao.update_historique(id_utilisateur, stage_id)
       
