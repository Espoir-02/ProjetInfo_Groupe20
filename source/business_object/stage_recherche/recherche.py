class Recherche:
    def _init__(
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
        zon = ""
        domaine = ""
        niveau_etude = ""

        if self.zone:
            if self.zone == 1:
                zon = str(self.region)
            
            elif self.zone == 2:
                dep = str(self.departement)

            elif self.zone == 3:
                vil = str(self.ville)

        if self.domaine != "Non renseigné":
            if self.domaine == "Agriculture, agroalimentaire, environnement":
                dommaine = "/domaines-84+108+158"

            elif self.dommaine == "Arts - Arts appliqués":
                dommaine = "/domaines-85+86+87+88+94+120+122"

            elif self.domaine == "Assurance, Banque, Immobilier":
                dommaine = "/domaines-93+96+117+125"

            elif self.dommaine == "Commerce, vente, distribution":
                dommaine = "/domaines-79+99+104+109+135+136+162+164"

            elif self.dommaine == "Communication, culture":
                dommaine = "/domaines-100+105+110+130+140+143+149"

            elif self.dommaine == "Droit, Sc Politique, Economie":
                dommaine = "/domaines-82+107+154+155"

            elif self.dommaine == "Gestion, management, RH":
                dommaine = "/domaines-81+95+101+150+151+152"

            elif self.dommaine == "Hôtellerie-restauration, tourisme":
                dommaine = "/domaines-123+163"

            elif self.dommaine == "Informatique, télécom":
                dommaine = "/domaines-97+103+127+129+134+165"

            elif self.dommaine == "Lettres et Sciences humaines":
                dommaine = "/domaines-115+121+131+132+148+157+161"

            elif self.dommaine == "Santé - Sports":
                dommaine = "/domaines-80+141+144+159"

            elif self.dommaine == "Sciences, technologie":
                dommaine = "/domaines-83+98+102+111+113+114+116+124+126+128+137+138+139+142+145+146+147+156"

            elif self.dommaine == "Secrétariat - Assistanat":
                dommaine = "/domaines-89+90+91+92+160"

            elif self.dommaine == "Transports, logistique":
                dommaine = "/domaines-112+118+119+133"



