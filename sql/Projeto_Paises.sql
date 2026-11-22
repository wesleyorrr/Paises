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