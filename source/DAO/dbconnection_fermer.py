import psycopg2

def close_all_connections(database, user, password, host, port):
    try:
        # Établir une connexion à la base de données PostgreSQL
        connection = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )

        

        # Créer un objet curseur pour exécuter des requêtes
        cursor = connection.cursor()

        # Exécuter la requête pour fermer toutes les connexions actives
        cursor.execute("""
            SELECT pg_terminate_backend(pid)
            FROM pg_stat_activity
            WHERE datname = %s
              AND state = 'active';
        """, (database,))

        # Valider et fermer la transaction
        connection.commit()

    except psycopg2.Error as e:
        print("Erreur lors de la fermeture des connexions:", e)

    finally:
        # Fermer le curseur et la connexion
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Exemple d'utilisation
close_all_connections(
            user="id2225",
            password="id2225",
            host="sgbd-eleves.domensai.ecole",
            port="5432",
            database="id2225"
)
