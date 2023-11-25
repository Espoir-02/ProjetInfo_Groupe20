from source.view.Page_option.recherche_stage_view import Recherche_Stage_View
from source.view.session_view import Session


class AffichageRecherche:
    def __init__(self):
        pass

    def display_additional_info(self, stage_info):
        print(f"{'*' * 40}")
        print(f"Titre: {stage_info['titre']}")
        print(f"Entreprise: {stage_info['entreprise']}")
        print(f"Lieu: {stage_info['lieu']}")
        print(f"Lien du stage: {stage_info['lien']}")
        print(f"{'-' * 40}")
        print(f"Domaine: {stage_info['domaine']}")
        print(f"Etude: {stage_info['etude']}")
        print(f"Période: {stage_info['periode']}")
        print(f"Gratification: {stage_info['gratification']}")
        print(f"Date de publication: {stage_info['date_publication']}")
        print(f"{'*' * 40}\n")

    def display_stage_menu(self, all_stages_info):
        if not all_stages_info:
            print("Aucun stage trouvé.")
            return None

        choix_stage = [
            f"{i + 1}. {stage_info['titre']} - {stage_info['entreprise']} - {stage_info['lieu']}"
            for i, stage_info in enumerate(all_stages_info)
        ] + ["Retour au menu"]

        questions = [
            inquirer.List(
                "selection", message="Sélectionner un stage:", choices=choix_stage
            )
        ]
        answers = inquirer.prompt(questions)

        selected_stage_str = answers["selection"]

        if selected_stage_str.lower() == "retour au menu":
            from source.view.Page_option.menu_view import Menu_view

            return Menu_view().display()
        elif re.match(r"^\d", selected_stage_str):
            selected_stage = int(re.search(r"\d+", selected_stage_str).group())
            selected_stage_info = all_stages_info[selected_stage - 1]
            self.display_additional_info(selected_stage_info)
            return selected_stage_info
        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")
            return None


