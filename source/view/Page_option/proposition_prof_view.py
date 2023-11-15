from InquirerPy import inquirer
from source.view.Page_option.menu_view import Menu_view
from source.view.session_view import Session
from source.services.service_utilisateur import UtilisateurService
from source.services.service_suggestion_eleve import ServiceSuggestion


class Proposition_prof_view:
    def __init__(self,selection_stage):
        self.selection_stage = selection_stage

    def display(self):
        service_utilisateur = UtilisateurService()
        id_professeur = Session().user_id
        service_suggestion = ServiceSuggestion()
        liste_eleves = service_suggestion.get_liste_eleve_by_id(id_professeur)

        while True:
            if liste_eleves:
                print("Liste d'élèves du professeur:", liste_eleves)
                choix_eleve = [
                    inquirer.Text("nom", message="Nom:"),
                    inquirer.Text("prenom", message="Prénom:")
                ]
                answers_debut = inquirer.prompt(choix_eleve, raise_keyboard_interrupt=True)

                id_eleve = service_utilisateur.trouver_utilisateur_par_nom(answers_debut["nom"], answers_debut["prenom"]).id
                id_stage = self.selection_stage
                service_suggestion=ServiceSuggestion()
                service_suggestion.create_suggestion(id_eleve, id_stage, id_professeur)
                print("Le stage a bien été ajouté à la liste de propositions de l'élève")
                
                questions = [
                    inquirer.List('choice', message='Choisir une option:', choices=['Proposer à mes élèves','Quitter'])
                ]
                answers_fin = inquirer.prompt(questions)

                if answers_fin['choice'] == 'Quitter':
                    return Menu_view()
                #tant que le professeur ne choisit pas de quitter , on continue la boucle
            else:
                print("La liste d'élèves est vide.")

        
