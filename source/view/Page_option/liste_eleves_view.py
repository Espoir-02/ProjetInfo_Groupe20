from source.services.service_liste_eleves import ListeElevesService

class ListeElevesView:

    def __init__(self, liste_eleves_service):
        self.liste_eleves_service = ListeElevesService()

    def afficher_menu(self):
        print("1. Consulter la liste des élèves")
        print("2. Ajouter un élève")
        print("3. Supprimer un élève")
        print("4. Quitter")

    def executer(self, id_professeur):
        while True:
            self.afficher_menu()
            choix = input("Choisissez une option : ")

            if choix == '1':
                self.liste_eleves_service.consulter_liste_eleves(id_professeur, option)
            elif choix == '2':
                nom_eleve = input("Entrez le nom de l'élève : ")
                prenom_eleve = input("Entrez le prénom de l'élève : ")
                eleve = {"nom": nom_eleve, "prenom": prenom_eleve}
                self.liste_eleves_service.ajouter_eleve_a_liste_eleves(eleve, id_professeur)
            elif choix == '3':
                id_eleve = int(input("Entrez l'ID de l'élève à supprimer : "))
                self.liste_eleves_service.supprimer_eleve_de_liste_eleves(id_eleve, id_professeur)
            elif choix == '4':
                print("Au revoir !")
                break
            else:
                print("Option invalide. Veuillez réessayer.")

