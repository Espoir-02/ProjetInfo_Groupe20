from source.DAO.ListeEleveDAO import ListeElevesDAO
from source.DAO.SuggestionsDAO import SuggestionsDAO
from source.DAO.utilitaire_dao import UtilitaireDAO
from source.exception.exceptions import IdStageInexistantError

class ServiceSuggestion:
    def __init__(self):
        self.utilitaire_dao = UtilitaireDAO()
        self.suggestions_dao = SuggestionsDAO()

    def get_liste_eleve_by_id(self,id_professeur):
        return ListeElevesDAO().get_liste_eleve_by_id(id_professeur)

    def create_suggestion(self, id_eleve, id_stage, id_professeur):
        return SuggestionsDAO().create_suggestion(id_eleve, id_stage, id_professeur)

    def get_suggestions_by_id(self, id_eleve):
        return SuggestionsDAO().get_suggestions_by_id(id_eleve)
  
    def delete_suggestion(self,id_eleve, id_stage):
        try:
            # Vérifier si l'utilisateur existe avant de le supprimer
            if not self.utilitaire_dao.check_stage_exists(id_stage):
                raise IdStageInexistantError(id_stage)

            print("Suggestion supprimée avec succès")
            return self.suggestions_dao.delete_suggestion(id_eleve, id_stage)
        except IdStageInexistantError as e:
            print(f"Erreur lors de la suppression de la suggestion : {e}")
  

    " Méthode où on stocke dans la liste de suggestion de l'élève les suggestions du prof"
    " Méthode permettant à un professeur de faire ds propositions aux élèves "
    " Méthode où le professeur peut consulter la liste de ses élèves"