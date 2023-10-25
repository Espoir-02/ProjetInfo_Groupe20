from source.business_object.stage_recherche.stage import Stage

class Entreprise:
    """
    Classe permettant de filtrer la recherche de stage par entreprise.

    Attributs
    ---------
        id_entreprise -> int 
            Identification de manière unique chaque entreprise dns la base de données

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

    def liste_nom_stage(self):
      """
      Méthode liste_nom_stage -> str 
        Méthode qui prend renvoie la liste des noms de stage que propose une entreprise 
    
      Examples
      -------
    
      >>> liste_stage=[112,115,452]
      >>> liste_nom_stage(liste_stage)
      ["Conseiller","Directeur Financier","Agent Technique"]
      """
      liste_nom_stage=[]
      for valeur in self.liste_stage:  
          liste_nom_stage.append(Stage(valeur))
            

    def __str__(self):
      return "{}, {}".format(self.nom_entreprise,self.liste_nom_stage())
    
# Je m'appelle Enzo