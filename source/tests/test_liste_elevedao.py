import pytest
from source.DAO.ListeEleveDAO import ListeElevesDAO


def test_update_liste_eleve():
    ma_liste_eleve = ListeElevesDAO()

    eleve = Eleve(nom="Dupont", prenom="Jean", id_eleve=1)
    id_prof = 85

    # Test avec des paramètres valides
    ma_liste_eleve.update_liste_eleve(eleve, id_prof)

    # Test avec un id_prof invalide
    with pytest.raises(TypeError) as exc_info:
        ma_liste_eleve.update_liste_eleve(eleve, "pas_un_entier")
    assert str(exc_info.value) == "l'identifiant du professeur est un entier numérique"


def test_get_liste_eleve_by_id():
    ma_liste_eleve = ListeElevesDAO()

    # Tester avec des paramètres valides
    ma_liste_eleve.get_liste_eleve_by_id(id_prof=85)

    # Tester avec un id_prof invalide
    with pytest.raises(TypeError) as exc_info:
        ma_liste_eleve.get_liste_eleve_by_id(id_prof="pas_un_entier")
    assert str(exc_info.value) == "l'identifiant du professeur est un entier numérique"


def test_delete_eleve():
    ma_liste_eleve = ListeElevesDAO()

    # Tester avec des paramètres valides
    ma_liste_eleve.delete_liste_eleve(id_eleve=6, id_prof=85)

    # Tester avec un id_eleve invalide
    with pytest.raises(TypeError) as exc_info:
        ma_liste_eleve.delete_liste_eleve(id_eleve="pas_un_entier", id_prof=85)
    assert str(exc_info.value) == "l'identifiant de l'élève est un entier numérique"

    # Tester avec un id_prof invalide
    with pytest.raises(TypeError) as exc_info:
        ma_liste_eleve.delete_liste_eleve(id_eleve=6, id_prof="pas_un_entier")
    assert str(exc_info.value) == "l'identifiant du professeur est un entier numérique"
