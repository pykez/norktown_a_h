-- Inicialização das tabelas de banco.

-- Criar tabela de cidadãos de Norktown
CREATE TABLE IF NOT EXISTS tbcitizen (
    ctzid SERIAL,
    ctzname VARCHAR(20) NOT NULL,
    ctzcpf VARCHAR(11) NOT NULL,
    ctzaddress VARCHAR(100)
);

-- Adicionar constraint de PK.
ALTER TABLE tbcitizen DROP CONSTRAINT IF EXISTS pk_tbcitizen;
ALTER TABLE tbcitizen ADD CONSTRAINT pk_tbcitizen PRIMARY KEY (ctzid);

-- Adicionar constraint unique do CPF.
ALTER TABLE tbcitizen DROP CONSTRAINT IF EXISTS unique_ctzcpf;
ALTER TABLE tbcitizen ADD CONSTRAINT unique_ctzcpf UNIQUE (ctzcpf);

-- Criar tabela de veículos
CREATE TABLE IF NOT EXISTS tbvehicle (
    vclid SERIAL,
    ctzid INTEGER,
    vclplate CHAR(7),
    vclmodel SMALLINT NOT NULL,
    vclcolor SMALLINT NOT NULL    
);

-- Adiciona constraint de PK.
ALTER TABLE tbvehicle DROP CONSTRAINT IF EXISTS pk_tbvehicle;
ALTER TABLE tbvehicle ADD CONSTRAINT pk_tbvehicle PRIMARY KEY (vclid);

-- Adiciona constraint de FK.
ALTER TABLE tbvehicle DROP CONSTRAINT IF EXISTS fk_tbvehicle_tbcitizen;
ALTER TABLE tbvehicle ADD CONSTRAINT fk_tbvehicle_tbcitizen FOREIGN KEY (ctzid) REFERENCES tbcitizen;

-- Adiciona constraint unique da placa.
ALTER TABLE tbvehicle DROP CONSTRAINT IF EXISTS unique_vclplate;
ALTER TABLE tbvehicle ADD CONSTRAINT unique_vclplate UNIQUE (vclplate);

-- Adiciona constraint para manter o campo de modelo com valores válidos (1-hatch, 2-sedan, 3-convertible).
ALTER TABLE tbvehicle DROP CONSTRAINT IF EXISTS check_vclmodel;
ALTER TABLE tbvehicle ADD CONSTRAINT check_vclmodel CHECK (vclmodel IN (1, 2, 3));

-- Adiciona constraint para manter o campo de cor com valores válidos (1-yellow, 2-blue, 3-gray).
ALTER TABLE tbvehicle DROP CONSTRAINT IF EXISTS check_vclcolor;
ALTER TABLE tbvehicle ADD CONSTRAINT check_vclcolor CHECK (vclcolor IN (1, 2, 3));

-- Trigger para que não seja possível existir mais de três carros para um mesmo cidadão.
-- Trigger é disparada após inserção de registro de veículo.
CREATE OR REPLACE FUNCTION fn_check_vehicle_per_citizen()
  RETURNS trigger AS
$$
BEGIN
    IF ((SELECT count(*) FROM tbvehicle WHERE ctzid = NEW.ctzid) >= 3) THEN RETURN NULL;
    END IF;
    RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';
CREATE TRIGGER trigger_check_vehicle_per_citizen 
    BEFORE INSERT ON "tbvehicle"
    FOR EACH ROW EXECUTE PROCEDURE fn_check_vehicle_per_citizen();


-- Tuplas iniciais:
INSERT INTO tbcitizen (ctzname, ctzcpf, ctzaddress) VALUES ('Alberto Carlos', '05195702942', 'Rua Cisjordania Bairro Jardim');
INSERT INTO tbcitizen (ctzname, ctzcpf, ctzaddress) VALUES ('Giancarlo Pandini', '05195702943', 'Rua Nardelli Bairro Garibaldi');
INSERT INTO tbcitizen (ctzname, ctzcpf, ctzaddress) VALUES ('Monsiour Francoa', '05195702944', 'Rua Marcanti Bairro Nortre Drame');

INSERT INTO tbvehicle (vclplate, ctzid, vclmodel, vclcolor) VALUES ('PZ65PWO', 1, 1, 1);
INSERT INTO tbvehicle (vclplate, ctzid, vclmodel, vclcolor) VALUES ('FG45RYT', 1, 3, 1);
INSERT INTO tbvehicle (vclplate, ctzid, vclmodel, vclcolor) VALUES ('HD63RHJ', 1, 2, 2);
INSERT INTO tbvehicle (vclplate, ctzid, vclmodel, vclcolor) VALUES ('FG12PDS', 2, 1, 2);
INSERT INTO tbvehicle (vclplate, ctzid, vclmodel, vclcolor) VALUES ('HG53FJS', 2, 1, 3);