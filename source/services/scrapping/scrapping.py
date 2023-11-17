from source.DAO.StageDAO import StageDAO
#from source.DAO.EntrepriseDAO import EntrepriseDAO
from source.business_object.stage_recherche.stage import Stage
#from source.business_object.stage_recherche.entreprise import Entreprise
from source.DAO.utilitaire_dao import UtilitaireDAO

from bs4 import BeautifulSoup
import requests


class Scrapping:
    def scrap(self, url):
        response = requests.get(url)
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')

        stages_trouves = soup.find_all("div", {"class": "advert-card-content"})

        cpt = 1

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
            lieu = nonr
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
            print(cpt)
            print("Titre:", nomstage)
            print("Entreprise:", nomentreprise)
            print("Lieu:", lieu)
            print("Domaine:", domaine)
            print("Etude:", etude)
            print("Période:", periode)
            print("Gratification:", gratification)
            print("Date de publication:", date_publication)
            print("Lien du stage:", url2)
            print("\n")
            cpt = cpt + 1
            stage_exist=UtilitaireDAO()
            verification = stage_exist.check_infos_stage_exists(
                nomstage, url2, domaine, periode, gratification, date_publication, etude, nomentreprise, lieu)
            print("stage similaire:", verification)
            # Créer un objet Stage
            if verification==False:
                nouveau_stage= Stage(titre=nomstage, lien=url2, domaine=domaine,  date_publication=date_publication, periode=periode, salaire=gratification, niveau_etudes=etude, entreprise=nomentreprise, lieu=lieu)
            # Utiliser StageDAO pour créer le stage dans la base de données
                stage_dao = StageDAO()
                stage_cree = stage_dao.create_stage(nouveau_stage)
                print("insertion reussie")
            #nouv_entreprise=Entreprise(nom_entreprise=nomentreprise, adresse=lieu)
            #entreprise_DAO=EntrepriseDAO()
            #entreprise_cree=entreprise_DAO.create_entreprise(nouv_entreprise)


