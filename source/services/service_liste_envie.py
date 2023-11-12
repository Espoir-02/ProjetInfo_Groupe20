from source.DAO.ListeEnvieDAO import ListeEnvieDAO

class ListeEnvieService:
    def __init__(self):
        self.ListeEnvieDAO = ListeEnvieDAO()

    def ajouter_stage_a_liste_envie(self, id_eleve, id_stage):
        """
        Ajoute un stage à la liste d'envies d'un élève.

        Parameters:
        id_eleve (int): L'identifiant de l'élève.
        id_stage (int): L'identifiant du stage à ajouter.

        Returns:
        bool: True si l'ajout a réussi, False sinon.
        """
        return self.ListeEnvieDAO.update_liste_envie(id_eleve, id_stage)

    def supprimer_stage_de_liste_envie(self, id_eleve, id_stage):
        """
        Supprime un stage de la liste d'envies d'un élève.

        Parameters:
        id_eleve (int): L'identifiant de l'élève.
        id_stage (int): L'identifiant du stage à supprimer.

        Returns:
        bool: True si la suppression a réussi, False sinon.
        """
        return self.ListeEnvieDAO.delete_liste_envie(id_eleve, id_stage)

    def get_liste_envie_eleve(self, id_eleve):
        """
        Récupère la liste d'envies d'un élève.

        Parameters:
        id_eleve (int): L'identifiant de l'élève.

        Returns:
        list of dict: Une liste contenant les informations des stages dans la liste d'envies.
        """
        return self.ListeEnvieDAO.get_liste_envie_by_id(id_eleve)

    def vider_liste_envie_eleve(self, id_eleve):
        """
        Vide la liste d'envies d'un élève.

        Parameters:
        id_eleve (int): L'identifiant de l'élève.

        Returns:
        bool: True si la suppression a réussi, False sinon.
        """
        #OPTIONNELLE Pas encore fait 