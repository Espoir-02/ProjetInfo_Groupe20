import inquirer
from inquirer import prompt, List
from source.DAO.StageDAO import StageDAO
from source.business_object.stage_recherche.stage import Stage
from source.DAO.utilitaire_dao import UtilitaireDAO
from source.services.service_liste_eleves import ListeElevesService
from source.services.service_liste_envie import ListeEnvieService
from source.services.service_historique import HistoriqueService
from source.services.service_suggestion_eleve import ServiceSuggestion
from source.services.service_utilisateur import ServiceUtilisateur
from source.services.service_stage import StageService
from source.exception.exceptions import UtilisateurInexistantError
from source.view.session_view import Session
from source.services.service_export import ExporteurStage
from bs4 import BeautifulSoup
import requests
import re


class Scrapping2:
    def __init__(self):
        self.historique_service = HistoriqueService()
        self.id_utilisateur = Session().user_id
        self.utilisateur_service = ServiceUtilisateur()
        self.liste_envie_service = ListeEnvieService()
        self.suggestions_service = ServiceSuggestion()
        self.service_liste_eleves = ListeElevesService()
        self.service_stage = StageService()
        self.export = ExporteurStage()
        self.type_utilisateur = Session().user_type
        self.current_page = 1  # Added attribute to track the current page
        
    def display_additional_info(self, stage_info):
        print(f"{'*' * 40}")
        print(f"Titre: {stage_info['titre']}")
        print(f"Entreprise: {stage_info['entreprise']}")
        print(f"Lieu: {stage_info['lieu']}")
        print(f"Lien du stage: {stage_info['lien']}")
        print(f"{'-' * 40}")
        print(f"Domaine: {stage_info['domaine']}")
        print(f"Etude: {stage_info['etude']}")
        print(f"Période: {stage_info['periode']}")
        print(f"Gratification: {stage_info['gratification']}")
        print(f"Date de publication: {stage_info['date_publication']}")
        print(f"{'*' * 40}\n")

    def display_stage_menu(self, all_stages_info,url):
        if not all_stages_info:
            print("Aucun stage trouvé.")
            return None
        numero = self.current_page-1
        choix_stage = [
            f"{i+1}. {stage_info['titre']} - {stage_info['entreprise']} - {stage_info['lieu']}"
            for i, stage_info in enumerate(all_stages_info)
        ] + ["Retour au menu"] + ["Autres stages"]
        
        questions = [
            inquirer.List(
                "selection", message="Sélectionner un stage:", choices=choix_stage
            )
        ]
        answers = inquirer.prompt(questions)

        selected_stage_str = answers["selection"]


        if selected_stage_str.lower() == "autres stages":
            self.current_page += 1
            if self.current_page==2:
                next_page_url = url.replace(".html", "/page-2.html")#
                #print("url 2:",next_page_url)
                #print("ça marche")
                self.scrap(next_page_url)
            if self.current_page>2:
                next_page_url = re.sub(r"/page-\d+.html", f"/page-{self.current_page}.html", url)
                #print("url 2:",next_page_url)
                self.scrap(next_page_url)
            #print("url 1:",url)
        elif selected_stage_str.lower() == "retour au menu":
            from source.view.Page_option.menu_view import Menu_view
            return Menu_view().display()
        
        elif re.match(r"^\d", selected_stage_str):
            selected_stage = int(re.search(r"\d+", selected_stage_str).group())
            selected_stage_info = all_stages_info[selected_stage - 1]
            self.display_additional_info(selected_stage_info)
            return selected_stage_info

        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")
            return None

    def choisir_eleve_menu(self, liste_eleves):
        choix_eleve = [
            f"{eleve['nom']} {eleve['prenom']}" for eleve in liste_eleves
        ] + ["Retour au menu"]

        questions = [
            inquirer.List(
                "selection_eleve",
                message="Sélectionner un élève:",
                choices=choix_eleve
            )
        ]

        answers = inquirer.prompt(questions)
        selected_eleve_str = answers["selection_eleve"]

        if selected_eleve_str == "Retour au menu":
            return None
        else:
            selected_eleve = [eleve for eleve in liste_eleves if f"{eleve['nom']} {eleve['prenom']}" == selected_eleve_str][0]
            return selected_eleve["id_eleve"]

    def display_stage_options(self, id_stage_selected):
        id_utilisateur = Session().user_id
        options = [
            "Exporter le stage",
            "Signaler ce stage",
            "Consulter un autre stage",
        ]

        if Session().user_type in ["professeur", "eleve", "administrateur"]:
            options.append("Ajouter le stage à votre liste d'envies")
        if Session().user_type == "professeur":
            options.append("Proposer ce stage à un élève")
        
        options.append("Quitter et revenir au menu principal")

        questions = [
            inquirer.List(
                "selection", message="Que souhaitez-vous faire?", choices=options
            )
        ]
        answers = inquirer.prompt(questions)
        selected_option = answers["selection"]

        if selected_option == "Ajouter le stage à votre liste d'envies":
            try:
                self.liste_envie_service.ajouter_stage_a_liste_envie(
                    self.id_utilisateur, id_stage_selected
                )
            except (ValueError, IndexError):
                print("Choix invalide. Veuillez entrer un numéro valide.")
        elif selected_option == "Exporter le stage":
            chemin_sortie = input("Entrez le nom du fichier de sortie (ex. sortie) : ")
            self.export.exporter_donnees(
                id_stage_selected, chemin_sortie
                )
        elif selected_option == "Proposer ce stage à un élève":
                liste_eleves = self.service_liste_eleves.get_liste_eleves(
                    self.id_utilisateur
                )
                id_eleve = self.choisir_eleve_menu(liste_eleves)
                if id_eleve is not None:
                    self.suggestions_service.create_suggestion(
                        id_eleve, id_stage_selected, self.id_utilisateur
                    )
                    print(f"Le stage a été proposé à l'élève sélectionné.")
                else:
                    print("Aucun élève sélectionné.")
        elif selected_option == "Signaler ce stage":
            confirmation = inquirer.confirm(
                message="Êtes-vous sûr de vouloir signaler ce stage?"
            )
            if confirmation:
                self.service_stage.signaler_stage(id_stage_selected,self.id_utilisateur)
                print("Stage signalé")
            else:
                print("Opération annulée.")
        elif selected_option == "Consulter un autre stage":
            return "continue"
        elif selected_option == "Quitter et revenir au menu principal":
            return "quit"
        else:
            from source.view.Page_option.menu_view import Menu_view

            return Menu_view().display()

    def scrap(self, url):
        id_utilisateur = Session().user_id
        url_next = url
        response = requests.get(url)
        html = response.text

        soup = BeautifulSoup(html, "html.parser")

        stages_trouves = soup.find_all("div", {"class": "advert-card-content"})

        all_stages_info = []

        for stage in stages_trouves:
            nomstage = stage.find("h2").get_text(strip=True)
            nomentreprise = stage.find("h3").get_text(strip=True)
            lieu = stage.find("span").get("title")
            beta = stage.parent.parent.parent
            url2 = beta.get("href")
            response2 = requests.get(url2)
            html2 = response2.text
            soup2 = BeautifulSoup(html2, "html.parser")

            tout = soup2.find_all("p")
            nonr = "Non Renseigné"
            domaine = nonr
            etude = nonr
            periode = nonr
            date_publication = nonr
            gratification = nonr

            for i in range(len(tout)):
                if tout[i].get_text() == "DOMAINE DE FORMATION":
                    domaine = tout[i + 1].get_text()
                if tout[i].get_text() == "NIVEAU D'ÉTUDES":
                    etude = tout[i + 1].get_text()
                if tout[i].get_text() == "GRATIFICATION":
                    gratification = tout[i + 1].get_text()
                if tout[i].get_text() == "PÉRIODE":
                    periode = tout[i + 1].get_text()
                phrase = tout[i].get_text(strip=True)
                if phrase.startswith("Réf."):
                    date_publication = phrase.split("- publié le ")[1].strip()

            stage_exist = UtilitaireDAO()
            verification = stage_exist.check_infos_stage_exists(
                nomstage,
                url2,
                domaine,
                periode,
                gratification,
                date_publication,
                etude,
                nomentreprise,
                lieu,
            )

            if verification == False:
                nouveau_stage = Stage(
                    titre=nomstage,
                    lien=url2,
                    domaine=domaine,
                    date_publication=date_publication,
                    periode=periode,
                    salaire=gratification,
                    niveau_etudes=etude,
                    entreprise=nomentreprise,
                    lieu=lieu,
                )
                stage_cree = StageDAO().create_stage(nouveau_stage)

            stage_info = {
                "titre": nomstage,
                "entreprise": nomentreprise,
                "lieu": lieu,
                "lien": url2,
                "domaine": domaine,
                "etude": etude,
                "periode": periode,
                "gratification": gratification,
                "date_publication": date_publication,
            }

            all_stages_info.append(stage_info)

        while True:
            selected_stage_info = self.display_stage_menu(all_stages_info, url_next)

            if selected_stage_info is None:
                # L'utilisateur a choisi de quitter
                break

            id_stage_selected = UtilitaireDAO().get_stage_ids(
                selected_stage_info["titre"],
                selected_stage_info["lien"],
                selected_stage_info["domaine"],
                selected_stage_info["periode"],
                selected_stage_info["gratification"],
                selected_stage_info["date_publication"],
                selected_stage_info["etude"],
                selected_stage_info["entreprise"],
                selected_stage_info["lieu"],
            )

            self.historique_service.ajouter_stage_a_historique(
                id_utilisateur, id_stage_selected
            )
            while True:
                result = self.display_stage_options(id_stage_selected)
                if result == "quit":
                    from source.view.Page_option.menu_view import Menu_view

                    return Menu_view().display()
                elif result == "continue":
                    break
