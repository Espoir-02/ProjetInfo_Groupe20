import psycopg2

class DBConnection:
    def __init__(self):
        self.connection = psycopg2.connect(
            user="id2225",
            password="id2225",
            host="sgbd-eleves.domensai.ecole",
            port="5432",
            database="id2225",
        )

try:
    db = DBConnection()
    print("La connexion à la base de données a réussi.")
except Exception as e:
    print(f"Erreur lors de la connexion à la base de données : {e}")
