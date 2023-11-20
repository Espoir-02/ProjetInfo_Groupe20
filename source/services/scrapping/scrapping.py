from source.DAO.StageDAO import StageDAO
#from source.DAO.EntrepriseDAO import EntrepriseDAO
from source.business_object.stage_recherche.stage import Stage
#from source.business_object.stage_recherche.entreprise import Entreprise
from source.DAO.utilitaire_dao import UtilitaireDAO
from source.services.service_export import ExporteurStage
from source.view.session_view import Session

from bs4 import BeautifulSoup
import requests


class Scrapping:
           
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


   def scrap(self, url):
        response = requests.get(url)
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')

        stages_trouves = soup.find_all("div", {"class": "advert-card-content"})

        cpt = 1
        all_stages_info = []
        liste_id_stages=[]
        for stage in stages_trouves:
            nomstage = stage.find("h2").get_text(strip=True)
            nomentreprise = stage.find("h3").get_text(strip=True)
            lieu = stage.find("span").get("title")
            beta = stage.parent.parent.parent
            url2 = beta.get("href")
            response2 = requests.get(url2)
            html2 = response2.text
            soup2 = BeautifulSoup(html2, 'html.parser')

            tout = soup2.find_all("p")
            nonr = 'Non Renseigné'
            domaine = nonr
            etude = nonr
            periode = nonr
            date_publication = nonr
            gratification = nonr

            for i in range(len(tout)):
                if tout[i].get_text() == 'DOMAINE DE FORMATION':
                    domaine = tout[i+1].get_text()
                if tout[i].get_text() == 'NIVEAU D\'ÉTUDES':
                    etude = tout[i+1].get_text()
                if tout[i].get_text() == 'GRATIFICATION':
                    gratification = tout[i+1].get_text()
                if tout[i].get_text() == 'PÉRIODE':
                    periode = tout[i+1].get_text()
                phrase = tout[i].get_text(strip=True)
                if phrase.startswith('Réf.'): 
                # Utilisez la méthode split() pour récupérer ce qui suit le premier tiret (-)
                    date_publication = phrase.split('- publié le ')[1].strip()
            #etude = tout[i+3].get_text()
            #gratification = tout[i+5].get_text()
            
            stage_exist=UtilitaireDAO()
            verification = stage_exist.check_infos_stage_exists(
                nomstage, url2, domaine, periode, gratification, date_publication, etude, nomentreprise, lieu)
            # Créer un objet Stage
            if verification==False:
                nouveau_stage= Stage(titre=nomstage, lien=url2, domaine=domaine,  date_publication=date_publication, periode=periode, salaire=gratification, niveau_etudes=etude, entreprise=nomentreprise, lieu=lieu)
            # Utiliser StageDAO pour créer le stage dans la base de données
                stage_cree = StageDAO().create_stage(nouveau_stage)

            # Créez un dictionnaire avec les informations du stage
            stage_info = {
                'titre': nomstage,
                'entreprise': nomentreprise,
                'lieu': lieu,
                'lien': url2,
                'domaine': domaine,
                'etude': etude,
                'periode': periode,
                'gratification': gratification,
                'date_publication': date_publication
            }

            all_stages_info.append(stage_info)

            # Affichez les informations de base du stage
            print(f"{cpt}. {nomstage} - {nomentreprise} - {lieu}")
            print(f"{'*' * 60}\n")

            # RECUPERATIONS DES ID DES STAGES
            stage_id = UtilitaireDAO().get_stage_ids(nomstage, url2, domaine, periode, gratification, date_publication, etude, nomentreprise, lieu)
            # LA LISTE DES ID DES STAGES 
            liste_id_stages.append(stage_id)

            cpt = cpt + 1
        

        for i in range(1,20):
            user_choice = input("Veuillez entrer le numéro du stage pour plus d'informations (ou tapez 'q' pour quitter): ")
            if user_choice.lower() == 'q':
                break

            try:
                # Obtenez les informations du stage sélectionné
                selected_stage_info = all_stages_info[int(user_choice) - 1]
                 # Affichez les informations supplémentaires
                self.display_additional_info(selected_stage_info)

            except (ValueError, IndexError):
                print("Choix invalide. Veuillez entrer un numéro valide.")

        id_utilisateur=Session().user_id 
        chemin_fichier_sortie = f'{id_utilisateur}_fichierExport.csv'

        # APPEL DE LA CLASSE EXPOTEURSTAGE POUR GERER L'EXPORTATION
        ExporteurStage().exporter_donnees(liste_id_stages, id_utilisateur,  chemin_fichier_sortie)
            