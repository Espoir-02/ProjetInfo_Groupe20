import pytest
import re
from ListeEleveDAO import delete_eleve
from ListeEleveDAO import get_liste_eleve_by_id
from ListeEleveDAO import ListeEleve
from dbconnection import DBConnection


@pytest.mark.parametrize(
    "params, erreur, message_erreur",
    [
        (
            {"id_prof": [4]},
            TypeError,
            "les arguments doivent être des instances int",
        ),
    ],
)
def test_get_liste_eleve_by_id_parametres(params, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        get_liste_eleve_by_id(**params)


@pytest.mark.parametrize(
    "params, erreur, message_erreur",
    [
        (
            {
                "id_eleve": 2,
                "id_prof": "Mr Y",
            },
            TypeError,
            "l'identifiant du professeur est une valeur numérique",
        ),
        (
            {"id_eleve": {2}, 
            "id_prof": 450,
            },
            TypeError,
            "l'identifiant de l'élève est une valeur int",
        ),
    ],
)
def test_delete_eleve_parametres(params, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        delete_eleve(**params)



# Écrivez un cas de test pour la fonction update_liste_eleve
def test_update_liste_eleve():
    # Créez une instance de la classe Eleve (ou utilisez une instance réelle si vous en avez une)
    eleve = Eleve(nom="Doe", prenom="John", id_eleve=1) # Remplacez ces valeurs par celles de votre élève

    # Appelez la fonction update_liste_eleve avec les arguments nécessaires
    id_prof = 123 # Remplacez par l'ID du professeur concerné
    ListeEleve().update_liste_eleve(eleve, id_prof)

    # Maintenant, vous pouvez vérifier si l'élève a été correctement ajouté à la liste
    # Vous pouvez faire une requête pour récupérer la liste d'élèves du professeur et vérifier si l'élève y est.
