from InquirerPy import inquirer

class Menu_view:
    def display(self, type_utilisateur):
        # Affiche le menu principal
        choices = ['Rechercher un stage', 'Accéder à son historique', 'Exit']

        if type_utilisateur in ['professeur', 'eleve', 'administrateur']:
            choices.append("Accéder à sa liste d'envie")

        questions = [inquirer.List('choice', message='Choose an option:', choices=choices)]

        answers = inquirer.prompt(questions)

        if answers['choice'] == 'Rechercher un stage':
            # Redirige vers la vue Stage
            return 'Recherche_Stage_View'
        
        elif answers['choice'] == 'Accéder à son historique':
            # Redirige vers la vue Historique
            return 'Historique_View'
        
        elif (type_utilisateur in ['professeur', 'eleve', 'administrateur']) and (answers['choice'] == "Accéder à sa liste d'envie"):
            # Redirige vers la vue Envies_View pour les utilisateurs authentifiés
            return 'Envies_View'

        else:
            # Termine l'application
            return 'Exit'