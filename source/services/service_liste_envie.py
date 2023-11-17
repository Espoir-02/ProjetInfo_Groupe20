from source.DAO.ListeEnvieDAO import ListeEnvieDAO
from prettytable import PrettyTable

class ListeEnvieService:
    def __init__(self):
        self.liste_envie_dao = ListeEnvieDAO()

    def ajouter_stage_a_liste_envie(self, id_eleve, id_stage):
        return self.liste_envie_dao.update_liste_envie(id_eleve, id_stage)

    def supprimer_stage_de_liste_envie(self, id_eleve, id_stage):
        return self.liste_envie_dao.delete_liste_envie(id_eleve, id_stage)

    def get_liste_envie_eleve(self, id_eleve):
        liste_envie= self.liste_envie_dao.get_liste_envie_by_id(id_eleve)
        if liste_envie:
            table = PrettyTable()
            table.field_names = ["ID Stage", "Titre", "Lien", "Domaine"]

            for envie in liste_envie:
                table.add_row([envie["id_stage"], envie["titre"], envie["lien"], envie["domaine"]])

            print(table)
        else:
            print("La liste d'envies est vide.")

    def vider_liste_envie_eleve(self, id_eleve):
        """
        Vide la liste d'envies d'un élève.
        """
        #OPTIONNELLE Pas encore fait 