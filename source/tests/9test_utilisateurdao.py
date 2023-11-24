import pytest
from source.DAO.utilisateur_dao import UtilisateurDAO
from source.business_object.utilisateur.utilisateur2 import Utilisateur
from source.exception.exceptions import (
    IdUtilisateurInexistantError,
    PseudoDejaExistantError,
)


def test_create_compte():
    mes_utilisateurs = UtilisateurDAO()

    # Création d'un objet Utilisateur
    nouvel_utilisateur = Utilisateur(
        nom="Fleur",
        prenom="Amaryllis",
        pseudo="Chercheurdestage",
        mot_de_passe="secret",
        type_utilisateur="eleve",
    )

    # Appel de la méthode create_compte
    utilisateur_cree = mes_utilisateurs.create_compte(nouvel_utilisateur)

    # Vérification que l'utilisateur créé a un ID attribué
    assert utilisateur_cree.id is not None
    assert isinstance(utilisateur_cree.id, int)


def test_find_id_by_pseudo():
    mes_utilisateurs = UtilisateurDAO()

    # Tester avec des paramètres valides
    id = mes_utilisateurs.find_id_by_pseudo(pseudo="Chercheurdestage")
    assert isinstance(id, int)

    # Tester avec un pseudo invalide
    with pytest.raises(TypeError) as exc_info:
        mes_utilisateurs.find_id_by_pseudo(pseudo=[85])
    assert (
        str(exc_info.value) == "le pseudo de l'utilisateur est une chaîne de caractères"
    )


def test_find_mdp():
    mes_utilisateurs = UtilisateurDAO()

    # Tester avec des paramètres valides
    mdp = mes_utilisateurs.find_mdp(pseudo="Chercheurdestage")
    assert isinstance(mdp, str)

    # Tester avec un pseudo invalide
    with pytest.raises(TypeError) as exc_info:
        mes_utilisateurs.find_mdp(pseudo=[85])
    assert (
        str(exc_info.value) == "le pseudo de l'utilisateur est une chaîne de caractères"
    )


def test_find_by_nom():
    mes_utilisateurs = UtilisateurDAO()

    # Tester avec des paramètres valides
    utilisateur = mes_utilisateurs.find_by_nom(nom="Fleur", prenom="Amaryllis")
    assert isinstance(utilisateur, dict)

    # Tester avec un nom invalide
    with pytest.raises(TypeError) as exc_info:
        mes_utilisateurs.find_by_nom(nom=59, prenom="Amaryllis")
    assert str(exc_info.value) == "le nom de l'utilisateur est une chaîne de caractères"

    # Tester avec un prénom invalide
    with pytest.raises(TypeError) as exc_info:
        mes_utilisateurs.find_by_nom(nom="Fleur", prenom=["Amaryllis"])
    assert (
        str(exc_info.value) == "le prénom de l'utilisateur est une chaîne de caractères"
    )


def test_find_by_id():
    mes_utilisateurs = UtilisateurDAO()

    # Tester avec des paramètres valides
    utilisateur = mes_utilisateurs.find_by_id(id_utilisateur=6)
    assert isinstance(utilisateur, dict)

    # Tester avec un id_utilisateur invalide
    with pytest.raises(TypeError) as exc_info:
        mes_utilisateurs.find_by_id(id_utilisateur="pas_un_entier")
    assert (
        str(exc_info.value) == "l'identifiant de l'utilisateur est un entier numérique"
    )

    # Tester avec un id_utilisateur qui n'existe pas
    with pytest.raises(IdUtilisateurInexistantError) as exc_info:
        mes_utilisateurs.find_by_id(id_utilisateur=999)
    assert str(exc_info.value) == "L'utilisateur avec l'ID 999 n'existe pas."


def test_update_utilisateur_mdp(self):
    mes_utilisateurs = UtilisateurDAO()

    # Test avec des paramètres valides
    pseudo_valide = "Milliris"
    ancien_mdp = mes_utilisateurs.find_mdp(pseudo_valide)
    nouveau_mdp_valide = "MotDePasse456"
    mes_utilisateurs.update_utilisateur_mdp(pseudo_valide, nouveau_mdp_valide)
    mdp_maj = mes_utilisateurs.find_mdp(pseudo_valide)
    assert mdp_maj == nouveau_mdp_valide
    assert mdp_maj != ancien_mdp

    # Test avec un pseudo invalide (type incorrect)
    with pytest.raises(TypeError) as exc_info:
        pseudo_invalide = 123
        nouveau_mdp_invalide = "MotDePasse789"
        mes_utilisateurs.update_utilisateur_mdp(pseudo_invalide, nouveau_mdp_invalide)
    assert (
        str(exc_info.value)
        == "Le pseudo de l'utilisateur doit être une chaîne de caractères"
    )

    # Test avec un nouveau mot de passe trop court
    with pytest.raises(ValueError) as exc_info:
        nouveau_mdp_trop_court = "Pass123"
        mes_utilisateurs.update_utilisateur_mdp(pseudo_valide, nouveau_mdp_trop_court)
    assert (
        str(exc_info.value)
        == "Le nouveau mot de passe doit contenir plus de 8 caractères"
    )

    # Test avec un pseudo inexistant
    with pytest.raises(Exception) as exc_info:
        pseudo_inexistant = "Inexistant"
        mes_utilisateurs.update_utilisateur_mdp(pseudo_inexistant, nouveau_mdp_valide)
    assert "Le pseudo n'existe pas" in str(exc_info.value)


def test_update_utilisateur_pseudo(self):
    mes_utilisateurs = UtilisateurDAO()
    id_utilisateur = 18
    ancien_pseudo = mes_utilisateurs.find_by_id(id_utilisateur).pseudo

    # Test de la mise à jour avec des paramètres valides
    nouveau_pseudo = "Chasseurdestage"
    mes_utilisateurs.update_utilisateur_pseudo(id_utilisateur, nouveau_pseudo)
    utilisateur_maj = mes_utilisateurs.find_by_id(id_utilisateur)

    assert utilisateur_maj.pseudo == nouveau_pseudo
    assert utilisateur_maj.pseudo != ancien_pseudo

    # Tester avec un id_utilisateur invalide
    with pytest.raises(TypeError) as exc_info:
        mes_utilisateurs.update_utilisateur_pseudo(
            id_utilisateur="pas_un_entier", nouveau_pseudo=nouveau_pseudo
        )
    assert (
        str(exc_info.value) == "l'identifiant de l'utilisateur est un entier numérique"
    )

    # Tester avec un id_utilisateur qui n'existe pas
    with pytest.raises(PseudoDejaExistantError) as exc_info:
        mes_utilisateurs.update_utilisateur_pseudo(id_utilisateur, "Milliris")
    assert str(exc_info.value) == "Le pseudo Milliris existe déjà."


def test_delete_utilisateur():
    mes_utilisateurs = UtilisateurDAO()

    # Tester avec des paramètres valides
    mes_utilisateurs.delete_utilisateur(id_utilisateur=30)

    # Tester avec un id_utilisateur invalide
    with pytest.raises(TypeError) as exc_info:
        mes_utilisateurs.delete_utilisateur(id_utilisateur="pas_un_entier")
    assert (
        str(exc_info.value) == "l'identifiant de l'utilisateur est un entier numérique"
    )
