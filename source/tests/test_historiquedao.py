import pytest
import re
from HistoriqueDAO import update_historique
from HistoriqueDAO import get_all_historique_by_id


@pytest.mark.parametrize(
    "params, erreur, message_erreur",
    [
        (
            {"id_historique": [4]},
            TypeError,
            "les arguments doivent être des instances int",
        ),
    ],
)
def test_get_all_historique_by_id_parametres(params, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        get_all_historique_by_id(**params)


@pytest.mark.parametrize(
    "params, erreur, message_erreur",
    [
        (
            {
                "id_utilisateur": 2,
                "id_stage": "Stage2",
            },
            TypeError,
            "l'identifiant du stage est une valeur numérique",
        ),
        (
            {"id_utilisateur": 0.45, "id_stage": 45,
            },
            TypeError,
            "les arguments doivent être des instances int",
        ),
    ],
)
def test_update_historique_parametres(params, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        update_historique(**params)
