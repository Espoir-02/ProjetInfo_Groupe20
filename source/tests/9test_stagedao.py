import pytest
from source.DAO.StageDAO import StageDAO
from source.business_object.stage_recherche.stage import Stage
from source.exception.exceptions import IdStageInexistantError


def test_create_stage():
    mes_stages = StageDAO()

    nouveau_stage = Stage(
        titre="Arroseur de cactus",
        lien="https://www.cactus.com/stage",
        domaine="Jardinerie",
        salaire="SMIC",
        date_publication="2023-10-30",
        periode="1 mois",
        niveau_etudes="L3",
        entreprise="CactusGibus",
    )

    stage_cree = mes_stages.create_stage(nouveau_stage)

    assert stage_cree.id is not None
    assert isinstance(stage_cree.id, int)


def test_find_stage_by_id():
    mes_stages = StageDAO()

    # Tester avec des paramètres valides
    stage = mes_stages.find_stage_by_id(id_stage=403)
    assert isinstance(stage, dict)

    # Tester avec un id_stage invalide
    with pytest.raises(TypeError) as exc_info:
        mes_stages.find_stage_by_id(id_stage="pas_un_entier")
    assert str(exc_info.value) == "l'identifiant du stage est un entier numérique"

    # Tester avec un id_stage qui n'existe pas
    with pytest.raises(IdStageInexistantError) as exc_info:
        mes_stages.find_stage_by_id(id_stage=88888)
    assert str(exc_info.value) == "Le stage avec l'ID 88888 n'existe pas."
