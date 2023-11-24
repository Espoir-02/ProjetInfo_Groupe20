from source.services.scrapping.scrapping import *
from source.services.scrapping.scrapping2 import *
class Recherche:
    def __init__(
        self,
        zone=None,
        region=None,
        departement=None,
        ville=None,
        domaine=None,
        niveau_etude=None,
        periode=None
    ):
        self.zone = zone
        self.region = region
        self.departement = departement
        self.ville = ville
        self.domaine = domaine
        self.niveau_etude = niveau_etude
        self.periode = periode

    def lancer_recherche(self):
        url = "https://jobs-stages.letudiant.fr/stages-etudiants/offres"
        zone = ""
        domaine = ""
        niveau_etude = ""

        if self.zone:
            if self.zone == 1:
                zone = "/region-"+str(self.region)

            elif self.zone == 2:
                zone = "/departement-"+str(self.departement)

            elif self.zone == 3:
                zone = "/ville-"+str(self.ville)

        if self.domaine != "Non renseigné":
            if self.domaine == "Agriculture, agroalimentaire, environnement":
                domaine = "/domaines-84+108+158"

            elif self.domaine == "Arts - Arts appliqués":
                domaine = "/domaines-85+86+87+88+94+120+122"

            elif self.domaine == "Assurance, Banque, Immobilier":
                domaine = "/domaines-93+96+117+125"

            elif self.domaine == "Commerce, vente, distribution":
                domaine = "/domaines-79+99+104+109+135+136+162+164"

            elif self.domaine == "Communication, culture":
                domaine = "/domaines-100+105+110+130+140+143+149"

            elif self.domaine == "Droit, Sc Politique, Economie":
                domaine = "/domaines-82+107+154+155"

            elif self.domaine == "Gestion, management, RH":
                domaine = "/domaines-81+95+101+150+151+152"

            elif self.domaine == "Hôtellerie-restauration, tourisme":
                domaine = "/domaines-123+163"

            elif self.domaine == "Informatique, télécom":
                domaine = "/domaines-97+103+127+129+134+165"

            elif self.domaine == "Lettres et Sciences humaines":
                domaine = "/domaines-115+121+131+132+148+157+161"

            elif self.domaine == "Santé - Sports":
                domaine = "/domaines-80+141+144+159"

            elif self.domaine == "Sciences, technologie":
                domaine = "/domaines-83+98+102+111+113+114+116+124+126+128+137+138+139+142+145+146+147+156"

            elif self.domaine == "Secrétariat - Assistanat":
                domaine = "/domaines-89+90+91+92+160"

            elif self.domaine == "Transports, logistique":
                domaine = "/domaines-112+118+119+133"

        if self.niveau_etude != "Non renseigné":
            if self.niveau_etude == "Bac +5":
                niveau_etude = "/niveaux-1"

            elif self.niveau_etude == "Bac +4":
                niveau_etude = "/niveaux-9"

            elif self.niveau_etude == "Bac +3":
                niveau_etude = "/niveaux-2"

            elif self.niveau_etude == "Bac +2":
                niveau_etude = "/niveaux-3"

            elif self.niveau_etude == "Bac":
                niveau_etude = "/niveaux-4"

            elif self.niveau_etude == "CAP/BEP":
                niveau_etude = "/niveaux-5"

            elif self.niveau_etude == "Bac professionnel":
                niveau_etude = "/niveaux-6"

            elif self.niveau_etude == "3ème":
                niveau_etude = "/niveaux-7"

        urlf = url + niveau_etude + domaine + zone + ".html"

        Scrapping2().scrap(urlf)
