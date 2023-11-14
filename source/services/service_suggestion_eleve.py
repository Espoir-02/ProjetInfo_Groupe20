from ListeEleveDAO import ListeElevesDAO

class ServiceSuggestion:
    def __init__(self):
        pass

    def get_liste_eleve_by_id(self,id_professeur):
        return ListeElevesDAO().get_liste_eleve_by_id(id_professeur)

    " Méthode où on stocke dans la liste de suggestion de l'élève les suggestions du prof"
    " Méthode permettant à un professeur de faire ds propositions aux élèves "
    " Méthode où le professeur peut consulter la liste de ses élèves"