import pytest
from source.DAO.SuggestionsDAO import SuggestionsDAO
from source.exception.exceptions import IdEleveInexistantError
from source.exception.exceptions import IdProfesseurInexistantError
from source.exception.exceptions import IdStageInexistantError


def test_create_suggestion():
    mes_suggestions = SuggestionsDAO()

    # Tester avec des paramètres valides
    mes_suggestions.create_suggestion(id_eleve=8, id_stage=406, id_professeur=10)

    # Tester avec un id_élève invalide
    with pytest.raises(TypeError) as exc_info:
        mes_suggestions.create_suggestion(
            id_eleve="pas_un_entier", id_stage=406, id_professeur=10
        )
    assert str(exc_info.value) == "l'identifiant de l'élève est un entier numérique"

    # Tester avec un id_stage invalide
    with pytest.raises(TypeError) as exc_info:
        mes_suggestions.create_suggestion(
            id_eleve=8, id_stage="pas_un_entier", id_professeur=10
        )
    assert str(exc_info.value) == "l'identifiant du stage est un entier numérique"

    # Tester avec un id_professeur invalide
    with pytest.raises(TypeError) as exc_info:
        mes_suggestions.create_suggestion(id_eleve=1, id_stage=42, id_professeur=[45])
    assert str(exc_info.value) == "l'identifiant du professeur est un entier numérique"

    # Tester avec un id_eleve qui n'existe pas
    with pytest.raises(IdEleveInexistantError) as exc_info:
        mes_suggestions.create_suggestion(id_eleve=999, id_stage=406, id_professeur=10)
    assert str(exc_info.value) == "L'élève avec l'ID 999 n'existe pas."

    # Tester avec un id_professeur qui n'existe pas
    with pytest.raises(IdProfesseurInexistantError) as exc_info:
        mes_suggestions.create_suggestion(id_eleve=8, id_stage=406, id_professeur=999)
    assert str(exc_info.value) == "Le professeur avec l'ID 999 n'existe pas."

    # Tester avec un id_stage qui n'existe pas
    with pytest.raises(IdStageInexistantError) as exc_info:
        mes_suggestions.create_suggestion(id_eleve=8, id_stage=88888, id_professeur=10)
    assert str(exc_info.value) == "Le stage avec l'ID 88888 n'existe pas."


def test_get_suggestions_by_id():
    mes_suggestions = SuggestionsDAO()

    # Tester avec des paramètres valides
    suggestions = mes_suggestions.get_suggestions_by_id(id_eleve=8)
    assert isinstance(suggestions, list)
    assert all(isinstance(suggestion, dict) for suggestion in suggestions)

    # Tester avec un id_eleve invalide
    with pytest.raises(TypeError) as exc_info:
        mes_suggestions.get_suggestions_by_id(id_eleve="pas_un_entier")
    assert str(exc_info.value) == "l'identifiant de l'élève est un entier numérique"

    # Tester avec un id_eleve qui n'existe pas
    with pytest.raises(IdEleveInexistantError) as exc_info:
        mes_suggestions.get_suggestions_by_id(id_eleve=999)
    assert str(exc_info.value) == "L'élève avec l'ID 999 n'existe pas."


def test_delete_suggestion():
    mes_suggestions = SuggestionsDAO()

    # Tester avec des paramètres valides
    mes_suggestions.delete_suggestion(id_eleve=8, id_stage=406)

    # Tester avec un id_eleve invalide
    with pytest.raises(TypeError) as exc_info:
        mes_suggestions.delete_suggestion(id_eleve="pas_un_entier", id_stage=50)
    assert str(exc_info.value) == "l'identifiant de l'élève est un entier numérique"

    # Tester avec un id_stage invalide
    with pytest.raises(TypeError) as exc_info:
        mes_suggestions.delete_suggestion(id_eleve=1, id_stage="pas_un_entier")
    assert str(exc_info.value) == "l'identifiant du stage est un entier numérique"

    # Tester avec un id_eleve qui n'existe pas
    with pytest.raises(IdEleveInexistantError) as exc_info:
        mes_suggestions.delete_suggestion(id_eleve=999, id_stage=406)
    assert str(exc_info.value) == "L'élève avec l'ID 999 n'existe pas."

    # Tester avec un id_stage qui n'existe pas
    with pytest.raises(IdStageInexistantError) as exc_info:
        mes_suggestions.delete_suggestion(id_eleve=8, id_stage=88888)
    assert str(exc_info.value) == "Le stage avec l'ID 88888 n'existe pas."


    def test_delete_all_suggestions(self):
        mes_suggestions = SuggestionsDAO()

        # Test avec des paramètres valides
        id_eleve_valide = 123
        mes_suggestions.delete_all_suggestions(id_eleve_valide)

        # Test avec un id_eleve invalide 
        with pytest.raises(TypeError) as exc_info:
            id_eleve_invalide = "pas_un_entier"
            mes_suggestions.delete_all_suggestions(id_eleve_invalide)
        assert str(exc_info.value) == "L'identifiant de l'élève doit être un entier numérique"

        # Test avec un id_eleve inexistant
        with pytest.raises(IdEleveInexistantError) as exc_info:
            id_eleve_inexistant = 9999
            mes_suggestions.delete_all_suggestions(id_eleve_inexistant)
        assert str(exc_info.value) == "L'élève avec l'identifiant '9999' n'existe pas"