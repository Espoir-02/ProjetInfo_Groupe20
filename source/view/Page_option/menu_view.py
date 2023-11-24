from source.view.Page_option.recherche_stage_view import Recherche_Stage_View
from source.view.Page_option.historique_view import HistoriqueView
from source.view.Page_option.Liste_envie_view import ListeEnvieView 
from source.view.Page_option.proposition_prof_view import Proposition_prof_view
from source.view.Page_option.suggestions_eleve_view import SuggestionEleveView
from source.view.Page_option.liste_eleves_view import ListeElevesView
from source.view.Page_option.historique_view import HistoriqueView
from source.services.service_utilisateur import ServiceUtilisateur  
from source.view.Page_option.admin_view import AdminView
from source.view.session_view import Session 
import inquirer

class Menu_view:
    def __init__(self):
        self.utilisateur_service = ServiceUtilisateur()

    def display(self):
        pseudo = Session().user_pseudo
        type_utilisateur = Session().user_type
        id_professeur= Session().user_id
        id_eleve = Session().user_id
        id_utilisateur = Session().user_id
        

        while True:

            choices = ['Rechercher un stage', 'Accéder à son historique', "Quitter l'application"]

            if Session().user_type in ['professeur', 'eleve', 'administrateur']:
                choices.append("Accéder à sa liste d'envie")
        
            if Session().user_type == 'eleve':
                choices.append("Accéder à la liste de suggestions du professeur")

            if Session().user_type == 'professeur':
                choices.append("Accéder à la liste d'élèves")

            if Session().user_type == 'administrateur':
                choices.append("Accéder aux fonctions administrateur")

            if Session().user_type in ['professeur', 'eleve', 'administrateur']:
                choices.append("Modifier ses informations")
            
            if Session().user_type in ['professeur', 'eleve', 'administrateur']:
                choices.append("Déconnexion")
            
            if Session().user_type in ['professeur', 'eleve', 'administrateur']:
                choices.append("Voir mes informations")

            questions = [inquirer.List('choice', message='Choisir une option:', choices=choices)]

            answers = inquirer.prompt(questions)

            if answers['choice'] == 'Rechercher un stage':
                return Recherche_Stage_View().display()
        
            elif answers['choice'] == 'Accéder à son historique':
                historique_view = HistoriqueView()
                return historique_view.display()

            elif (Session().user_type in ['professeur', 'eleve', 'administrateur']) and (answers['choice'] == "Accéder à sa liste d'envie"):
                liste_envie_view= ListeEnvieView(id_utilisateur)
                return liste_envie_view.display()
                """from source.view.Page_option.view_envie2_essaie import ListeEnvieView
                return ListeEnvieView(Session().user_id).display()"""

            elif (Session().user_type in ['professeur', 'eleve', 'administrateur']) and (answers['choice'] == "Modifier ses informations"):
                from source.view.Page_option.maj_utilisateur_view import MajUtilisateurView
                maj_utilisateur_view = MajUtilisateurView(pseudo)
                return maj_utilisateur_view.display()
            
            elif (Session().user_type in ['professeur', 'eleve', 'administrateur']) and (answers['choice'] == "Déconnexion"):
                from source.view.Page_principale.start_view import Start_view
                start_view= Start_view()
                return start_view.display()
            
            elif (Session().user_type in ['professeur', 'eleve', 'administrateur']) and (answers['choice'] == "Voir mes informations"):
                from source.view.Page_option.mes_info import MesInfos
                info= MesInfos()
                return info.display()
    

            elif (Session().user_type  == 'eleve') and (answers['choice'] == "Accéder à la liste de suggestions du professeur"):
                suggestions_view = SuggestionEleveView(id_eleve)
                return suggestions_view.display()


            elif (Session().user_type == 'professeur') and (answers['choice'] == "Accéder à la liste d'élèves"):
                liste_eleves_view = ListeElevesView(id_professeur)
                return liste_eleves_view.display()

            elif(Session().user_type == 'administrateur') and (answers['choice']== 'Accéder aux fonctions administrateur'):
                admin_view= AdminView()
                return admin_view.display()


            elif answers['choice'] == "Quitter l'application":
                print("Au revoir !")
                break

    def make_choice(self):
        return self.display()

if __name__ == "__main__":
    connexion_menu = Menu_view()
    connexion_menu.display()