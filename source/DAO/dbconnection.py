import psycopg2

class DBConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                user="id2225",
                password="id2225",
                host="sgbd-eleves.domensai.ecole",
                port="5432",
                database="id2225",
            )
        except Exception as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")
            # Si une exception se produit, assurez-vous de ne pas essayer de fermer la connexion ici

    def close_connection(self):
        if hasattr(self, 'connection') and self.connection is not None:
            self.connection.close()
            print("La connexion à la base de données a été fermée.")

# Utilisation de la classe DBConnection
try:
    db = DBConnection()
    # Faites vos opérations de base de données ici

    # Fermez la connexion lorsque vous avez terminé
    db.close_connection()

except Exception as e:
    print(f"Erreur lors de la connexion à la base de données : {e}")
