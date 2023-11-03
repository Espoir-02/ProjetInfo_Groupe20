import pytest
from source.DAO.HistoriqueDAO import HistoriqueDAO
from source.exception.exceptions import IdUtilisateurInexistantError
from source.exception.exceptions import IdStageInexistantError


def test_get_all_historique_by_id():
    mon_historique = HistoriqueDAO()

    # Tester avec des paramètres valides
    historique = mon_historique.get_all_historique_by_id(id_utilisateur=8)
    assert isinstance(historique, list)
    assert all(isinstance(recherche, dict) for recherche in historique)

    # Tester avec un id_utilisateur invalide
    with pytest.raises(TypeError) as exc_info:
        mon_historique.get_all_historique_by_id(id_utilisateur="pas_un_entier")
    assert (
        str(exc_info.value) == "l'identifiant de l'utilisateur est un entier numérique"
    )

    # Tester avec un id_utilisateur qui n'existe pas
    with pytest.raises(IdUtilisateurInexistantError) as exc_info:
        mon_historique.get_all_historique_by_id(id_utilisateur=999)
    assert str(exc_info.value) == "L'utilisateur avec l'ID 999 n'existe pas."


def test_update_historique():
    mon_historique = HistoriqueDAO()

    # Tester avec des paramètres valides
    mon_historique.update_historique(id_utilisateur=8, id_stage=404)

    # Tester avec un id_utilisateur invalide
    with pytest.raises(TypeError) as exc_info:
        mon_historique.update_historique(id_utilisateur="pas_un_entier", id_stage=403)
    assert (
        str(exc_info.value) == "l'identifiant de l'utilisateur est un entier numérique"
    )

    # Tester avec un id_stage invalide
    with pytest.raises(TypeError) as exc_info:
        mon_historique.update_historique(id_utilisateur=9, id_stage="pas_un_entier")
    assert str(exc_info.value) == "l'identifiant du stage est un entier numérique"

    # Tester avec un id_utilisateur qui n'existe pas
    with pytest.raises(IdUtilisateurInexistantError) as exc_info:
        mon_historique.update_historique(id_utilisateur=999, id_stage=404)
    assert str(exc_info.value) == "L'utilisateur avec l'ID 999 n'existe pas."

    # Tester avec un id_stage qui n'existe pas
    with pytest.raises(IdStageInexistantError) as exc_info:
        mon_historique.update_historique(id_utilisateur=8, id_stage=88888)
    assert str(exc_info.value) == "Le stage avec l'ID 88888 n'existe pas."
