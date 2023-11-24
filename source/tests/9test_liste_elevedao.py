import pytest
from source.DAO.ListeEleveDAO import ListeElevesDAO
from source.business_object.utilisateur.eleve import Eleve
from source.exception.exceptions import IdEleveInexistantError
from source.exception.exceptions import IdProfesseurInexistantError


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

    # Tester avec un id_eleve qui n'existe pas
    eleve2 = Eleve(nom="Fleur", prenom="Amaryllis", id_eleve=999)

    with pytest.raises(IdEleveInexistantError) as exc_info:
        ma_liste_eleve.update_liste_eleve(eleve2, id_professeur)
    assert str(exc_info.value) == "L'élève avec l'ID 999 n'existe pas."

    # Tester avec un id_professeur qui n'existe pas
    with pytest.raises(IdProfesseurInexistantError) as exc_info:
        ma_liste_eleve.update_liste_eleve(eleve, id_professeur=999)
    assert str(exc_info.value) == "Le professeur avec l'ID 999 n'existe pas."


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

    # Tester avec un id_professeur qui n'existe pas
    with pytest.raises(IdProfesseurInexistantError) as exc_info:
        ma_liste_eleve.get_liste_eleve_by_id(id_professeur=999)
    assert str(exc_info.value) == "Le professeur avec l'ID 999 n'existe pas."


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

    # Tester avec un id_eleve qui n'existe pas
    with pytest.raises(IdEleveInexistantError) as exc_info:
        ma_liste_eleve.delete_eleve(id_eleve=999, id_professeur=10)
    assert str(exc_info.value) == "L'élève avec l'ID 999 n'existe pas."

    def test_delete_all_liste(self):
        ma_liste = ListeElevesDAO()

        # Test avec des paramètres valides
        id_professeur_valide = 18
        ma_liste.delete_all_liste(id_professeur_valide)

        # Test avec un id_professeur invalide (type incorrect)
        with pytest.raises(TypeError) as exc_info:
            id_professeur_invalide = "pas_un_entier"
            ma_liste.delete_all_liste(id_professeur_invalide)
        assert (
            str(exc_info.value)
            == "L'identifiant du professeur doit être un entier numérique"
        )

        # Test avec un id_professeur inexistant
        with pytest.raises(IdProfesseurInexistantError) as exc_info:
            id_professeur_inexistant = 9999
            ma_liste.delete_all_liste(id_professeur_inexistant)
        assert (
            str(exc_info.value)
            == "Le professeur avec l'identifiant '9999' n'existe pas"
        )
