from source.exception.exceptions import IdUtilisateurInexistantError, IdEleveInexistantError
from source.exception.exceptions import IdStageInexistantError
from source.services.service_stage import StageService
from source.services.service_liste_envie import ListeEnvieService
from source.services.service_historique import HistoriqueService
from source.services.service_suggestion_eleve import ServiceSuggestion


class ExporteurStage:

    @staticmethod
    def exporter_donnees(id_stage, chemin_fichier_sortie):
        print(f"{'*' * 40}")
        chemin_fichier_sortie = "source/Fichiers_exportes/" + chemin_fichier_sortie
        stage_service = StageService()

        try:
            stage = stage_service.find_stage_by_id(id_stage)
            if not stage:
                print(f"Aucun stage trouvé avec l'identifiant {id_stage}")
                return

            with open(chemin_fichier_sortie, "w", encoding="utf-8") as fichier_sortie:
                # Écrire l'en-tête avec le nom des colonnes
                en_tete = "Titre; Lien; Domaine; Periode; Salaire; Date de publication; Niveau d'études; Entreprise; Lieu"
                fichier_sortie.write(f"{en_tete}\n")

            # Écrire chaque information sur une ligne différente
                fichier_sortie.write(f"Titre: {stage['titre']}\n")
                fichier_sortie.write(f"Lien: {stage['lien']}\n")
                fichier_sortie.write(f"Domaine: {stage['domaine']}\n")
                fichier_sortie.write(f"Période: {stage['periode']}\n")
                fichier_sortie.write(f"Salaire: {stage['salaire']}\n")
                fichier_sortie.write(
                    f"Date de publication: {stage['date_publication']}\n"
                )
                fichier_sortie.write(f"Niveau d'études: {stage['niveau_etudes']}\n")
                fichier_sortie.write(f"Entreprise: {stage['entreprise']}\n")
                fichier_sortie.write(f"Lieu: {stage['lieu']}\n")

            print("****Exportation réussie! Veuillez consulter vos fichiers")

        except Exception as e:
            print("Erreur lors de l'écriture dans le fichier :", str(e))


    @staticmethod
    def exporter_listeEnvies(id_utilisateur, chemin_fichier_sortie):
        print(f"{'*' * 40}")
        chemin_fichier_sortie = "source/Fichiers_exportes/" + chemin_fichier_sortie
        ma_liste = ListeEnvieService()
        try:
            liste_envies = ma_liste.get_liste_envie_eleve(id_utilisateur)
        except ListeEnvieVideError as e:
            print(f"La liste d'envies est vide : {str(e)}")
            return

        try:
            with open(chemin_fichier_sortie, "w", encoding="utf-8") as fichier_sortie:
                en_tete = "ID Stage; Titre; Lien; Domaine"
                fichier_sortie.write(f"{en_tete}\n")

                for envie in liste_envies:
                    id_stage, titre, lien, domaine = (
                        envie["id_stage"],
                        envie["titre"],
                        envie["lien"],
                        envie["domaine"],
                    )

                    ligne = f"{id_stage}; {titre}; {lien}; {domaine}"
                    fichier_sortie.write(f"{ligne}\n")

                print("****Exportation réussie! Veuillez consulter vos fichiers")
        except Exception as e:
            print("Erreur lors de l'écriture dans le fichier :", str(e))

    @staticmethod
    def exporter_historique(id_utilisateur, chemin_fichier_sortie):
        print(f"{'*' * 40}")
        chemin_fichier_sortie = "source/Fichiers_exportes/" + chemin_fichier_sortie
        ma_liste = HistoriqueService()
        try:
            historique = ma_liste.get_all_historique_by_id(id_utilisateur)
        except ListeEnvieVideError as e:
            print(f"La liste d'envies est vide : {str(e)}")
            return

        try:
            with open(chemin_fichier_sortie, "w", encoding="utf-8") as fichier_sortie:
                en_tete = "ID Stage; Titre; Lien; Domaine"
                fichier_sortie.write(f"{en_tete}\n")

                for historique in historique:
                    id_stage, titre, lien, domaine = (
                        historique["id_stage"],
                        historique["titre"],
                        historique["lien"],
                        historique["domaine"],
                    )

                    ligne = f"{id_stage}; {titre}; {lien}; {domaine}"
                    fichier_sortie.write(f"{ligne}\n")

                print("****Exportation réussie! Veuillez consulter vos fichiers")
        except Exception as e:
            print("Erreur lors de l'écriture dans le fichier :", str(e))

    @staticmethod
    def exporter_suggestions(id_eleve, chemin_fichier_sortie):
        print(f"{'*' * 40}")
        chemin_fichier_sortie = "source/Fichiers_exportes/" + chemin_fichier_sortie
        mes_suggestions = ServiceSuggestion()
        try:
            suggestions = mes_suggestions.get_suggestions_by_id(id_eleve)
        except IdEleveInexistantError(id_eleve) as e:
            print(f"Élève inexistant : {str(e)}")
            return

        try:
            with open(chemin_fichier_sortie, "w", encoding="utf-8") as fichier_sortie:
                en_tete = "ID Stage; Titre; Lien; Domaine; ID Professeur"
                fichier_sortie.write(f"{en_tete}\n")

                for suggestion in suggestions:
                    id_stage, titre, lien, domaine, id_professeur = (
                        suggestion["id_stage"],
                        suggestion["titre"],
                        suggestion["lien"],
                        suggestion["domaine"],
                        suggestion["id_professeur"],
                    )

                    ligne = f"{id_stage}; {titre}; {lien}; {domaine}; {id_professeur}"
                    fichier_sortie.write(f"{ligne}\n")

                print(
                    "**** Exportation de la liste de suggestions réussie! Veuillez consulter vos fichiers.\n"
                )
        except Exception as e:
            print("Erreur lors de l'écriture dans le fichier :", str(e))

