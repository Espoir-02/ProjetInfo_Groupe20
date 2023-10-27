import pytest
import re
from source.DAO.HistoriqueDAO import HistoriqueDAO



@pytest.mark.parametrize(
    "params, erreur, message_erreur",
    [
        (
            {"id_historique": [4]},
            TypeError,
            "l'identifiant de l'historique est un entier numérique'",
        ),
    ],
)
def test_get_all_historique_by_id_parametres(params, erreur, message_erreur):
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        get_all_historique_by_id(**params)


def test_get_all_historiqye_by_id():
    mon_historique= HistoriqueDAO()

    # Tester avec des paramètres valides
    mon_historique.update_liste_envie(id_utilisateur=1, id_stage=42)

    # Tester avec un id_utilisateur invalide
    with pytest.raises(TypeError) as exc_info:
        mon_historique.get_all_historique_by_id(id_utilisateur="pas_un_entier", id_stage=42)
    assert str(exc_info.value) == "l'identifiant de l'utilisateur est un entier numérique"





def test_update__historique():
    mon_historique = HistoriqueDAO()

    # Tester avec des paramètres valides
    mon_historique.update_historique(id_utilisateur=1, id_stage=42)

    # Tester avec un id_utilisateur invalide
    with pytest.raises(TypeError) as exc_info:
        mon_historique.update_historique(id_utilisateur="pas_un_entier", id_stage=42)
    assert str(exc_info.value) == "l'identifiant de l'utilisateur est un entier numérique"

    # Tester avec un id_stage invalide
    with pytest.raises(TypeError) as exc_info:
        mon_historique.update_historique(id_utilisateur=1, id_stage="pas_un_entier")
    assert str(exc_info.value) == "l'identifiant du stage est un entier numérique"