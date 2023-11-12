from source.DAO.utilisateur import UtilisateurDAO
from source.business_object.utilisateur.Utilisateur import Utilisateur

class UtilisateurService:
    def __init__(self):
        self.utilisateur_dao = UtilisateurDAO()

    def creer_compte(self, nom, prenom, pseudo, mot_de_passe, type_utilisateur):
        # Créer un nouvel utilisateur
        nouvel_utilisateur = Utilisateur(nom=nom, prenom=prenom, pseudo=pseudo, mot_de_passe=mot_de_passe, type_utilisateur=type_utilisateur)
        utilisateur_cree = self.utilisateur_dao.create_compte(nouvel_utilisateur)
        return utilisateur_cree

    def authentifier(self, pseudo, mot_de_passe):
        # Vérifier l'authentification de l'utilisateur
        mot_de_passe_utilisateur = self.utilisateur_dao.find_mdp(pseudo)
        if mot_de_passe_utilisateur and mot_de_passe == mot_de_passe_utilisateur:
            return True
        return False

    def utilisateur_authentifier_verif(self,id_utilisateur):
        # A implementer
        
    def recuperer_informations(self, pseudo):
        # Récupérer les informations de l'utilisateur
        utilisateur = self.utilisateur_dao.find_by_nom(pseudo)
        return utilisateur

    class ServiceUtilisateur:
    def __init__(self):
        self.utilisateur_dao = UtilisateurDAO()

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
        return self.utilisateur_dao.find_by_nom(nom, prenom)
        
    
    