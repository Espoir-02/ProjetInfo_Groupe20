from InquirerPy import inquirer
from source.view.couche2menu.menu_view import Menu_view
from session_view import Session
from service_utilisateur import UtilisateurService

class Proposition_prof_view:
    def display(self):
        service_utilisateur = UtilisateurService()
        id_professeur = service_utilisateur.find_id_by_pseudo(self.pseudo)
        liste_eleves = ListeEleveDAO.get_liste_eleve_by_id(id_professeur)

        if liste_eleves:
            print("Liste d'élèves du professeur:", liste_eleves)
            choix_eleve = [
                inquirer.Text("nom", message="Nom:"),
                inquirer.Text("prenom", message="Prénom:")
            ]
            answers_debut = inquirer.prompt(choix_eleve, raise_keyboard_interrupt=True)

            id_eleve = UtilisateurDAO.find_by_nom(answers_debut["nom"], answers_debut["prenom"]).id
            id_stage = StageDAO.create_stage().id
            SuggestionsDAO.create_suggestion(id_eleve, id_stage, id_professeur)
            print("Le stage a bien été ajouté à la liste de propositions de l'élève")
            
            questions = [
                inquirer.List('choice', message='Choisir une option:', choices=['Proposer à mes élèves', 'Retour en arrière', 'Quitter'])
            ]
            answers_fin = inquirer.prompt(questions)

            if answers_fin['choice'] == 'Proposer à mes élèves':
                return  # à ajouter
            elif answers_fin['choice'] == "Retour en arrière":
                return  # à ajouter
            else:
                return "Exit"
        else:
            print("La liste d'élèves est vide.")

    
