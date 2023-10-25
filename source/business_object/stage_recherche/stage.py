class Stage:
    """
    Classe permettant de filtrer la recherche de stage suivant différents critères : Salaire, Domaine, Modalité, Date de début, Date de fin.

    Attributs
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
    def __init__(self,id_stage,id_entreprise_stage, nom_stage,debut,fin,salaire,domaine,modalites):
        self.id_stage = id_stage
        self.id_entreprise_stage = id_entreprise_stage
        self.nom_stage=nom_stage
        self.debut = debut
        self.fin = fin
        self.salaire=salaire
        self.modalites=modalites
       
    def __str__(self):
        return "{}".format(self.nom_stage) # Est ce qu'on rajoute toutes les info concernant le stage ou que le nom ?