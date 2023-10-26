from InquirerPy import inquirer

class Menu_view:
    def display(self):
        # Affiche le menu principal
        questions = [inquirer.List('choice', message = 'Choose an option:', choices=['Rechercher un stage', 'Accéder à son historique', "Accéder à sa liste d'envie","Exit"])]
        answers = inquirer.prompt(questions)

        if answers['choice'] == 'Rechercher un stage':
            # Redirige vers la vue Stage
            return 'Recherche_Stage_View'
        
        elif answers['choice'] == 'Accéder à son historique':
            # Redirige vers la vue Historique
            return 'Historique_View'
        
        elif answers['choice'] == "Accéder à sa liste d'envie":
            # Redirige vers la vue Historique
            return 'Envies_View'

        else:
            # Termine l'application
            return 'Exit'