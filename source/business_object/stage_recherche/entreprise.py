from source.business_object.stage_recherche.stage import Stage

class Entreprise:
    """
    Classe permettant de filtrer la recherche de stage par entreprise.

    Attributs
    ---------
        id_entreprise -> int 
            Identification de manière unique chaque entreprise dans la base de données

        nom_entreprise -> string
            Nom de l'entreprise

        adresse -> string
            Adresse de l'entreprise, pour permettre la recherche par entreprise dans une région donnée

        liste_stage -> list[int]
            Contient la liste de stage qu'offre l'entreprise

    Examples
    --------
        *******
        
    Methode 
    -------
        str 

    Examples
    --------
    >>> stage = Entreprise(1196,SFR,"16 rue Lescault,75010",[13,22])
    >>> str(stage)
    "Agent d'accueil"
    """
    def __init__(self,id_entreprise,nom_entreprise,adresse,liste_stage):
        self.id_entreprise = id_entreprise
        self.nom_entreprise = nom_entreprise
        self.adresse = adresse
        self.liste_stage = liste_stage

    def liste_nom_stages(self, id_entreprise):
        """
        Méthode qui prend en entrée une entreprise (son id) et qui renvoie les stages associées.

        Return
        ------
        str
        
        Examples
        --------
        >>> liste_stage=[112,115,452]
        >>> liste_nom_stage(liste_stage)
        ["Conseiller","Directeur Financier","Agent Technique"]
        """
        liste_nom_stage=[]
        for valeur in self.liste_stage:  
            liste_nom_stage.append(Stage(valeur))
        
        return liste_nom_stage
            
    def __str__(self):
        """
        Méthode qui permet de passer pour une même entreprise d'une visualisation machine à une visualisation humaine.
        """
        return "{}, {}".format(self.nom_entreprise,self.liste_nom_stages())