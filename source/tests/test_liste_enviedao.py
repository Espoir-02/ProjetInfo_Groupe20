import pytest
from source.DAO.ListeEnvieDAO import ListeEnvieDAO


def test_update_liste_envie():
    ma_liste_envie = ListeEnvieDAO()

    # Tester avec des paramètres valides
    ma_liste_envie.update_liste_envie(id_utilisateur=1, id_stage=42)

    # Tester avec un id_utilisateur invalide
    with pytest.raises(TypeError) as exc_info:
        ma_liste_envie.update_liste_envie(id_utilisateur="pas_un_entier", id_stage=42)
    assert str(exc_info.value) == "l'identifiant de l'utilisateur est un entier numérique"

    # Tester avec un id_stage invalide
    with pytest.raises(TypeError) as exc_info:
        ma_liste_envie.update_liste_envie(id_utilisateur=1, id_stage="pas_un_entier")
    assert str(exc_info.value) == "l'identifiant du stage est un entier numérique"


def test_delete_liste_envie():
    ma_liste_envie = ListeEnvieDAO()

    # Tester avec des paramètres valides
    ma_liste_envie.delete_liste_envie(id_utilisateur=1, id_stage=42)

    # Tester avec un id_utilisateur invalide
    with pytest.raises(TypeError) as exc_info:
        ma_liste_envie.update_liste_envie(id_utilisateur="pas_un_entier", id_stage=42)
    assert str(exc_info.value) == "l'identifiant de l'utilisateur est un entier numérique"

    # Tester avec un id_stage invalide
    with pytest.raises(TypeError) as exc_info:
        ma_liste_envie.update_liste_envie(id_utilisateur=1, id_stage=[56])
    assert str(exc_info.value) == "l'identifiant du stage est un entier numérique"


def test_get_liste_envie_by_id():
    ma_liste_envie = ListeEnvieDAO()

    # Tester avec des paramètres valides
    ma_liste_envie.get_liste_envie_by_id(id_utilisateur=6)

    # Tester avec un id_utilisateur invalide
    with pytest.raises(TypeError) as exc_info:
        ma_liste_envie.update_liste_envie(id_utilisateur="pas_un_entier")
    assert str(exc_info.value) == "l'identifiant de l'utilisateur est un entier numérique"
