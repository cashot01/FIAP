CREATE DATABASE FIAP;
USE FIAP;

CREATE TABLE T_ENDERECO(
  cep int,
  logradouro varchar(100)  NOT NULL ,
  bairro varchar(100)  NOT NULL ,
  cidade varchar(100)  NOT NULL ,
  uf varchar(2),
  CONSTRAINT pk_cep PRIMARY KEY (cep),
  CONSTRAINT ck_uf CHECK(UF='SP' OR UF='RJ' 
     OR UF='PR' OR UF='PE' OR UF='AC' OR UF='MG' OR UF='BA' OR UF='AP')
);

INSERT INTO t_endereco (cep, logradouro,bairro, cidade)
 VALUES (0131417,'Av. Ipiranga', 'Centro','São Paulo');
 rollback;

 DELETE FROM t_endereco;

