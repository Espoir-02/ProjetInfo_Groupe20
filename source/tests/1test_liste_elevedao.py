import pytest
from source.DAO.ListeEleveDAO import ListeElevesDAO
from source.business_object.utilisateur.eleve import Eleve


def test_update_liste_eleve():
    ma_liste_eleve = ListeElevesDAO()

    eleve = Eleve(nom="Fleur", prenom="Amaryllis", id_eleve=8)
    id_professeur = 10

    # Test avec des paramètres valides
    ma_liste_eleve.update_liste_eleve(eleve, id_professeur)

    # Test avec un id_prof invalide
    with pytest.raises(TypeError) as exc_info:
        ma_liste_eleve.update_liste_eleve(eleve, "pas_un_entier")
    assert str(exc_info.value) == "l'identifiant du professeur est un entier numérique"


def test_get_liste_eleve_by_id():
    ma_liste_eleve = ListeElevesDAO()

    # Tester avec des paramètres valides
    liste = ma_liste_eleve.get_liste_eleve_by_id(id_professeur=10)
    print(liste)
    assert isinstance(liste, list)
    assert all(isinstance(eleve, dict) for eleve in liste)

    # Tester avec un id_professeur invalide
    with pytest.raises(TypeError) as exc_info:
        ma_liste_eleve.get_liste_eleve_by_id(id_professeur="pas_un_entier")
    assert str(exc_info.value) == "l'identifiant du professeur est un entier numérique"


def test_delete_eleve():
    ma_liste_eleve = ListeElevesDAO()

    # Tester avec des paramètres valides
    ma_liste_eleve.delete_eleve(id_eleve=8, id_professeur=10)

    # Tester avec un id_eleve invalide
    with pytest.raises(TypeError) as exc_info:
        ma_liste_eleve.delete_eleve(id_eleve="pas_un_entier", id_professeur=10)
    assert str(exc_info.value) == "l'identifiant de l'élève est un entier numérique"

    # Tester avec un id_professeur invalide
    with pytest.raises(TypeError) as exc_info:
        ma_liste_eleve.delete_eleve(id_eleve=8, id_professeur="pas_un_entier")
    assert str(exc_info.value) == "l'identifiant du professeur est un entier numérique"
