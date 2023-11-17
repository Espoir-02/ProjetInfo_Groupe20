from InquirerPy import inquirer
from source.view.Page_option.recherche_stage_view import Recherche_Stage_View
from source.services.service_utilisateur import UtilisateurService
from source.DAO.StageDAO import StageDAO
from source.services.service_historique import HistoriqueService
from source.view.session_view import Session
import inquirer

class HistoriqueView:
    def display(self):

        # Récupérez l'historique de l'utilisateur à partir de son identifiant
        historique_service = HistoriqueService()
        historique = historique_service.get_all_historique_by_id(Session().user_id)

        if not historique:
            print("L'historique est vide.")
            from source.view.Page_option.menu_view import Menu_view
            return Menu_view()
        
        else :
            option = []
            for element in historique :
                stage_service = StageService()
                stage = stage_service.find_stage_by_id(element["id_stage"])
                stage_info = f"ID du stage : {element['id_stage']}, Nom du stage : {stage['titre']}, Nom de l'entreprise : {stage['entreprise']}"
                # Date de consultation : {element['date_consultation']}, 
                # On rempli la liste d'affichage
                option.append(inquirer.Option(f"{index}", stage_info)) 
            
            #Ajout de l'option pour retourner au menu
            option.append(inquirer.Option(str(len(historique) + 1), "Retourner au menu"))

            # Affichage de la liste
            answers = inquirer.prompt([inquirer.List("Stage vu précedemment", "Consulter son historique :", option)])
            num_selection = int(answers["Stage vu précedemment"])
            
            if num_selection == len(historique) + 1:
                # Retourner au menu principal
                from source.view.Page_option.menu_view import Menu_view
                return Menu_view()
            
            element_selection_historique = historique[num_selection - 1]
        
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
