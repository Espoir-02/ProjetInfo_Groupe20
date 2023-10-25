from source.business_object.utilisateur.non_authentifie import Non_Authentifie

class Eleve(Non_Authentifie):
    def __init__(self,id, id_historique, nom, prenom, id_list_voeux, id_suggestion):
        super().__init__(id, id_historique)
        self.nom = nom
        self.prenom = prenom
        self.voeux = id_list_voeux
        self.suggestion = id_suggestion

    