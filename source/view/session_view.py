from source.utils.singleton import Singleton


class Session(metaclass=Singleton):
    def __init__(self):
        self.user_id: int = None
        self.user_type: str = "invite"  # Type d'utilisateur par défaut
        self.user_pseudo: str = None
