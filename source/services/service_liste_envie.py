from source.DAO.ListeEnvieDAO import ListeEnvieDAO

class ListeEnvieService:
    def __init__(self):
        self.ListeEnvieDAO = ListeEnvieDAO()

    def ajouter_stage_a_liste_envie(self, id_eleve, id_stage):
        return self.ListeEnvieDAO.update_liste_envie(id_eleve, id_stage)

    def supprimer_stage_de_liste_envie(self, id_eleve, id_stage):
        return self.ListeEnvieDAO.delete_liste_envie(id_eleve, id_stage)

    def get_liste_envie_eleve(self, id):
        return self.ListeEnvieDAO.get_liste_envie_by_id(id)

    def vider_liste_envie_eleve(self, id_eleve):
        """
        Vide la liste d'envies d'un élève.
        """
        #OPTIONNELLE Pas encore fait 