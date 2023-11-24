import pytest
from source.DAO.ListeEnvieDAO import ListeEnvieDAO
from source.exception.exceptions import IdEleveInexistantError
from source.exception.exceptions import IdStageInexistantError


def test_update_liste_envie():
    ma_liste_envie = ListeEnvieDAO()

    # Tester avec des paramètres valides
    ma_liste_envie.update_liste_envie(id_eleve=6, id_stage=403)

    # Tester avec un id_eleve invalide
    with pytest.raises(TypeError) as exc_info:
        ma_liste_envie.update_liste_envie(id_eleve="pas_un_entier", id_stage=403)
    assert str(exc_info.value) == "l'identifiant de l'élève est un entier numérique"

    # Tester avec un id_stage invalide
    with pytest.raises(TypeError) as exc_info:
        ma_liste_envie.update_liste_envie(id_eleve=6, id_stage="pas_un_entier")
    assert str(exc_info.value) == "l'identifiant du stage est un entier numérique"

    # Tester avec un id_eleve qui n'existe pas
    with pytest.raises(IdEleveInexistantError) as exc_info:
        ma_liste_envie.update_liste_envie(id_eleve=999, id_stage=403)
    assert str(exc_info.value) == "L'élève avec l'ID 999 n'existe pas."

    # Tester avec un id_stage qui n'existe pas
    with pytest.raises(IdStageInexistantError) as exc_info:
        ma_liste_envie.update_liste_envie(id_eleve=6, id_stage=88888)
    assert str(exc_info.value) == "Le stage avec l'ID 88888 n'existe pas."


def test_get_liste_envie_by_id():
    ma_liste_envie = ListeEnvieDAO()

    # Tester avec des paramètres valides
    liste = ma_liste_envie.get_liste_envie_by_id(id_eleve=6)
    print(liste)
    assert isinstance(liste, list)
    assert all(isinstance(envie, dict) for envie in liste)

    # Tester avec un id_eleve invalide
    with pytest.raises(TypeError) as exc_info:
        ma_liste_envie.get_liste_envie_by_id(id_eleve="pas_un_entier")
    assert str(exc_info.value) == "l'identifiant de l'élève est un entier numérique"

    # Tester avec un id_eleve qui n'existe pas
    with pytest.raises(IdEleveInexistantError) as exc_info:
        ma_liste_envie.get_liste_envie_by_id(id_eleve=999)
    assert str(exc_info.value) == "L'élève avec l'ID 999 n'existe pas."


def test_delete_liste_envie():
    ma_liste_envie = ListeEnvieDAO()

    # Tester avec des paramètres valides
    ma_liste_envie.delete_liste_envie(id_eleve=6, id_stage=403)

    # Tester avec un id_eleve invalide
    with pytest.raises(TypeError) as exc_info:
        ma_liste_envie.delete_liste_envie(id_eleve="pas_un_entier", id_stage=403)
    assert str(exc_info.value) == "l'identifiant de l'élève est un entier numérique"

    # Tester avec un id_stage invalide
    with pytest.raises(TypeError) as exc_info:
        ma_liste_envie.delete_liste_envie(id_eleve=6, id_stage=[56])
    assert str(exc_info.value) == "l'identifiant du stage est un entier numérique"

    # Tester avec un id_eleve qui n'existe pas
    with pytest.raises(IdEleveInexistantError) as exc_info:
        ma_liste_envie.delete_liste_envie(id_eleve=999, id_stage=403)
    assert str(exc_info.value) == "L'élève avec l'ID 999 n'existe pas."

    # Tester avec un id_stage qui n'existe pas
    with pytest.raises(IdStageInexistantError) as exc_info:
        ma_liste_envie.delete_liste_envie(id_eleve=6, id_stage=88888)
    assert str(exc_info.value) == "Le stage avec l'ID 88888 n'existe pas."

    def test_delete_all_liste_envie(self):
        ma_liste_envie = ListeEnvieDAO()

        # Test avec des paramètres valides
        id_eleve_valide = 6
        ma_liste_envie.delete_all_liste_envie(id_eleve_valide)

        # Test avec un id_eleve invalide
        with pytest.raises(TypeError) as exc_info:
            id_eleve_invalide = "pas_un_entier"
            ma_liste_envie.delete_all_liste_envie(id_eleve_invalide)
        assert (
            str(exc_info.value)
            == "L'identifiant de l'élève doit être un entier numérique"
        )

        # Test avec un id_eleve inexistant
        with pytest.raises(IdEleveInexistantError) as exc_info:
            id_eleve_inexistant = 9999
            ma_liste_envie.delete_all_liste_envie(id_eleve_inexistant)
        assert str(exc_info.value) == "L'élève avec l'identifiant '9999' n'existe pas"
