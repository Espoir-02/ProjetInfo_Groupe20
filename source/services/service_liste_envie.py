from source.DAO.ListeEnvieDAO import ListeEnvieDAO

class ListeEnvieService:
    def __init__(self):
        self.liste_envie_dao = ListeEnvieDAO()

    def ajouter_stage_a_liste_envie(self, id_eleve, id_stage):
        return self.liste_envie_dao.update_liste_envie(id_eleve, id_stage)

    def supprimer_stage_de_liste_envie(self, id_eleve, id_stage):
        return self.liste_envie_dao.delete_liste_envie(id_eleve, id_stage)

    def get_liste_envie_eleve(self, id_eleve):
        return self.liste_envie_dao.get_liste_envie_by_id(id_eleve)

    def vider_liste_envie_eleve(self, id_eleve):
        """
        Vide la liste d'envies d'un élève.
        """
        #OPTIONNELLE Pas encore fait 