from source.DAO.utilisateur_dao import UtilisateurDAO
from source.business_object.utilisateur.utilisateur2 import Utilisateur
from source.DAO.utilitaire_dao import UtilitaireDAO
from source.exception.exceptions import PseudoDejaExistantError, UtilisateurInexistantError

class ServiceUtilisateur:
    def __init__(self):
        self.utilisateur_dao = UtilisateurDAO()
        self.utilitaire_dao = UtilitaireDAO()

    def creer_utilisateur(self, utilisateur):
        utilisateur_cree = self.utilisateur_dao.create_compte(utilisateur)
        return utilisateur_cree


    def creer_compte_anonyme(self):
        utilisateur_invite=Utilisateur("invité",None,None,None,None)
        nouvel_utilisateur_invite=self.utilisateur_dao.create_compte(utilisateur_invite)
        return nouvel_utilisateur_invite


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
        try :
            if nouveau_mdp is None:
                raise ValueError("Le mot de passe ne peut pas être vide")

            return self.utilisateur_dao.update_utilisateur_mdp(pseudo,nouveau_mdp)
        except ValueError as e:
            print(f"Erreur de mise à jour du mot de passe : {e}")

    
    def maj_pseudo(self, id_utilisateur, nouveau_pseudo):
        try:
            if nouveau_pseudo is None:
                print("Le pseudo ne peut pas être None. Modification annulée.")
                return

            if self.utilitaire_dao.check_pseudo_exists(nouveau_pseudo):
                raise PseudoDejaExistantError(nouveau_pseudo)

            return self.utilisateur_dao.update_utilisateur_pseudo(id_utilisateur, nouveau_pseudo)
        except PseudoDejaExistantError as e:
            print(f"Erreur de mise à jour du pseudo : {e}")
        except ValueError as e:
            print(f"Erreur de mise à jour du pseudo : {e}")
    
    def information(self,id_utilisateur):
        utilisateur_existant = self.utilisateur_dao.find_by_id(id_utilisateur)
        return utilisateur_existant["nom"],utilisateur_existant["prénom"]
        #print(f'Nom : {utilisateur_existant["nom"]} \nPrénom : {utilisateur_existant["prénom"]}')

