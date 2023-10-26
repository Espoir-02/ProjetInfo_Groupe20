DROP SCHEMA IF EXISTS base_ProjetInfo;
CREATE SCHEMA base_ProjetInfo;

DROP TABLE IF EXISTS base_ProjetInfo.utilisateur;
CREATE TABLE base_ProjetInfo.utilisateur (
    id_utilisateur INT,
    pseudo VARCHAR(25),
    nom VARCHAR(25),
    prenom VARCHAR(25),
    mot_de_passe VARCHAR(25),
    type_utilisateur VARCHAR(25),
      PRIMARY KEY (id_utilisateur)

);



DROP TABLE IF EXISTS base_ProjetInfo.administrateur;
CREATE TABLE base_ProjetInfo.Administrateur(
        id_admin     Varchar (25),
        mot_de_passe     Varchar (25),
        PRIMARY KEY (id_admin)
);



DROP TABLE IF EXISTS base_ProjetInfo.stage;
CREATE TABLE base_ProjetInfo.stage(
        id_stage     Int,
        titre     Varchar (70),
        lien     Varchar (500),
        domaine     Varchar (50),
        modalites     Varchar (50),
        date_publication     Date ,
        salaire     Int,
        date_debut     Date,
        date_fin     Date,
        id_ent     Int,
        PRIMARY KEY (id_stage)
);



DROP TABLE IF EXISTS base_ProjetInfo.entreprise;
CREATE TABLE base_ProjetInfo.entreprise(
        id_ent     Int,
        denomination     Varchar (50),
        ville     Varchar (30),
        region     Varchar (30),
        pays     Varchar (30),
        email_ent     Varchar (70),
        domaine     Varchar (402),
        PRIMARY KEY (id_ent)
);




DROP TABLE IF EXISTS base_ProjetInfo.recherche;
CREATE TABLE base_ProjetInfo.recherche(
        id_recherche     Int,
        domaine     Varchar (50),
        ville     Varchar (50),
        entreprise     Varchar (50),
        PRIMARY KEY (id_recherche)
);



DROP TABLE IF EXISTS base_ProjetInfo.historique;
CREATE TABLE base_ProjetInfo.historique(
        id_historique     Int,
        id_stage     Int,
        id_utilisateur     Int,
        PRIMARY KEY (id_historique)
);



DROP TABLE IF EXISTS base_ProjetInfo.voeux;
CREATE TABLE base_ProjetInfo.voeux(
        id_voeux     Int,
        id_eleve     Int ,
        id_stage     Int,
        PRIMARY KEY (id_voeux)
);



DROP TABLE IF EXISTS base_ProjetInfo.suggestion;
CREATE TABLE base_ProjetInfo.suggestion(
        id_suggestion     Int,
        id_eleve     Int,
        id_stage     Int,
        id_professeur    Int,
        PRIMARY KEY (id_suggestion)
);

DROP TABLE IF EXISTS base_ProjetInfo.liste_eleves;
CREATE TABLE base_ProjetInfo.liste_eleves(
        id_eleve     Int,
        id_professeur     Int
);



ALTER TABLE base_ProjetInfo.stage ADD CONSTRAINT FK_stage_id_ent FOREIGN KEY (id_ent) REFERENCES base_ProjetInfo.entreprise(id_ent)

ALTER TABLE base_ProjetInfo.historique  ADD CONSTRAINT FK_Historique_id_stage FOREIGN KEY (id_stage) REFERENCES base_ProjetInfo.stage(id_stage)
ALTER TABLE base_ProjetInfo.historique  ADD CONSTRAINT FK_Historique_id_utilisateur FOREIGN KEY (id_utilisateur) REFERENCES base_ProjetInfo.utilisateur(id_utilisateur)

ALTER TABLE base_ProjetInfo.voeux ADD CONSTRAINT FK_voeux_id_utilisateur FOREIGN KEY (id_eleve) REFERENCES base_ProjetInfo.utilisateur(id_utilisateur)
ALTER TABLE base_ProjetInfo.voeux ADD CONSTRAINT FK_voeux_id_stage FOREIGN KEY (id_stage) REFERENCES base_ProjetInfo.stage(id_stage)

ALTER TABLE base_ProjetInfo.suggestion ADD CONSTRAINT FK_suggestion_id_stage FOREIGN KEY (id_stage) REFERENCES base_ProjetInfo.stage(id_stage)
ALTER TABLE base_ProjetInfo.suggestion ADD CONSTRAINT FK_suggestion_id_utilisateur FOREIGN KEY (id_eleve) REFERENCES base_ProjetInfo.utilisateur(id_utilisateur)
ALTER TABLE base_ProjetInfo.suggestion ADD CONSTRAINT FK_suggestion_id_utilisateur2 FOREIGN KEY (id_professeur) REFERENCES base_ProjetInfo.utilisateur(id_utilisateur)


ALTER TABLE base_ProjetInfo.liste_eleves ADD CONSTRAINT FK_Liste_eleves FOREIGN KEY (id_eleve) REFERENCES base_ProjetInfo.utilisateur(id_utilisateur)
ALTER TABLE base_ProjetInfo.liste_eleves ADD CONSTRAINT FK_Liste_eleves2 FOREIGN KEY (id_professeur) REFERENCES base_ProjetInfo.utilisateur(id_utilisateur);