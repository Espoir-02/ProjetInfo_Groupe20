from bs4 import BeautifulSoup
import requests

url = "https://jobs-stages.letudiant.fr/stages-etudiants/offres.html"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

pagination = soup.find_all("a", {"data-layer-event-cat" : "Pagination"})

pagination[0]["data-layer-event-act"]

print("nb:",len(pagination))
pages = 1
for i in range(len(pagination)):
    if int(pagination[i]["data-layer-event-act"]) > pages:
        pages = int(pagination[i]["data-layer-event-act"])

for i in range(1, 2 ):
    print("Page: ", i)
    if i == 1:
        url = "https://jobs-stages.letudiant.fr/stages-etudiants/offres.html"
    else:
        url = "https://jobs-stages.letudiant.fr/stages-etudiants/offres/page-2.html"

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    propose = soup.find_all("div", {"class" : "advert-card-content"})
    cpt = 1
    for stage in propose:
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
        periode=nonr
        date_publication=nonr
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
        print("Entreprise",nomentreprise )
        print("Lieu",lieu)
        print("Domaine:",domaine)
        print("Etude:",etude)
        print("Période:",periode)
        print("Date de publication:", date_publication)
        print("\n")
        cpt = cpt + 1

