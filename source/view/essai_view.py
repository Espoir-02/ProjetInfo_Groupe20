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
        salary = [inquirer.List("choice", message = "Choose an option:", choices=["None", ">= 20 000","40 000","60 000","80 000","100 000"])]
        Recherche.changer_salaire(inquirer.prompt(salary))

        # Choix de la durée :
        duree = [inquirer.List('choice', message = 'Choose an option:', choices=['None','1-3 mois',"4-6 mois","7-12 mois","13-24 mois","25-36 mois"])]
        Recherche.changer_duree(inquirer.prompt(duree))

        # Choix du télétravail :
        teletravail = [inquirer.List("choice", message = "Choose an option:", choices=["Inconnu","Télétravail occasionnel","Télétravail régulier","Ouvert au télétravail total"])]
        Recherche.changer_teletravail(inquirer.prompt(teletravail))

        # Choix de la profession :
        profession = [inquirer.List("choice", message = 'Choose an option:', choices=[
            "Audit / Finance / Assurance","Business","Conseil","Créa","Hôtellerie / Restauration","Immobilier","Industrie","Marketing / Communication",
            "Media","Métiers de la mode","Relation client","Retail","Santé / Médical / Social","Support","Tech","Tourisme"
        ])]
        answer_profession = inquirer.prompt(profession)

        # Choix de la taille de l'entreprise :

        # Choix du secteur :
        secteur = [inquirer.List("choice", message = 'Choose an option:', choices=[
            "Architecture","Association / ONG","Banques / Assurances / Finance","Conseil / Audit","Culture / Média / Divertissement","Distribution","Education / Formation / Recrutement",
            "Food et boisson","Hôtellerie / Tourisme / Loisirs","Immobilier","Industrie","Ingénierie"," Légal / Justice","Mobilité / Transport","Mode / Luxe / Beauté / Art de vivre",
            "Publicité ....................."
        ])]
        answer_profession = inquirer.prompt(secteur)

        # Choix du niveau d'expérience :

        # Choix du niveau d'étude :

        # Choix du salaire minimum :

        return #Class.scrapping(answer_duree,answer_salary)
