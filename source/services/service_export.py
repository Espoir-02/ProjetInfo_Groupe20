from source.DAO.dbconnection import DBConnection
from source.DAO.utilitaire_dao import UtilitaireDAO
from source.exception.exceptions import IdUtilisateurInexistantError
from source.exception.exceptions import IdStageInexistantError
from source.services.scrapping.scrapping import Scrapping


class ExporteurStage:
    @staticmethod
    def exporter_donnees(liste_id_stages, id_utilisateur, chemin_fichier_sortie):
       
        print(f"{'*' * 40}")
        for i in range(1, 20):
                    user_choice = input("Veuillez entrer le numéro du stage que vous voulez exporter(ou tapez 'q' pour quitter): ")
                    if user_choice.lower() == 'q':
                        break

                    try:
                        # Obtenez les informations du stage sélectionné
                        id_stage = liste_id_stages[int(user_choice) - 1]
                        with DBConnection().connection as conn:
                            with conn.cursor() as cursor:
                                cursor.execute(
                                    "SELECT * FROM base_projetinfo.stage "
                                    "WHERE id_stage = %(id_stage)s",
                                    {"id_stage": id_stage[0]},
                                )

                                # Récupération des résultats
                                resultats = cursor.fetchall()
                                # Écriture des résultats dans un fichier texte
                                try:
                                    with open(chemin_fichier_sortie, 'w') as fichier_sortie:
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
                                            print("****Exportation reussie! Veuillez consulter vos fichiers")
                                except Exception as e:
                                    print("Erreur lors de l'écriture dans le fichier :", str(e))
                                    
                    except (ValueError, IndexError):
                        print("Choix invalide. Veuillez entrer un numéro valide.")





