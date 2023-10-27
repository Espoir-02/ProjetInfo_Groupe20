

class Stage:
    """
    Classe permettant de filtrer la recherche de stage suivant différents critères : Salaire, Domaine, Modalité, Date de début, Date de fin.

    Attributes
    ---------
        id_stage -> int 
            Identification de manière unique chaque stage dns la base de données

        id_entreprise_stage -> int
            Identification de l'entreprise qui propose le stage

        nom_stage -> string 
            Intitulé du stage
        
        debut -> date
            Date du commencement du stage

        fin -> date 
            Date de la fin du stage

        domaine -> string
            Domaine du stage

        Modalité -> str
            **************

    Methods 
    -------
        str 

    Examples
    --------
    >>> stage = Entreprise(1196,SFR,"16 rue Lescault,75010",[13,22])
    >>> str(stage)
    "Agent d'accueil"
    """
    
    def __init__(self, titre, lien, domaine, modalites, date_publication, periode, salaire, entreprise):
        self.titre = titre
        self.lien = lien
        self.domaine = domaine
        self.modalites = modalites
        self.date_publication = date_publication
        self.periode = periode
        self.salaire = salaire
        self.entreprise = entreprise
        self.id = None

    def liste_nom_entreprise(self, nom_stage):
        """
        Méthode qui prend en entrée un stage et qui renvoie l'entreprise associée

        Return
        ------
        str

        Examples
        -------
        >>> nom_stage = "Conseiller"
        >>> liste_nom_entreprise(liste_stage)
        SNCF
        """
        
        return Stage.id_entreprise_stage
       
    def __str__(self):
        """
        Méthode qui permet de passer pour un même stage d'une visualisation machine à une visualisation humaine.
        """
        return "{}".format(self.nom_stage) # Est ce qu'on rajoute toutes les info concernant le stage ou que le nom ?