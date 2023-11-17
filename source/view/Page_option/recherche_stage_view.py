from InquirerPy import inquirer
from source.business_object.stage_recherche.recherche import *


class Recherche_Stage_View:
#    def __init__(self,id_stage):
#        self.id_stage = id_stage
    
    def display(self):
        # Choix des filtres

        # 1) Choix de la ville/département/région :

        choix_echelle = [inquirer.List("choice", message = "Choose an option:", choices=["Toute échelle", "région","département","ville"])]
        answers_echelle = inquirer.prompt(choix_echelle)
        stock_reponse = 0
        region = 0
        departement = 0
        ville = 0

        if answers_echelle['choice'] == "Toute échelle":
            stock_reponse = 0
        
        elif answers_echelle['choice'] == "région":
            region = [inquirer.Text("région", message="région:")]
            stock_reponse = 1
    
        elif answers_echelle['choice'] == "département":
            departement = [inquirer.Text("département", message="département:")]
            stock_reponse = 2

        elif answers_echelle['choice'] == "ville":
            ville = [inquirer.Text("ville", message="ville:")]
            stock_reponse = 3
        
        # 2) Mot-clé
        #mot_cle = [inquirer.Text("mot_cle", message="mot_cle:")]
        #answer_mot_cle = inquirer.prompt(mot_cle)

        # 3) Domaine de formation
        formation = [inquirer.List("choice", message = 'Choose an option:', choices=[
            "Non renseigné", "Agriculture, agroalimentaire, environnement","Arts - Arts appliqués","Assurance, Banque, Immobilier","Commerce, vente, distribution",
            "Communication, culture","Droit, Sc Politique, Economie","Gestion, management, RH","Hôtellerie-restauration, tourisme",
            "Informatique, télécom","Lettres et Sciences humaines","Santé - Sports","Sciences, technologie","Secrétariat - Assistanat",
            "Transports, logistique"
        ])]
        answer_profession = inquirer.prompt(formation)

        # 4) Niveau d'études :
        niveau_etude = [inquirer.List("choice", message = 'Choose an option:', choices=[
            "Non renseigné", "Bac +5","Bac +4","Bac +3","Bac +2","Bac","CAP/BEP","Bac professionnel","3ème"
        ])]
        answer_etude = inquirer.prompt(niveau_etude)

        # 5) Période :
        periode = [inquirer.List("choice", message = 'Choose an option:', choices=["Non renseigné","1 mois","2 mois","3 mois","4 mois","5 mois","6 mois"])]
        answer_periode = inquirer.prompt(periode)
        
        # Lancer la recherche
        stock_recherche = Recherche(
            zone = stock_reponse, region = region, departement = departement, ville = ville, domaine = answer_profession, 
            niveau_etude = answer_etude, periode = answer_periode
        )
        stock_recherche.lancer_recherche() # exécute le scrapping via la classe Recherche

    


    # mettre tous les stages à la liste avec pour chaque stage le titre (position 0), l'entreprise (position 1) et le lieu (position 2)
    # l'user clique dessus et là on affiche toute la liste, plus les boutons "ajouter à la liste d'envie", "suggérer à un élève" pour le prof

if __name__ == "__main__":
    Recherche_Stage_View().display()