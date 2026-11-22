-- banco de dados
IF DB_ID('Projeto_Paises') IS NULL
BEGIN
CREATE DATABASE Projeto_Paises;
PRINT 'Banco de dados criado com sucesso!';
END 
ELSE
BEGIN
PRINT 'O banco de dados já existe!';

END;

USE Projeto_Paises;

CREATE TABLE Paises (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Pais VARCHAR(100) NOT NULL,
    Continente VARCHAR(50) NOT NULL,
    Populacao_Milhoes INT NOT NULL,
    PIB_Trilhoes DECIMAL(10,2) NOT NULL,
    Area_Km2 BIGINT NOT NULL,
    Expectativa_Vida INT NOT NULL,
    IDH DECIMAL(4,3) NOT NULL,
    Moeda VARCHAR(50) NOT NULL,
    Capital VARCHAR(100) NOT NULL
);

PRINT 'Tabela Paises criada com sucesso!';