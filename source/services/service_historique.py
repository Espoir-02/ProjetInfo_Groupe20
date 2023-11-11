from source.DAO.HistoriqueDAO import HistoriqueDAO
from source.DAO.utilisateur_dao import UtilisateurDAO
from source.view.couche3sousmenu.detail_stage_view import detail_stage_view_eleve, detail_stage_view_prof
from InquirerPy import inquirer
from source.DAO.StageDAO import StageDAO

class HistoriqueService:
    def __init__(self):
        self.historique_dao = HistoriqueDAO()

    def get_all_historique_by_id(self, id_utilisateur):
        """
        Récupère tout l'historique d'un utilisateur à partir de son identifiant.

        Parameters
        ----------
        id_utilisateur : int
            L'identifiant de l'utilisateur.

        Returns
        -------
        list of dict
            Une liste contenant les recherches qui constituent l'historique.
            Chaque recherche est représentée sous forme de dictionnaire.
        """
        return self.historique_dao.get_all_historique_by_id(id_utilisateur)

    def consulter_historique(self, id_utilisateur):
        """
        Affiche l'historique de l'utilisateur et permet de consulter des stages consultés précédemment.

        Parameters
        ----------
        id_utilisateur : int
            L'identifiant de l'utilisateur.

        Returns
        -------
        None
        """
        # Récupère l'historique de l'utilisateur
        historique = self.get_all_historique_by_id(id_utilisateur)
        options = []

        # Affiche les éléments de l'historique
        for index, element in enumerate(historique, start=1):
            stage = StageDAO().find_stage_by_id(element["id_stage"])
            stage_info = f"Date de consultation : {element['date_consultation']}, ID du stage : {element['id_stage']}, Nom du stage : {stage['titre']}, Nom de l'entreprise : {stage['entreprise']}"
            options.append(inquirer.Option(str(index), stage_info))

        # Vérifie si l'historique est vide
        if not options:
            print("L'historique est vide.")
        else:
            # Permet à l'utilisateur de choisir un stage dans l'historique
            answers = inquirer.prompt([inquirer.List("Stage consulté précédemment", "Consulter son historique :", options)])
            num_selection = int(answers["Stage consulté précédemment"])
            element_selection_historique = historique[num_selection - 1]

            # Récupère le type de l'utilisateur
            utilisateur = UtilisateurDAO.find_by_id(id_utilisateur)
            id_stage = element_selection_historique["id_stage"]

            if utilisateur.type_utilisateur == "eleve":
                # Si l'utilisateur est un élève, affiche les détails du stage comme un élève
                detail_view = detail_stage_view_eleve(id_stage)
                return detail_view.display()
            elif utilisateur.type_utilisateur == "prof":
                # Si l'utilisateur est un professeur, affiche les détails du stage comme un professeur
                detail_view = detail_stage_view_prof(id_stage)
                return detail_view.display()
