import pytest
from source.DAO.ListeEnvieDAO import ListeEnvieDAO


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


def test_delete_liste_envie():
    ma_liste_envie = ListeEnvieDAO()

    # Tester avec des paramètres valides
    ma_liste_envie.delete_liste_envie(id_eleve=6, id_stage=403)

    # Tester avec un id_eleve invalide
    with pytest.raises(TypeError) as exc_info:
        ma_liste_envie.update_liste_envie(id_eleve="pas_un_entier", id_stage=403)
    assert str(exc_info.value) == "l'identifiant de l'élève est un entier numérique"

    # Tester avec un id_stage invalide
    with pytest.raises(TypeError) as exc_info:
        ma_liste_envie.update_liste_envie(id_eleve=6, id_stage=[56])
    assert str(exc_info.value) == "l'identifiant du stage est un entier numérique"
