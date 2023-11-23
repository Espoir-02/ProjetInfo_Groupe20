

class Stage:

    def __init__(self, titre, lien, domaine, salaire, date_publication, periode, niveau_etudes, entreprise, lieu):
        self.titre = titre
        self.lien = lien
        self.domaine = domaine
        self.salaire = salaire
        self.date_publication = date_publication
        self.periode = periode
        self.niveau_etudes= niveau_etudes
        self.entreprise= entreprise
        self.lieu= lieu
        self.id = None

       
    def __str__(self):
        """
        Méthode qui permet de passer pour un même stage d'une visualisation machine à une visualisation humaine.
        """
        return "{}".format(self.nom_stage) # Est ce qu'on rajoute toutes les info concernant le stage ou que le nom ?