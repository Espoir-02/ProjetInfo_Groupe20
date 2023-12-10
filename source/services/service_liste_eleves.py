from source.DAO.ListeEleveDAO import ListeElevesDAO
from source.DAO.utilitaire_dao import UtilitaireDAO
from source.exception.exceptions import IdEleveInexistantError
from prettytable import PrettyTable


class ListeElevesService:
    def __init__(self):
        self.liste_eleves_dao = ListeElevesDAO()
        self.utilitaire_dao = UtilitaireDAO

    def ajouter_eleve_a_liste_eleves(self, id_eleve, id_professeur):
        return self.liste_eleves_dao.update_liste_eleve(id_eleve, id_professeur)
        print("Élève ajouté avec succès.")

    def supprimer_eleve_de_liste_eleves(self, id_eleve, id_professeur):
        try:
            # Validation de l'ID de l'élève
            if not id_eleve:
                print("ID de l'élève non fourni.")
                return False

            try:
                id_eleve = int(id_eleve)
            except ValueError:
                print("Veuillez entrer un ID d'élève valide.")
                return False

            # Validation de l'existence de l'élève
            if not self.utilitaire_dao.check_user_exists(id_eleve):
                raise IdEleveInexistantError(id_eleve)

            success = self.liste_eleves_dao.delete_eleve(id_eleve, id_professeur)

            if success:
                print(f"Suppression de l'élève avec l'ID {id_eleve} réussie.")
            else:
                print("Erreur lors de la suppression de l'élève.")
            return success

        except IdEleveInexistantError as e:
            print(f"Erreur lors de la suppression de l'élève : {e}")
            return False

    def consulter_liste_eleves(self, id_professeur):
        liste_eleves = self.liste_eleves_dao.get_liste_eleve_by_id(id_professeur)

        if liste_eleves:
            table = PrettyTable()
            table.field_names = ["ID Élève", "Nom", "Prénom"]

            for eleve in liste_eleves:
                table.add_row([eleve["id_eleve"], eleve["nom"], eleve["prenom"]])
            print(table)
        else:
            print("La liste d'élèves est vide.")

    def vider_liste_eleves(self, id_professeur):
        if not self.utilitaire_dao.check_liste_eleves_exists(id_professeur):
            print("La liste d'élèves est déjà vide.")
            return False
        else:
            succes = self.liste_eleves_dao.delete_all_liste(id_professeur)
            if succes:
                print("Liste vidée avec succès")
            else:
                print("Erreur lors de la suppression de la liste")
            return succes

    def verifier_eleve_dans_liste(self, id_eleve, id_professeur):
        return self.utilitaire_dao.check_eleve_exist_dans_liste(id_eleve, id_professeur)

    def get_liste_eleves(self, id_professeur):
        return self.liste_eleves_dao.get_liste_eleve_by_id(id_professeur)