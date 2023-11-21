from source.DAO.utilisateur_dao import UtilisateurDAO
from source.business_object.utilisateur.utilisateur2 import Utilisateur
from source.DAO.utilitaire_dao import UtilitaireDAO
from source.exception.exceptions import PseudoDejaExistantError,UtilisateurInexistantError

class ServiceUtilisateur:
    def __init__(self):
        self.utilisateur_dao = UtilisateurDAO()
        self.utilitaire_dao = UtilitaireDAO()

    def creer_utilisateur(self, nom, prenom, pseudo, mot_de_passe, type_utilisateur):
        nouvel_utilisateur = Utilisateur(nom=nom, prenom=prenom, pseudo=pseudo, mot_de_passe=mot_de_passe, type_utilisateur=type_utilisateur)
        utilisateur_cree = self.utilisateur_dao.create_compte(nouvel_utilisateur)
        return utilisateur_cree

    def mettre_a_jour_utilisateur(self, id_utilisateur, nom, prenom, pseudo, mot_de_passe, type_utilisateur):
        utilisateur_existant = self.utilisateur_dao.find_by_id(id_utilisateur)
        if utilisateur_existant:
            utilisateur_existant.nom = nom
            utilisateur_existant.prenom = prenom
            utilisateur_existant.pseudo = pseudo
            utilisateur_existant.mot_de_passe = mot_de_passe
            utilisateur_existant.type_utilisateur = type_utilisateur
            utilisateur_mis_a_jour = self.utilisateur_dao.MAJ_utilisateur(utilisateur_existant)
            #methode a créer dans utilisateur dao
            return utilisateur_mis_a_jour
        else:
            return None

    def supprimer_utilisateur(self, id_utilisateur):
        utilisateur_existant = self.utilisateur_dao.find_by_id(id_utilisateur)
        if utilisateur_existant:
            self.utilisateur_dao.delete_utilisateur(id_utilisateur)
            return True
        else:
            return False

    def trouver_utilisateur_par_id(self, id_utilisateur):
        return self.utilisateur_dao.find_by_id(id_utilisateur)

    def trouver_utilisateur_par_nom(self, nom, prenom):
        try:
            eleve = self.utilisateur_dao.find_by_nom(nom, prenom)

            if eleve is not None:
                return eleve
            else:
                raise UtilisateurInexistantError(f"Aucun utilisateur trouvé avec le nom '{nom}' et le prénom '{prenom}'.")
        except UtilisateurInexistantError as e:
            print(f"Une erreur s'est produite lors de la recherche de l'utilisateur : {e}")

    def get_type_utilisateur(self, pseudo):
        return self.utilisateur_dao.get_type_utilisateur(pseudo)

    def find_id_by_pseudo(self,pseudo):
        return self.utilisateur_dao.find_id_by_pseudo(pseudo)
        
    def maj_mdp(self, pseudo,nouveau_mdp):
        return self.utilisateur_dao.update_utilisateur_mdp(pseudo,nouveau_mdp)
    
    def maj_pseudo(self, id_utilisateur, nouveau_pseudo):
        try:
            if self.utilitaire_dao.check_pseudo_exists(nouveau_pseudo):
                raise PseudoDejaExistantError(nouveau_pseudo)

            print("Pseudo modifié avec succès")
            return self.utilisateur_dao.update_utilisateur_pseudo(id_utilisateur, nouveau_pseudo)
        except PseudoDejaExistantError as e:
            print(f"Erreur de mise à jour du pseudo : {e}")

