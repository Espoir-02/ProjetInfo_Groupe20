from bs4 import BeautifulSoup
import requests

url = "https://www.directetudiant.com/candidatOffre/search/type/stage"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

pagination_elements = soup.find_all(class_="bt_pager_chiffre")

page_number = 0

# vérifier que la liste n'est pas vide
if pagination_elements:
    last_element = pagination_elements[-1]
    page_number = int(last_element.get_text(strip=True))
    
print(page_number)

cpt = 1
# for i in range(1, page_number + 1):
for i in range(1, 2 ):
    print("Page: ", i)
    if i == 1:
        url = "https://www.directetudiant.com/candidatOffre/search/type/stage"
    else:
        url = "https://www.directetudiant.com/candidatOffre/search/type/stage/page/" + str(i)
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    listing_text_elements = soup.find_all(class_="listing_text")

    for element in listing_text_elements:
        a_element = element.find("a")  # Find the <a> element
        # Récupérer le contenu de l'attribut "title"
        title = a_element.get("title")
        # Récupérer le contenu de l'attribut "href"
        href = a_element.get("href")
        h4_element = element.find("h4")  # Find the <h> element
        if a_element and h4_element:
            print(cpt)
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Titre:", title)
            print("Lien:", href)
            print("Lieu et date:", h4_element.get_text(strip=True))
            print("\n")
            cpt = cpt + 1