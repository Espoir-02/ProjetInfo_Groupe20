class Recherche:
    def _init__(
        self,
        duree=None,
        teletravail=None,
        profession=None,
        secteur=None,
        taille_entreprise=None,
        niveau_experience=None,
        niveau_etude=None,
        salaire_minimum=None,
    ):
        self.duree = duree
        self.teletravail = teletravail
        self.profession = profession
        self.secteur = secteur
        self.taille_entreprise = taille_entreprise
        self.niveau_experience = niveau_experience
        self.niveau_etude = niveau_etude
        self.salaire_minimum = salaire_minimum

    def changer_salaire(self,i):
        """
        Permet de changer le salaire récupéré en format string vers un format utilisable pour le scrapping.

        Parameters
        ---------
        i : str
            correspond au choix de la plage du salaire faite par l'utilisateur
        
        Examples
        --------
        >>> changer_salaire(">= 20 000")
        20 000
        """
        if (i == ">= 20 000"):
            # a compléter en demandant quel format du scrapping à Espoir
        
        elif (i == ">= 40 000"):
            # a compléter en demandant quel format du scrapping à Espoir
        
        elif (i == ">= 60 000"):
            # a compléter en demandant quel format du scrapping à Espoir
        
        elif (i == ">= 80 000"):
            # a compléter en demandant quel format du scrapping à Espoir
        
        elif (i == ">= 100 000"):
            # a compléter en demandant quel format du scrapping à Espoir
        
        else:
            raise ValueError("Le salaire envoyé est incorrect")