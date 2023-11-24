from source.view.session_view import Session
from source.services.service_utilisateur import ServiceUtilisateur

class MesInfos:
    def display(self):
        service = ServiceUtilisateur()
        return service.information(Session().user_id)
    
    def make_choice(self):
        return display()