from InquirerPy import inquirer
from source.view.Page_option.recherche_stage_view import Recherche_Stage_View
from source.services.service_utilisateur import UtilisateurService
from source.DAO.StageDAO import StageDAO
from source.services.service_historique import HistoriqueService
from source.view.session_view import Session
import inquirer

class HistoriqueView:
    def __init__(self):
        self.id_user = Session().user_id

    def display(self):

        # Récupérez l'historique de l'utilisateur à partir de son identifiant
        historique_service = HistoriqueService()
        historique = historique_service.get_all_historique_by_id(self.id_user)

        option = []
        for element in historique :
            stage_service = StageService()
            stage = stage_service.find_stage_by_id(element["id_stage"])
            stage_info = f"ID du stage : {element['id_stage']}, Nom du stage : {stage['titre']}, Nom de l'entreprise : {stage['entreprise']}"
            # Date de consultation : {element['date_consultation']}, 
            #On rempli la liste d'affichage
            option.append(inquirer.Option(f"{index}", stage_info)) 
        
        # On affiche la liste
        """answers = inquirer.prompt([inquirer.List("Stage vu précedemment", "Consulter son historique :", options)])

        num_selection = int(answers["Stage vu précedemment"])
        element_selection_historique = historique[num_selection - 1]" """

        #Les details du stage seront différent en fonction du type d'utilisateur 

        utilisateur_service =UtilisateurService()
        utilisateur = utilisateur_service.find_by_id(self.id_user)

        if utilisateur.type_utilisateur == "eleve":
            id_stage = element_selection_historique["id_stage"]
            from source.view.Page_detail.detail_stage_view import detail_stage_view_eleve
            detail_view = detail_stage_view_eleve(id_stage)
            return detail_view.display()

        elif utilisateur.type_utilisateur == "prof":
            id_stage = element_selection_historique["id_stage"]
            from source.view.Page_detail.detail_stage_view import detail_stage_view_prof
            detail_view = detail_stage_view_prof(id_stage)
            return detail_view.display()
        
        else:
            detail_view = detail_stage_view_invite["id_stage"]
            return detail_view.display()