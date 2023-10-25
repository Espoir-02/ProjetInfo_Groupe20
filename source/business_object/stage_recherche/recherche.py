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
        i : 

        """
        
        if (i == ">= 20 000"):
            #
        
        elif (i == ">= 40 000"):
            #
        
        elif (i == ">= 60 000"):
            #
        
        elif (i == ">= 80 000"):
            #
        
        elif (i == ">= 100 000"):
            #
        
        else:
            raise ValueError("Le salaire envoyé est incorrect")