

CREATE TABLE T_ENDERECO(
  cep int,
  logradouro varchar(100) CONSTRAINT nn_log NOT NULL ,
  bairro varchar(100) CONSTRAINT nn_bairro NOT NULL ,
  cidade varchar(100) CONSTRAINT nn_cidade NOT NULL ,
  uf varchar(2),
  CONSTRAINT pk_cep PRIMARY KEY (cep),
  CONSTRAINT ck_uf CHECK(UF='SP' OR UF='RJ' 
     OR UF='PR' OR UF='PE' OR UF='AC' OR UF='MG' OR UF='BA' OR UF='AP')
);

CREATE TABLE T_ALUNO (
  ra int primary key,
  nome varchar(60) not null,
  cpf number(11) unique not null,
  sexo varchar(1) CHECK(sexo='f' OR sexo='m' OR sexo='i'),
  dt_nascimento date,
  num_endereco int,
  complemento varchar(100),
  fk_cep int references T_ENDERECO(cep)
);

DROP TABLE T_ALUNO;

-- COMENTÁRIO DE 1a linha
/* 
 comentário de n linhas 
*/