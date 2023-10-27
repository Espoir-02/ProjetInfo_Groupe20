import pytest
from source.DAO.StageDAO import StageDAO


def test_find_stage_by_id():
    mes_stages = StageDAO()

    # Tester avec des paramètres valides
    stage = mes_stages.find_stage_by_id( id_stage=87)
    assert isinstance(stage, dict)

    # Tester avec un id_stage invalide
    with pytest.raises(TypeError) as exc_info:
        mes_stages.find_stage_by_id( id_stage="pas_un_entier")
    assert str(exc_info.value) == "l'identifiant du stage est un entier numérique"