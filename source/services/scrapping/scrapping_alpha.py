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
