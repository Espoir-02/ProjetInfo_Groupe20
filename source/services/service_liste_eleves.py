from source.DAO.ListeEleveDAO import ListeElevesDAO


class ListeElevesService:
    def __init__(self):
        self.liste_eleves_dao = ListeElevesDAO()

    def ajouter_eleve_a_liste_eleves(self, eleve, id_professeur):
        return self.liste_eleves_dao.update_liste_eleve(eleve, id_professeur)

    def supprimer_eleve_de_liste_eleves(self, id_eleve, id_professeur):
        return self.liste_eleves_dao.delete_eleve(id_eleve, id_professeur)

    def consulter_liste_eleves(self, id_professeur):
        return self.liste_eleves_dao.get_liste_eleve_by_id(id_professeur)
