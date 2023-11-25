-- DROP SCHEMA base_projetinfo;

CREATE SCHEMA base_projetinfo AUTHORIZATION id2225;

-- DROP SEQUENCE base_projetinfo.sequence_stage;

CREATE SEQUENCE base_projetinfo.sequence_stage
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 3000
	START 400;
-- DROP SEQUENCE base_projetinfo.sequence_utilisateur;

CREATE SEQUENCE base_projetinfo.sequence_utilisateur
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 300
	START 1;-- base_projetinfo.administrateur definition

-- Drop table

-- DROP TABLE base_projetinfo.administrateur;

CREATE TABLE base_projetinfo.administrateur (
	id_admin varchar(25) NOT NULL,
	mot_de_passe varchar(25) NULL,
	CONSTRAINT administrateur_pkey PRIMARY KEY (id_admin)
);


-- base_projetinfo.entreprise definition

-- Drop table

-- DROP TABLE base_projetinfo.entreprise;

CREATE TABLE base_projetinfo.entreprise (
	id_ent int4 NOT NULL,
	denomination varchar(50) NULL,
	ville varchar(30) NULL,
	region varchar(30) NULL,
	pays varchar(30) NULL,
	email_ent varchar(70) NULL,
	domaine varchar(402) NULL,
	CONSTRAINT entreprise_pkey PRIMARY KEY (id_ent)
);


-- base_projetinfo.recherche definition

-- Drop table

-- DROP TABLE base_projetinfo.recherche;

CREATE TABLE base_projetinfo.recherche (
	id_recherche int4 NOT NULL,
	domaine varchar(800) NULL,
	ville varchar(50) NULL,
	entreprise varchar(50) NULL,
	CONSTRAINT recherche_pkey PRIMARY KEY (id_recherche)
);


-- base_projetinfo.stage definition

-- Drop table

-- DROP TABLE base_projetinfo.stage;

CREATE TABLE base_projetinfo.stage (
	id_stage int4 NOT NULL DEFAULT nextval('base_projetinfo.sequence_stage'::regclass),
	titre varchar(800) NULL,
	lien varchar(800) NULL,
	domaine varchar(800) NULL,
	date_publication varchar NULL,
	salaire varchar NULL,
	periode varchar NULL,
	niveau_etudes varchar NULL,
	entreprise varchar NULL,
	lieu varchar NULL,
	CONSTRAINT stage_pkey PRIMARY KEY (id_stage)
);


-- base_projetinfo.utilisateur definition

-- Drop table

-- DROP TABLE base_projetinfo.utilisateur;

CREATE TABLE base_projetinfo.utilisateur (
	id_utilisateur int4 NOT NULL DEFAULT nextval('base_projetinfo.sequence_utilisateur'::regclass),
	pseudo varchar(25) NULL,
	nom varchar(25) NULL,
	prenom varchar(25) NULL,
	mot_de_passe varchar(25) NULL,
	type_utilisateur varchar(25) NULL,
	CONSTRAINT check_longueur_mot_de_passe CHECK ((length((mot_de_passe)::text) >= 8)),
	CONSTRAINT unique_pseudo UNIQUE (pseudo),
	CONSTRAINT utilisateur_pkey PRIMARY KEY (id_utilisateur)
);


-- base_projetinfo.historique definition

-- Drop table

-- DROP TABLE base_projetinfo.historique;

CREATE TABLE base_projetinfo.historique (
	id_stage int4 NOT NULL,
	id_utilisateur int4 NOT NULL,
	CONSTRAINT fk_historique_id_stage FOREIGN KEY (id_stage) REFERENCES base_projetinfo.stage(id_stage),
	CONSTRAINT fk_historique_id_utilisateur FOREIGN KEY (id_utilisateur) REFERENCES base_projetinfo.utilisateur(id_utilisateur)
);


-- base_projetinfo.liste_eleves definition

-- Drop table

-- DROP TABLE base_projetinfo.liste_eleves;

CREATE TABLE base_projetinfo.liste_eleves (
	id_eleve int4 NULL,
	id_professeur int4 NULL,
	nom varchar NULL,
	prenom varchar NULL,
	CONSTRAINT fk_liste_eleves FOREIGN KEY (id_eleve) REFERENCES base_projetinfo.utilisateur(id_utilisateur),
	CONSTRAINT fk_liste_eleves2 FOREIGN KEY (id_professeur) REFERENCES base_projetinfo.utilisateur(id_utilisateur)
);


-- base_projetinfo.liste_envie definition

-- Drop table

-- DROP TABLE base_projetinfo.liste_envie;

CREATE TABLE base_projetinfo.liste_envie (
	id_eleve int4 NOT NULL,
	id_stage int4 NOT NULL,
	CONSTRAINT liste_envie_pkey PRIMARY KEY (id_eleve, id_stage),
	CONSTRAINT fk_voeux_id_stage FOREIGN KEY (id_stage) REFERENCES base_projetinfo.stage(id_stage),
	CONSTRAINT fk_voeux_id_utilisateur FOREIGN KEY (id_eleve) REFERENCES base_projetinfo.utilisateur(id_utilisateur)
);


-- base_projetinfo.suggestion definition

-- Drop table

-- DROP TABLE base_projetinfo.suggestion;

CREATE TABLE base_projetinfo.suggestion (
	id_eleve int4 NOT NULL,
	id_stage int4 NOT NULL,
	id_professeur int4 NOT NULL,
	CONSTRAINT suggestion_pkey PRIMARY KEY (id_eleve, id_stage, id_professeur),
	CONSTRAINT fk_suggestion_id_stage FOREIGN KEY (id_stage) REFERENCES base_projetinfo.stage(id_stage),
	CONSTRAINT fk_suggestion_id_utilisateur FOREIGN KEY (id_eleve) REFERENCES base_projetinfo.utilisateur(id_utilisateur),
	CONSTRAINT fk_suggestion_id_utilisateur2 FOREIGN KEY (id_professeur) REFERENCES base_projetinfo.utilisateur(id_utilisateur)
);
