from InquirerPy import inquirer

class StartView:
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
        
from source.business_object.listes.historique import Historique

class HistoriqueView:
    def __init__(self,id_historique):
        self.id_historique = id_historique

    def display(self):
        # Récupère une liste de l'historique selon l'id_historique
        historique_courant = self.id_historique.get_historique()

        # Affiche une liste de choix pour sélectionner un Pokémon
        questions = [inquirer.List('select_stage', 'exit')]
        answers = inquirer.prompt(questions)

        if answers['choice'] == "select_stage":
            # Redirige vers la vue Stage avec un certain id
            return Recherche_Stage_View
    
        else:
            # Termine l'application
            return 'Exit'
        
from source.business_object.stage_recherche.recherche import Recherche

class Recherche_Stage_View:
    def __init__(self,id_stage):
        self.id_stage = id_stage
    
    def display(self):
        # Choix des filtres

        # Choix du salaire :
        salary = [inquirer.List('choice', message = 'Choose an option:', choices=['None', ">= 20 000","40 000","60 000","80 000","100 000"])]
        Recherche.changer_salaire(inquirer.prompt(salary))

        # Choix de la durée :
        duree = [inquirer.List('choice', message = 'Choose an option:', choices=['None','1',"3", "4","6"])]
        answer_duree = int(inquirer.prompt(duree))

        # Choix du télétravail :
        teletravail = [inquirer.List('choice', message = 'Choose an option:', choices=['Inconnu','non'])]
        answer_teletravail = inquirer.prompt(teletravail)

        # Choix de la profession :
        profession = [inquirer.List('choice', message = 'Choose an option:', choices=['oui','non'])]
        answer_profession = inquirer.prompt(profession)

        return Class.scrapping(answer_duree,answer_salary)
        return blablz.recherche({salary=answer_salary,domaine=None, Type=answer_teletravail,duree=answer_duree})
        profession=None,
        secteur=None,
        taille_entreprise=None,
        niveau_experience=None,
        niveau_etude=None,
        salaire_minimum=None,
    ):
        self.duree = duree
        self.teletravail = teletravail
        self.profession = profession
        self.secteur = secteur
        self.taille_entreprise = taille_entreprise
        self.niveau_experience = niveau_experience
        self.niveau_etude = niveau_etude
        self.salaire_minimum = salaire_minimum
