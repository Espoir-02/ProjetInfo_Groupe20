from InquirerPy import inquirer
from source.services.service_liste_envie import ListeEnvieService
from source.view.session_view import Session
from source.services.service_stage import StageService
from source.services.service_utilisateur import ServiceUtilisateur
from source.services.service_suggestion_eleve import ServiceSuggestion
from source.services.service_liste_eleves import ListeElevesService
from source.exception.exceptions import UtilisateurInexistantError
from source.services.service_export import ExporteurStage
from source.services.service_import import ImporteurStage


class ListeEnvieView:
    def __init__(self, id_utilisateur):
        self.service_liste_envie = ListeEnvieService()
        self.stage_service = StageService()
        self.service_liste_eleves = ListeElevesService()
        self.utilisateur_service = ServiceUtilisateur()
        self.suggestions_service = ServiceSuggestion()
        self.export = ExporteurStage()
        self.importer = ImporteurStage()
        self.type_utilisateur = Session().user_type
        self.id_utilisateur = Session().user_id

    def afficher_menu(self):
        menu_options = [
            "Consulter la liste d'envies",
            "Supprimer un stage de la liste",
            "Vider la liste d'envie",
            "Exporter la liste d'envie",
            "Importer une liste d'envie au format csv"
            "Revenir au menu principal",
        ]

        if Session().user_type in ["professeur", "administrateur"]:
            menu_options.append("Proposer un stage à partir de la liste d'envies")

        return [
            inquirer.List(
                "choix", message="Choisissez une option", choices=menu_options
            )
        ]

    def choisir_stage(self, liste_envie_courant):
        if not liste_envie_courant:
            print(" ")  # on doit rien mettre si la DAO renvoie déja un msg
        else:
            choix_stage = [
                f"{envie['id_stage']} - {envie['titre']}"
                for envie in liste_envie_courant
            ] + ["Retour au menu"]
            questions = [
                inquirer.List(
                    "selection", message="Sélectionner un stage:", choices=choix_stage
                )
            ]
            answers = inquirer.prompt(questions)

            selected_stage_str = answers["selection"].split(" - ")[0]

            if selected_stage_str == "Retour au menu":
                self.display()
            else:
                selected_stage = int(selected_stage_str)
                return selected_stage

    def consulter_liste_envies(self):
        liste_envie_courant = self.service_liste_envie.get_liste_envie_eleve(
            self.id_utilisateur
        )
        selected_stage = self.choisir_stage(liste_envie_courant)

        if selected_stage is not None:
            stage = self.stage_service.find_stage_by_id(selected_stage)
            if stage is not None:
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
                print(f"   Lieu : {stage['lieu']}\n")
                input("Appuyez sur Entrée pour continuer...\n")

    def proposer_stage(self):
        liste_envie_courant = self.service_liste_envie.get_liste_envie_eleve(
            self.id_utilisateur
        )
        selected_stage = self.choisir_stage(liste_envie_courant)

        if selected_stage is not None:
            try:
                nom_eleve = input("Entrez le nom de l'élève : ")
                prenom_eleve = input("Entrez le prénom de l'élève : ")
                eleve = self.utilisateur_service.trouver_utilisateur_par_nom(
                    nom_eleve, prenom_eleve
                )

                if eleve is not None:
                    id_eleve = eleve.get("id_utilisateur")
                    if self.service_liste_eleves.verifier_eleve_dans_liste(
                        id_eleve, self.id_utilisateur
                    ):
                        self.suggestions_service.create_suggestion(
                            id_eleve, selected_stage, self.id_utilisateur
                        )
                        print(
                            f"Le stage a été proposé à l'élève {nom_eleve} {prenom_eleve}."
                        )
                    else:
                        print(
                            "Vous ne pouvez pas proposer de stage à cet élève. Il n'est pas dans votre liste."
                        )
                else:
                    print("Aucun utilisateur trouvé avec les nom et prénom spécifiés.")
            except UtilisateurInexistantError as e:
                print(f"Erreur : {e}")

    def supprimer_envie(self):
        while True:
            id_stage = input(
                "Entrez l'ID du stage à supprimer (ou appuyez sur Entrée pour annuler) : "
            )

            if not id_stage.strip():
                print("L'ID du stage ne peut pas être vide.")
                return  # Annuler l'opération si l'ID est vide

            try:
                id_stage = int(id_stage)
                break  # Sortir de la boucle si la conversion en entier réussit
            except ValueError:
                print("L'ID du stage doit être un nombre entier. Veuillez réessayer.")

        self.service_liste_envie.supprimer_stage_de_liste_envie(
            self.id_utilisateur, id_stage
        )

    def display(self):
        while True:
            reponse = inquirer.prompt(self.afficher_menu())
            choix = reponse["choix"]

            if choix == "Consulter la liste d'envies":
                self.consulter_liste_envies()
            elif choix == "Supprimer un stage de la liste":
                self.supprimer_envie()
            elif choix == "Vider la liste d'envie":
                confirmation = inquirer.confirm(
                    message="Êtes-vous sûr de vouloir vider la liste d'envies?"
                )
                if confirmation:
                    self.service_liste_envie.vider_liste_envie_eleve(
                        self.id_utilisateur
                    )
                else:
                    print("Opération annulée.")
            elif choix == "Proposer un stage à partir de la liste d'envies":
                self.proposer_stage()
            elif choix == "Exporter la liste d'envie":
                chemin_sortie = input("Entrez le chemin du fichier de sortie (ex. sortie.txt) : ")
                self.export.exporter_listeEnvies(self.id_utilisateur, chemin_sortie)
            elif choix == "Importer une liste d'envie au format csv":
                chemin_entree = chemin_sortie = input("Entrez le chemin du fichier d'entrée (ex. sortie.txt) : ")
                self.importer.importer_donnees(self.id_utilisateur, chemin_entree)
            elif choix == "Revenir au menu principal":
                from source.view.Page_option.menu_view import Menu_view

                menu_view = Menu_view()
                return menu_view.display()
            else:
                print("Option invalide. Veuillez réessayer.")


if __name__ == "__main__":
    id_utilisateur = Session().user_id
    liste_envie_view = ListeEnvieView(id_utilisateur=id_utilisateur)
    liste_envie_view.display()
