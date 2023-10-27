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
        url = "https://jobs-stages.letudiant.fr/stages-etudiants/offres.html"

