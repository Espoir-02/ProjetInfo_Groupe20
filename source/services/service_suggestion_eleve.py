from ListeEleveDAO import ListeElevesDAO
from SuggestionsDAO import SuggestionsDAO

class ServiceSuggestion:
    def __init__(self):
        pass

    def get_liste_eleve_by_id(self,id_professeur):
        return ListeElevesDAO().get_liste_eleve_by_id(id_professeur)

    def create_suggestion(self, id_eleve, id_stage, id_professeur):
        return SuggestionsDAO().create_suggestion(id_eleve, id_stage, id_professeur)

    def get_suggestions_by_id(self, id_eleve):
        return SuggestionsDAO().get_suggestions_by_id(id_eleve)
  
    def delete_suggestion(self,id_eleve, id_stage):
        return SuggestionsDAO().delete_suggestion(id_eleve,id_stage)
  

    " Méthode où on stocke dans la liste de suggestion de l'élève les suggestions du prof"
    " Méthode permettant à un professeur de faire ds propositions aux élèves "
    " Méthode où le professeur peut consulter la liste de ses élèves"