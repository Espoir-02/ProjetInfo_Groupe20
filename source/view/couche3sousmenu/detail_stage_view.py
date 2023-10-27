from source.business_object.stage_recherche.stage import Stage
from source.view.abstract_view import AbstractView
from source.DAO.ListeEleveDAO import ListeEleves
from source.DAO.UtilisateurDAO import UtilisateurDAO
from source.DAO.SuggestionsDAO import SuggestionsDAO
from source.DAO.StageDAO import StageDAO
from source.view.couche2menu.Liste_envie_view import Liste_envie_view

from InquirerPy import inquirer

class detail_stage_view_eleve(AbstractView):
    def __init__(self, stage):
        self.stage = stage

    def display(self, selection_stage):
        # Affiche les détails du stage sélectionné
        stage_details = self.stage.get_stage_details(stage_details)

        # Affiche les détails du Pokémon et propose de retourner à la vue précédente
        print(f"Intitulé : {stage_details['nom']}")
        print(f"Durée: {stage_details['durée']}")
        print(f"Salaire: {stage_details['salaire']}")
        print(f"Type: {stage_details['type']}")
        print(f"Entreprise: {stage_details['entreprise']}")
        questions = [inquirer.List('choice', message='Choisir une option:', choices=['Retour en arrière', 'Quitter'])]
        answers = inquirer.prompt(questions)

        if answers['choice'] == 'Retour en arrière':
            # Retourne à la vue précédente
            return Liste_envie_view().liste_envie_view()
        else:
            # Termine l'application
            return 'Exit'

class detail_stage_view_prof(AbstractView):
    def __init__(self, stage):
        self.stage = stage

    def display(self, selection_stage):
        # Affiche les détails du stage sélectionné
        stage_details = self.stage.get_stage_details(stage_details)

        # Affiche les détails du Pokémon et propose de retourner à la vue précédente
        print(f"Intitulé : {stage_details['nom']}")
        print(f"Durée: {stage_details['durée']}")
        print(f"Salaire: {stage_details['salaire']}")
        print(f"Type: {stage_details['type']}")
        print(f"Entreprise: {stage_details['entreprise']}")
        questions = [inquirer.List('choice', message='Choisir une option:', choices=[
            'Proposer à mes élèves','Retour en arrière', 'Quitter'])]
        answers = inquirer.prompt(questions)

        if answers['choice'] == 'Proposer à mes élèves':
            # Accède à la liste de ses élèves
            id_professeur = UtilisateurDAO.find_id_by_pseudo().id # faut-il mettre des attributs noms et prénom du prof ???
            liste_eleves = self.ListeEleveDAO.get_liste_eleve_by_id(id_professeur)

            if liste_eleves:
                print("Liste d'élèves du professeur:", liste_eleves)
                choix_eleve = [inquirer.Text("nom", message="Nom:"),inquirer.Text("prenom", message="Prénom:")]
                answers_debut = inquirer.prompt(choix_eleve, raise_keyboard_interrupt=True)

                id_eleve = UtilisateurDAO.find_by_nom(answers["nom"],answers["prenom"]).id #rentrer les attribyuts nom et 
                id_stage = StageDAO.create_stage().id
                SuggestionsDAO.create_suggestion(id_eleve, id_stage, id_professeur) # ajouter le stage dans la liste de proposition des élèves
                print("La stage a bien été ajouté à la liste de propositions de l'élève")
                
                questions = [inquirer.List('choice', message='Choisir une option:', choices=['Proposer à mes élèves','Retour en arrière', 'Quitter'])]
                answers_fin = inquirer.prompt(questions)

                if answers_fin['choice'] == 'Proposer à mes élèves':
                    return # à ajouter
                
                elif answers_fin['choice'] == "Retour en arrière":
                    return # à ajouter

                else :
                    return "Exit"

            
            else:
                print("La liste d'élèves est vide.")
        
        elif answers['choice'] == 'Retour en arrière':
            # Retourne à la vue précédente
            return Liste_envie_view.liste_envie_view
        else:
            # Termine l'application
            return 'Exit'