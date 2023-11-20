from source.services.service_suggestion_eleve import ServiceSuggestion
from source.view.session_view import Session
from inquirer import prompt, List
import inquirer

class SuggestionEleveView:

    def __init__(self, id_eleve):
        self.id_eleve = id_eleve
        self.suggestions_eleves_service = ServiceSuggestion()

    def afficher_menu(self):
        return [
            List('choix',
                 message="Choisissez une option",
                 choices=[
                     'Consulter la liste de suggestions',
                     'Supprimer une suggestion',
                     'Vider la liste de suggestions',
                     'Quitter et revenir au menu principal'
                 ]),
        ]

    def display(self):
        while True:
            reponse = prompt(self.afficher_menu())
            choix = reponse['choix']

            if choix == 'Consulter la liste de suggestions':
                self.suggestions_eleves_service.get_suggestions_by_id(self.id_eleve)
            elif choix == 'Supprimer une suggestion':
                id_stage = int(input("Entrez l'ID du stage à supprimer : "))
                self.suggestions_eleves_service.delete_suggestion(self.id_eleve, id_stage)
            elif choix== 'Vider la liste de suggestions':
                confirmation = inquirer.confirm(message="Êtes-vous sûr de vouloir vider la liste de suggestions ?")
                if confirmation:
                    self.suggestions_eleves_service.vider_liste_suggestions(self.id_eleve)
                else:
                    print("Opération annulée.")
            elif choix == 'Quitter et revenir au menu principal':
                print("Au revoir !")
                menu_view = Menu_view()
                menu_view.display()
                break
            else:
                print("Option invalide. Veuillez réessayer.")

    def make_choice(self):
        return self.display()
if __name__ == "__main__":

    id_eleve = Session().user_id 
    suggestions_eleves = SuggestionEleveView(id_eleve=id_eleve)
    suggestions_eleves.display()
    