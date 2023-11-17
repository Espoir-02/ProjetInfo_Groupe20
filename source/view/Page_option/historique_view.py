from InquirerPy import inquirer
from source.services.service_historique import HistoriqueService
from source.view.session_view import Session
import inquirer 

class HistoriqueView:

    def display(self):

        # Récupérez l'historique de l'utilisateur à partir de son identifiant
        historique_service = HistoriqueService()
        historique = historique_service.get_all_historique_by_id(Session().user_id)

        option = []
        for element in historique :
            stage_service = StageService()
            stage = stage_service.find_stage_by_id(element["id_stage"])
            stage_info = f"ID du stage : {element['id_stage']}, Nom du stage : {stage['titre']}, Nom de l'entreprise : {stage['entreprise']}"
            #Date de consultation : {element['date_consultation']}, 
            #On rempli la liste d'affichage
            option.append(inquirer.Option(f"{index}", stage_info)) 
        
        #On affiche la liste
        answers = inquirer.prompt([inquirer.List("Stage vu précedemment", "Consulter son historique :", options)])
        #Les stages seront choisit avec leur numéro de stage
        num_selection = int(answers["Stage vu précedemment"])
        #
        element_selection_historique = historique[num_selection - 1]

        #Les details du stage seront différent en fonction du type d'utilisateur 



        if Session().user_type == "eleve":
            id_stage = element_selection_historique["id_stage"]
            from source.view.Page_detail.detail_stage_view import detail_stage_view_eleve
            detail_view = detail_stage_view_eleve(id_stage)
            return detail_view

        elif Session().user_type == "prof":
            id_stage = element_selection_historique["id_stage"]
            from source.view.Page_detail.detail_stage_view import detail_stage_view_prof
            detail_view = detail_stage_view_prof(id_stage)
            return detail_view
        
        else:
            detail_view = detail_stage_view_invite["id_stage"]
            return detail_view
    
    def make_choice(self):
        return self.display()