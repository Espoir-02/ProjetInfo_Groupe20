from bs4 import BeautifulSoup
import requests

url = "https://jobs-stages.letudiant.fr/stages-etudiants/offres.html"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

pagination = soup.find_all("a", {"data-layer-event-cat" : "Pagination"})

pagination[0]["data-layer-event-act"]


pages = 1
for i in range(len(pagination)):
    if int(pagination[i]["data-layer-event-act"]) > pages:
        pages = int(pagination[i]["data-layer-event-act"])


propose = soup.find_all("div", {"class" : "advert-card-content"})
cpt = 1
for stage in propose:
    nomstage = stage.find("h2").get_text(strip=True)
    nomentreprise = stage.find("h3").get_text(strip=True)
    lieu = stage.find("span").get("title")
    print(cpt)
    print("Titre:", nomstage)
    print("Entreprise",nomentreprise )
    print("Lieu",lieu)
    print("\n")
    cpt = cpt + 1


beta = propose[0].parent.parent.parent
url2 = beta.get("href")
response2 = requests.get(url2)
html2 = response2.text
soup2 = BeautifulSoup(html2, 'html.parser')

tout = soup2.find_all("p")
nonr = 'Non Renseigné'
domaine = nonr
etude = nonr
for i in range(len(tout)):
    if tout[i].get_text() == 'PÉRIODE':
        domaine = tout[i+1].get_text()
        etude = tout[i+3].get_text()
        gratification = tout[i+5].get_text()
