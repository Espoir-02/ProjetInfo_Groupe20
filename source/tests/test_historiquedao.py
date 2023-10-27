import pytest
from source.DAO.HistoriqueDAO import HistoriqueDAO
from source.DAO.dbconnection import DBConnection


def test_get_all_historique_by_id():
    mon_historique = HistoriqueDAO()

    # Tester avec des paramètres valides
    historique = mon_historique.get_all_historique_by_id(id_utilisateur=1)
    assert isinstance(historique, list)
    assert all(isinstance(recherche, dict) for recherche in historique)

    # Tester avec un id_utilisateur invalide
    with pytest.raises(TypeError) as exc_info:
        mon_historique.get_all_historique_by_id(id_utilisateur="pas_un_entier")
    assert (
        str(exc_info.value) == "l'identifiant de l'utilisateur est un entier numérique"
    )


def test_update_historique():
    mon_historique = HistoriqueDAO()

    # Tester avec des paramètres valides
    mon_historique.update_historique(id_utilisateur=1, id_stage=42)

    # Tester avec un id_utilisateur invalide
    with pytest.raises(TypeError) as exc_info:
        mon_historique.update_historique(id_utilisateur="pas_un_entier", id_stage=42)
    assert (
        str(exc_info.value) == "l'identifiant de l'utilisateur est un entier numérique"
    )

    # Tester avec un id_stage invalide
    with pytest.raises(TypeError) as exc_info:
        mon_historique.update_historique(id_utilisateur=1, id_stage="pas_un_entier")
    assert str(exc_info.value) == "l'identifiant du stage est un entier numérique"
