from source.DAO.dbconnection import DBConnection
from source.DAO.utilitaire_dao import UtilitaireDAO
from source.exception.exceptions import IdUtilisateurInexistantError
from source.exception.exceptions import IdStageInexistantError
#from source.services.scrapping.scrapping import Scrapping
#n'importe pas Scrapping dans tout le fichier 
#importe le seulment dans une méthode de cette classe où tu en aura besoin car sinon ça va pas marcher

class ExporteurStage:
    @staticmethod
    def exporter_donnees(id_utilisateur, id_stage, chemin_fichier_sortie):
        print(f"{'*' * 40}")

        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM base_projetinfo.stage "
                    "WHERE id_stage = %(id_stage)s",
                    {"id_stage": id_stage},
                )

                # Récupération des résultats
                resultats = cursor.fetchall()

                # Écriture des résultats dans un fichier texte
                try:
                    with open(chemin_fichier_sortie, 'w', encoding='utf-8') as fichier_sortie:
                    with open(chemin_fichier_sortie, 'w' ) as fichier_sortie:
                        # Écrire l'en-tête avec le nom des colonnes
                        en_tete = "Titre; Lien; Domaine; Periode; Salaire; Date de publication; Niveau d'études; Entreprise; Lieu"
                        fichier_sortie.write(f"{en_tete}\n")

                        for resultat in resultats:
                            # Récupérez les valeurs spécifiques du résultat
                            titre = resultat[0]
                            lien = resultat[1]
                            domaine = resultat[2]
                            periode = resultat[3]
                            salaire = resultat[4]
                            date_publication = resultat[5]
                            niveau_etudes = resultat[6]
                            entreprise = resultat[7]
                            lieu = resultat[8]

                            # Écrire les valeurs dans le fichier avec le séparateur ";"
                            ligne = f"{titre}; {lien}; {domaine}; {periode}; {salaire}; {date_publication}; {niveau_etudes}; {entreprise}; {lieu}"
                            fichier_sortie.write(f"{ligne}\n")
                        
                    print("****Exportation réussie! Veuillez consulter vos fichiers")
                except Exception as e:
                    print("Erreur lors de l'écriture dans le fichier :", str(e))

                except (ValueError, IndexError):
                    print("Choix invalide. Veuillez entrer un numéro valide.")

    @staticmethod
    def exporter_listeEnvies(id_utilisateur, liste_id_stages, chemin_fichier_sortie):
        print(f"{'*' * 40}")

        with DBConnection().connection as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM base_projetinfo.stage "
                    "WHERE id_stage IN %(liste_id_stages)s",
                    {"liste_id_stages": tuple(liste_id_stages)},
                )

                # Récupération des résultats
                resultats = cursor.fetchall()

                # Écriture des résultats dans un fichier texte
                try:
                    with open(chemin_fichier_sortie, 'w', encoding='utf-8') as fichier_sortie:
                        # Écrire l'en-tête avec le nom des colonnes
                        en_tete = "Titre; Lien; Domaine; Periode; Salaire; Date de publication; Niveau d'études; Entreprise; Lieu"
                        fichier_sortie.write(f"{en_tete}\n")

                        for resultat in resultats:
                            # Récupérez les valeurs spécifiques du résultat
                            titre = resultat[1]
                            lien = resultat[2]
                            domaine = resultat[3]
                            periode = resultat[4]
                            salaire = resultat[5]
                            date_publication = resultat[6]
                            niveau_etudes = resultat[7]
                            entreprise = resultat[8]
                            lieu = resultat[]

                            # Écrire les valeurs dans le fichier avec le séparateur ";"
                            ligne = f"{titre}; {lien}; {domaine}; {periode}; {salaire}; {date_publication}; {niveau_etudes}; {entreprise}; {lieu}"
                            fichier_sortie.write(f"{ligne}\n")
                        
                    print("****Exportation réussie! Veuillez consulter vos fichiers")
                except Exception as e:
                    print("Erreur lors de l'écriture dans le fichier :", str(e))

                except (ValueError, IndexError):
                    print("Choix invalide. Veuillez entrer un numéro valide.")
        
# Exemple d'utilisation 
# liste_id_stages = [511,512,513,514]
#chemin_fichier_sortie = "ListeEnvies.csv" 
# Appel de la méthode exporter_listeEnvies
#ExporteurStage.exporter_listeEnvies(9, liste_id_stages, chemin_fichier_sortie)