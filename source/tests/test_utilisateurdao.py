import pytest
from source.DAO.UtilisateurDAO import UtilisateurDAO


def test_find_mdp():
    mes_utilisateurs = UtilisateurDAO()

    # Tester avec des paramètres valides
    mdp = mes_utilisateurs.delete_utilisateur(pseudo='Chercheurdestage')
    assert isinstance(mdp, str)

    # Tester avec un pseudo invalide
    with pytest.raises(TypeError) as exc_info:
        mes_utilisateurs.find_mp(pseudo=[85])
    assert str(exc_info.value) == "le pseudo de l'utilisateur est une chaîne de caractères"


def test_find_by_nom():
    mes_utilisateurs = UtilisateurDAO()

    # Tester avec des paramètres valides
    utilisateur = mes_utilisateurs.find_by_nom(nom='Fleur', prenom='Amaryllis')
    assert isinstance(utilisateur, dict)

    # Tester avec un nom invalide
    with pytest.raises(TypeError) as exc_info:
        mes_utilisateurs.find_by_nom(nom=59, prenom='Amaryllis')
    assert str(exc_info.value) == "le nom de l'utilisateur est une chaîne de caractères"

    # Tester avec un prénom invalide
    with pytest.raises(TypeError) as exc_info:
        mes_utilisateurs.find_by_nom(nom='Fleur', prenom=['Amaryllis'])
    assert str(exc_info.value) == "le prénom de l'utilisateur est une chaîne de caractères"

def test_find_by_id():
    mes_utilisateurs = UtilisateurDAO()

    # Tester avec des paramètres valides
    utilisateur = mes_utilisateurs.find_by_id(id_utilisateur=1)
    assert isinstance(utilisateur, dict)

    # Tester avec un id_utilisateur invalide
    with pytest.raises(TypeError) as exc_info:
        mes_utilisateurs.find_by_id(id_utilisateur="pas_un_entier")
    assert str(exc_info.value) == "l'identifiant de l'utilisateur est un entier numérique"


def test_delete_utilisateur():
    mes_utilisateurs = UtilisateurDAO()

    # Tester avec des paramètres valides
    mes_utilisateurs.delete_utilisateur(id_utilisateur=1)

    # Tester avec un id_utilisateur invalide
    with pytest.raises(TypeError) as exc_info:
        mes_utilisateurs.delete_utilisateur(id_utilisateur="pas_un_entier")
    assert str(exc_info.value) == "l'identifiant de l'utilisateur est un entier numérique"