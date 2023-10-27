import pytest
from source.DAO.StageDAO import StageDAO
from source.business_object.stage_recherche.stage import Stage


def test_create_stage():
    mes_stages = StageDAO()

    nouveau_stage = Stage(
        titre="Stage en développement web",
        lien="https://www.example.com/stage",
        domaine="Développement web",
        modalites="À distance",
        date_publication="2023-10-30",
        date_debut="2023-11-15",
        date_fin="2023-12-15",
        entreprise="Web Solutions Inc.",
    )

    stage_cree = mes_stages.create_stage(nouveau_stage)

    assert stage_cree.id is not None
    assert isinstance(stage_cree.id, int)


def test_find_stage_by_id():
    mes_stages = StageDAO()

    # Tester avec des paramètres valides
    stage = mes_stages.find_stage_by_id(id_stage=87)
    assert isinstance(stage, dict)

    # Tester avec un id_stage invalide
    with pytest.raises(TypeError) as exc_info:
        mes_stages.find_stage_by_id(id_stage="pas_un_entier")
    assert str(exc_info.value) == "l'identifiant du stage est un entier numérique"
