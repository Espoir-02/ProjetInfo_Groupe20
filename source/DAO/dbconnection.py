import psycopg2

class DBConnection:
    def __init__(self):
        self.connection = psycopg2.connect(
            user="votre_utilisateur",
            password="votre_mot_de_passe",
            host="votre_host",
            port="votre_port",
            database="votre_base_de_donnees"
        )


