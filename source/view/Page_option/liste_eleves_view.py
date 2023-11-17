from source.services.service_liste_eleves import ListeElevesService
from source.view.session_view import Session

class ListeElevesView:

    def __init__(self, id_professeur):
        self.id_professeur=id_professeur
        self.liste_eleves_service = ListeElevesService()

    def afficher_menu(self):
        print("1. Consulter la liste des élèves")
        print("2. Ajouter un élève")
        print("3. Supprimer un élève")
        print("4. Quitter")

    def display(self):
        while True:
            self.afficher_menu()
            choix = input("Choisissez une option : ")

            if choix == '1':
                self.liste_eleves_service.consulter_liste_eleves(self.id_professeur)
            elif choix == '2':
                nom_eleve = input("Entrez le nom de l'élève : ")
                prenom_eleve = input("Entrez le prénom de l'élève : ")
                eleve = {"nom": nom_eleve, "prenom": prenom_eleve}
                self.liste_eleves_service.ajouter_eleve_a_liste_eleves(eleve, self.id_professeur)
            elif choix == '3':
                id_eleve = int(input("Entrez l'ID de l'élève à supprimer : "))
                self.liste_eleves_service.supprimer_eleve_de_liste_eleves(id_eleve, self.id_professeur)
            elif choix == '4':
                print("Au revoir !")
                break
            else:
                print("Option invalide. Veuillez réessayer.")

    def make_choice(self):
        return self.display()

if __name__ == "__main__":

    id_professeur = Session().user_id 
    vue_liste_eleves = ListeElevesView(id_professeur=id_professeur)
    vue_liste_eleves.display()
    