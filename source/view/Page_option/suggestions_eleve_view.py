from source.services.service_suggestion_eleve import ServiceSuggestion
from source.view.session_view import Session

class SuggestionEleveView:

    def __init__(self, id_eleve):
        self.id_eleve=id_eleve
        self.suggestions_eleves_service = ServiceSuggestion()

    def afficher_menu(self):
        print("1. Consulter la liste de suggestions")
        print("2. Supprimer une suggestion")
        print("3. Quitter et revenir au menu principal")

    def display(self):
        while True:
            self.afficher_menu()
            choix = input("Choisissez une option : ")

            if choix == '1':
                self.suggestions_eleves_service.get_suggestions_by_id(self.id_eleve)
            elif choix == '2':
                id_stage = int(input("Entrez l'ID du stage à supprimer : "))
                self.suggestions_eleves_service.delete_suggestion(self.id_eleve, id_stage)
            elif choix == '3':
                print("Au revoir !")
                from source.view.Page_option.menu_view import Menu_view
                menu_view=Menu_view()
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
    