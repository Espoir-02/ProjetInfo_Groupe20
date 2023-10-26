from bs4 import BeautifulSoup
import requests

url = "https://www.directetudiant.com/candidatOffre/search/type/stage"
response = requests.get(url) # récupération de l'url
html = response.text # récupération de l'url en format texte

soup = BeautifulSoup(html, 'html.parser') # cette commande récupère toute la page provenant de l'url

pagination_elements = soup.find_all(class_="bt_pager_chiffre") # nombre de pages sur l'url en question

page_number = 0

# vérifier que la liste (avoir au moins 1 page) n'est pas vide
if pagination_elements: # c'est une liste contenant toutes les balises
    last_element = pagination_elements[-1] # on prend le dernier élément de cette liste
    page_number = int(last_element.get_text(strip=True)) # parmi ce dernier élément, on extrait le texte hors des balises
    
print(page_number) # affiche ce texte pas entre balises

cpt = 1
# for i in range(1, page_number + 1):
for i in range(1, 2 + 1):
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
        h4_element = element.find("h4")  # Find the <h> element
        if a_element and h4_element:
            print(cpt)
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Titre:", a_element.get_text(strip=True))
            print("Lieu et date:", h4_element.get_text(strip=True))
            print("\n")
            cpt = cpt + 1