from source.DAO.StageDAO import StageDAO
#from source.DAO.EntrepriseDAO import EntrepriseDAO
from source.business_object.stage_recherche.stage import Stage
#from source.business_object.stage_recherche.entreprise import Entreprise
from source.DAO.utilitaire_dao import UtilitaireDAO

from bs4 import BeautifulSoup
import requests

url = "https://jobs-stages.letudiant.fr/stages-etudiants/offres/domaines-93+96+117+125/departement-paris.html"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
stages_trouves = soup.find_all("div", {"class" : "advert-card-content"})

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
    publication = nonr
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
            publication =str(phrase.split('- publié le ')[1].strip())
            #etude = tout[i+3].get_text()
            #gratification = tout[i+5].get_text()
    print(cpt)
    print("Titre:", nomstage)
    print("Entreprise:", nomentreprise )
    print("Lieu:", lieu)
    print("Domaine:", domaine)
    print("Etude:", etude)
    print("Période:", periode)
    print("Salaire:", gratification)
    print("Date de publication:", publication)
    print("Lien du stage:", url2)
    print("\n")
    cpt = cpt + 1
    stage_exist=UtilitaireDAO()
    verification = stage_exist.check_infos_stage_exists(
        nomstage, url2, domaine, periode, gratification,
        etude, nomentreprise, lieu
    )
    print("stage similaire:", verification)
    # Créer un objet Stage
    if verification==False:
        nouveau_stage= Stage(titre=nomstage, lien=url2, domaine=domaine,  date_publication=None, periode=periode, salaire=gratification, niveau_etudes=etude, entreprise=nomentreprise, lieu=lieu)
    # Utiliser StageDAO pour créer le stage dans la base de données
        stage_dao = StageDAO()
        stage_cree = stage_dao.create_stage(nouveau_stage)
        print("insertion reussie")
    #nouv_entreprise=Entreprise(nom_enteprise=ent, adresse=lieu)
    #entreprise_DAO=EntrepriseDAO()
    #entreprise_cree=entreprise_DAO.create_entreprise(nouv_entreprise)

# le lieu du stage à mettre dans stage directement ou pas
# changer la longueur des variables
# prendre en compte l'url
# il faut relier les stages qu'on vient de chercher à la recherche
# date de publication a un problème
# non concordance de certaines variables de la classe stage avec stageDAO