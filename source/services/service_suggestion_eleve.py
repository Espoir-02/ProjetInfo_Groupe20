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
        return self.suggestions_dao.create_suggestion(id_eleve, id_stage, id_professeur)

    def get_suggestions_by_id(self, id_eleve):
        return self.suggestions_dao.get_suggestions_by_id(id_eleve)
  
    def delete_suggestion(self,id_eleve, id_stage):
        try:
            # Vérifier si l'utilisateur existe avant de le supprimer
            if not self.utilitaire_dao.check_stage_exists(id_stage):
                raise IdStageInexistantError(id_stage)

            return self.suggestions_dao.delete_suggestion(id_eleve, id_stage)
        except IdStageInexistantError as e:
            print(f"Erreur lors de la suppression de la suggestion : {e}")
  
    def vider_liste_suggestions(self,id_eleve):
        if not self.utilitaire_dao.check_liste_suggestions_exists(id_eleve):
            print("La liste de suggestions est déjà vide.")
            return False
        else :
            print("Liste de suggestions vidées avec succès")
            succes = self.suggestions_dao.delete_all_suggestions(id_eleve)
            return succes

