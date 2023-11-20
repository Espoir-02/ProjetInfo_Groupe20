from source.DAO.ListeEleveDAO import ListeElevesDAO
from source.DAO.utilitaire_dao import UtilitaireDAO
from source.exception.exceptions import IdEleveInexistantError
from prettytable import PrettyTable


class ListeElevesService:
    def __init__(self):
        self.liste_eleves_dao = ListeElevesDAO()
        self.utilitaire_dao = UtilitaireDAO

    def ajouter_eleve_a_liste_eleves(self, eleve, id_professeur):
        return self.liste_eleves_dao.update_liste_eleve(eleve, id_professeur)
        print("Élève ajouté avec succès.")


    def supprimer_eleve_de_liste_eleves(self, id_eleve, id_professeur):
        try:
            if not self.utilitaire_dao.check_user_exists(id_eleve):
                raise IdEleveInexistantError(id_eleve)

            print("Élève supprimé avec succès.")
            return self.liste_eleves_dao.delete_eleve(id_eleve, id_professeur)
        except IdEleveInexistantError as e:
            print(f"Erreur lors de la suppression de l'élève : {e}")
        


    def consulter_liste_eleves(self, id_professeur):
        liste_eleves= self.liste_eleves_dao.get_liste_eleve_by_id(id_professeur)

        if liste_eleves:
            table = PrettyTable()
            table.field_names = ["ID Élève", "Nom", "Prénom"]

            for eleve in liste_eleves:
                table.add_row([eleve["id_eleve"], eleve["nom"], eleve["prenom"]])
            print(table)
        else:
            print("La liste d'élèves est vide.")

        """print("Liste des élèves :")
        for eleve in liste_eleves:
            print(eleve)"""




