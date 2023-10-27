
class IdUtilisateurInexistantError(Exception):
    def __init__(self, id_utilisateur):
        self.id_utilisateur = id_utilisateur
        super().__init__(f"L'utilisateur avec l'ID {id_utilisateur} n'existe pas.")

 
class IdStageInexistantError(Exception):
    def __init__(self, id_stage):
        self.id_stage = id_stage
        super().__init__(f"Le stage avec l'ID {id_stage} n'existe pas.")


class IdEleveInexistantError(Exception):
    def __init__(self, id_eleve):
        self.id_eleve = id_eleve
        super().__init__(f"L'élève avec l'ID {id_eleve} n'existe pas.")