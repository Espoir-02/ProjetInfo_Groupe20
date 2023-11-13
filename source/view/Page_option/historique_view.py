from InquirerPy import inquirer
from source.view.couche2menu.recherche_stage_view import Recherche_Stage_View
from source.DAO.HistoriqueDAO import HistoriqueDAO
from source.DAO.UtilisateurDAO import UtilisateurDAO
from source.DAO.StageDAO import StageDAO
from source.view.couche3sousmenu.detail_stage_view import detail_stage_view_eleve
from source.view.couche3sousmenu.detail_stage_view import detail_stage_view_prof

class HistoriqueView:
    def __init__(self,id_utilisateur):
        self.id_utilisateur = id_utilisateur

    def display(self):

        # Récupérez l'historique de l'utilisateur à partir de son identifiant
        historique_dao = HistoriqueDAO()
        historique = historique_dao.get_all_historique_by_id(self.id_utilisateur)

        option = []
        for element in historique :
            #On récupère le stage par son id 
            stage = StageDAO().find_stage_by_id(element["id_stage"])
            #On précise les informations du stage à afficher 
            stage_info = f"Date de consultation : {element['date_consultation']}, ID du stage : {element['id_stage']}, Nom du stage : {stage['titre']}, Nom de l'entreprise : {stage['entreprise']}"
            #On rempli la liste d'affichage
            option.append(inquirer.Option(f"{index}", stage_info)) 
        
        # On affiche la liste
        answers = inquirer.prompt([inquirer.List("Stage vu précedemment", "Consulter son historique :", options)])

        num_selection = int(answers["Stage vu précedemment"])
        element_selection_historique = historique[num_selection - 1]

        #Les details du stage seront différent en fonction du type d'utilisateur 

        utilisateur = UtilisateurDAO.find_by_id(self.id_utilisateur)

        if utilisateur.type_utilisateur == "eleve":
            id_stage = element_selection_historique["id_stage"]
            detail_view = detail_stage_view_eleve(id_stage)
            return detail_view.display()

        elif utilisateur.type_utilisateur == "prof":
            id_stage = element_selection_historique["id_stage"]
            detail_view = detail_stage_view_prof(id_stage)
            return detail_view.display()