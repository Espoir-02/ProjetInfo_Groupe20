from source.services.service_liste_eleves import ListeElevesService
from source.services.service_utilisateur import ServiceUtilisateur
from source.exception.exceptions import UtilisateurInexistantError
from source.view.session_view import Session
from inquirer import prompt, List
import inquirer
 

class ListeElevesView:
    def __init__(self, id_professeur):
        self.id_professeur = Session().user_id
        self.liste_eleves_service = ListeElevesService()
        self.utilisateur_service = ServiceUtilisateur()

    def afficher_menu(self):
        return [
            List('choix',
                 message="Choisissez une option",
                 choices=[
                     'Consulter la liste des élèves',
                     'Ajouter un élève',
                     'Supprimer un élève',
                     'Vider la liste des élèves',
                     'Quitter et revenir au menu principal'
                 ]),
        ]

    def ajout_eleve(self):
        try:
            nom_eleve = input("Entrez le nom de l'élève : ")
            prenom_eleve = input("Entrez le prénom de l'élève : ")
        
            eleve = self.utilisateur_service.trouver_utilisateur_par_nom(nom_eleve, prenom_eleve)

            if eleve is not None:
                id_eleve = eleve.get("id_utilisateur")
                self.liste_eleves_service.ajouter_eleve_a_liste_eleves(id_eleve, self.id_professeur)
            else:
                print("Aucun utilisateur trouvé avec les nom et prénom spécifiés.")

        except UtilisateurInexistantError as e:
            print(f"Erreur : {e}")



    def display(self):
        while True:
            reponse = prompt(self.afficher_menu())
            choix = reponse['choix']

            if choix == 'Consulter la liste des élèves':
                self.liste_eleves_service.consulter_liste_eleves(self.id_professeur)
            elif choix == 'Ajouter un élève':
                self.ajout_eleve()
            elif choix == 'Supprimer un élève':
                id_eleve = int(input("Entrez l'ID de l'élève à supprimer : "))
                self.liste_eleves_service.supprimer_eleve_de_liste_eleves(id_eleve, self.id_professeur)
            elif choix== 'Vider la liste des élèves':
                confirmation = inquirer.confirm(message="Êtes-vous sûr de vouloir vider la liste des élèves?")
                if confirmation:
                    self.liste_eleves_service.vider_liste_eleves(self.id_professeur)
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
    id_professeur = Session().user_id 
    vue_liste_eleves = ListeElevesView(id_professeur=id_professeur)
    vue_liste_eleves.display()