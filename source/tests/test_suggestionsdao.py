import pytest
from source.DAO.SuggestionsDAO import SuggestionsDAO


def test_create_suggestion():
    mes_suggestions = SuggestionsDAO()

    # Tester avec des paramètres valides
    mes_suggestions.create_suggestion(id_eleve=1, id_stage=42, id_professeur=45)

    # Tester avec un id_élève invalide
    with pytest.raises(TypeError) as exc_info:
        mes_suggestions.create_suggestion(
            id_eleve="pas_un_entier", id_stage=42, id_professeur=45
        )
    assert str(exc_info.value) == "l'identifiant de l'élève est un entier numérique"

    # Tester avec un id_stage invalide
    with pytest.raises(TypeError) as exc_info:
        mes_suggestions.create_suggestion(
            id_eleve=1, id_stage="pas_un_entier", id_professeur=45
        )
    assert str(exc_info.value) == "l'identifiant du stage est un entier numérique"

    # Tester avec un id_professeur invalide
    with pytest.raises(TypeError) as exc_info:
        mes_suggestions.create_suggestion(id_eleve=1, id_stage=42, id_professeur=[45])
    assert str(exc_info.value) == "l'identifiant du professeur est un entier numérique"


def test_get_suggestions_by_id():
    mes_suggestions = SuggestionsDAO()

    # Tester avec des paramètres valides
    suggestions = mes_suggestions.get_suggestions_by_id(id_eleve=1)
    assert isinstance(suggestions, list)
    assert all(isinstance(suggestion, dict) for suggestion in suggestions)

    # Tester avec un id_utilisateur invalide
    with pytest.raises(TypeError) as exc_info:
        mes_suggestions.get_suggestions_by_id(id_eleve="pas_un_entier")
    assert (
        str(exc_info.value) == "l'identifiant de l'élève est un entier numérique"
    )


def test_delete_suggestion():
    mes_suggestions = SuggestionsDAO()

    # Tester avec des paramètres valides
    mes_suggestions.delete_suggestion(id_eleve=1, id_stage=42)

    # Tester avec un id_eleveinvalide
    with pytest.raises(TypeError) as exc_info:
        mes_suggestions.delete_suggestion(id_eleve="pas_un_entier", id_stage=50)
    assert (
        str(exc_info.value) == "l'identifiant de l'élève est un entier numérique"
    )

    # Tester avec un id_stage invalide
    with pytest.raises(TypeError) as exc_info:
        mes_suggestions.delete_suggestion(id_eleve=1, id_stage="pas_un_entier")
    assert str(exc_info.value) == "l'identifiant du stage est un entier numérique"
