from InquirerPy import inquirer
from source.services.service_utilisateur import ServiceUtilisateur
from source.services.service_historique import HistoriqueService
from source.services.service_liste_envie import ListeEnvieService
from source.services.service_suggestion_eleve import ServiceSuggestion
from source.services.service_stage import StageService
from source.view.session_view import Session
from source.exception.exceptions import UtilisateurInexistantError
import inquirer


class HistoriqueView:

    def __init__(self):
        self.historique_service = HistoriqueService()
        self.id_utilisateur= Session().user_id
        self.liste_envie_service = ListeEnvieService()
        self.stage_service = StageService()
        self.suggestions_service = ServiceSuggestion()
        self.utilisateur_service = ServiceUtilisateur()
        self.type_utilisateur = Session().user_type

    def afficher_menu(self):
        menu_options = [
            'Consulter l\'historique',
            'Vider l\'historique',
            'Revenir au menu principal'
        ]

        if (Session().user_type == 'professeur'):
            menu_options.append('Proposer un stage à partir de la liste d\'envies')

        return [
            inquirer.List('choix', message="Choisissez une option", choices=menu_options)
        ]

    def choisir_stage(self, liste_historique_courant):
        if not liste_historique_courant:
            print("L'historique est vide.")
        else:
            choix_stage = [f"{historique['id_stage']} - {historique['titre']}" for historique in liste_historique_courant] + ["Retour au menu"]
            questions = [inquirer.List('selection', message='Sélectionner un stage:', choices=choix_stage)]
            answers = inquirer.prompt(questions)

            selected_stage = int(answers['selection'].split(' - ')[0])

            if selected_stage == "Retour au menu":
                self.display()
            else:
                return selected_stage

    def consulter_historique(self):
        liste_historique_courant = self.historique_service.get_all_historique_by_id(self.id_utilisateur)
        selected_stage = self.choisir_stage(liste_historique_courant)

        if selected_stage is not None:
            stage = self.stage_service.find_stage_by_id(selected_stage)
            print("Informations sur le stage :")
            print(f"   ID du stage : {stage['id_stage']}")
            print(f"   Titre : {stage['titre']}")
            print(f"   Lien : {stage['lien']}")
            print(f"   Domaine : {stage['domaine']}")
            print(f"   Salaire : {stage['salaire']}")
            print(f"   Date de publication : {stage['date_publication']}")
            print(f"   Période : {stage['periode']}")
            print(f"   Niveau d'études : {stage['niveau_etudes']}")
            print(f"   Entreprise : {stage['entreprise']}")
            print(f"   Lieu : {stage['lieu']}")

            # Demander à l'utilisateur s'il souhaite ajouter le stage à sa liste d'envies
            if self.type_utilisateur in ['professeur', 'eleve', 'administrateur']:
                ajout_envie = inquirer.confirm(message="Voulez-vous ajouter ce stage à votre liste d'envies?")
                if ajout_envie:
                    self.liste_envie_service.ajouter_stage_a_liste_envie(self.id_utilisateur, selected_stage)
                    print("Le stage a été ajouté à votre liste d'envies.")
                else:
                    print("Le stage n'a pas été ajouté à votre liste d'envies.")

            # Demander à l'utilisateur s'il souhaite proposer le stage à un élève
            if self.type_utilisateur == 'professeur':
                proposer_eleve = inquirer.confirm(message="Voulez-vous proposer ce stage à un élève?")
                if proposer_eleve:
                    try:
                        nom_eleve = input("Entrez le nom de l'élève : ")
                        prenom_eleve = input("Entrez le prénom de l'élève : ")
                        eleve = self.utilisateur_service.trouver_utilisateur_par_nom(nom_eleve, prenom_eleve)

                        if eleve is not None:
                            id_eleve = eleve.get("id_utilisateur")
                            self.suggestions_service.create_suggestion(id_eleve, selected_stage, self.id_utilisateur)
                            print(f"Le stage a été proposé à l'élève {nom_eleve} {prenom_eleve}.")
                        else:
                                print("Aucun utilisateur trouvé avec les nom et prénom spécifiés.")
                    except UtilisateurInexistantError as e:
                        print(f"Erreur : {e}")

    def vider_historique(self):
        confirmation = inquirer.confirm(message="Êtes-vous sûr de vouloir vider l'historique?")
        if confirmation:
            self.historique_service.vider_historique(self.id_utilisateur)
            print("L'historique a été vidé avec succès.")
        else:
            print("Opération annulée.")

    def display(self):
        while True:
            reponse = inquirer.prompt(self.afficher_menu())
            choix = reponse['choix']

            if choix == 'Consulter l\'historique':
                self.consulter_historique()
            elif choix == 'Vider l\'historique':
                self.vider_historique()
            elif choix == 'Revenir au menu principal':
                menu_view=Menu_view()
                menu_view.display()
                break
            else:
                print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    historique_view = HistoriqueView()
    historique_view.display()








"""class HistoriqueView:
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

if __name__ == "__main__":
    vue_historique = HistoriqueView()
    vue_historique.display()"""