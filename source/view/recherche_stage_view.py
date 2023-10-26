from InquirerPy import inquirer
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