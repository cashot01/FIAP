
 -- REMOVENDO TABELAS
DROP TABLE T_CONTATO;
DROP TABLE T_ALUNO;
DROP TABLE T_ENDERECO;


/* 
ORDEM DE REMO��O: 1� AS TABELAS FRACAS E DEPOIS AS FORTES
    COMO � O O SCRIPT:
        * INICIO: TABELAS COM MAIS DE UMA FK
        * MEIO: TABELAS COM PK E FK
        * FIM: TABELAS COM PK
ORDEM DE CRIA��O: 1� AS TABELAS FORTES E DEPOIS AS FRACAS
    COMO � O O SCRIPT:
        * INICIO: TABELAS COM PK
        * MEIO: TABELAS COM PK E FK
        * FIM: TABELAS COM MAIS DE UMA FK

TABELA FORTE: � AQUELA QUE PERMITE O RELACIONAMENTO E NORMALMENTE TEM APENAS A PKs
TABELA FRACA: � AQUELA QUE RECEBE O RELACIONAMENTO E NORMALMENTE TEM UMA OU MAIS FKs
*/
-- CRIANDO TABELAS
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

CREATE TABLE T_CONTATO (
    id_contato int primary key,
    tel_contato varchar(50),
    email_contato varchar(50),
    ra int references T_ALUNO(ra)
);

-- listar todas as tabelas
SELECT * FROM USER_TABLES;

-- visualizar uma tabela
DESC t_aluno;

DESC T_CONTATO;

-- adicionar colunas
ALTER TABLE T_CONTATO
    ADD parentesco varchar(20);

-- renomear colunas

ALTER TABLE T_CONTATO 
    RENAME COLUMN email_contato to email;

-- adicionando uma constraint a uma coluna existente
ALTER TABLE T_CONTATO
    ADD CONSTRAINT UK_TEL UNIQUE(tel_contato);

-- listando constraints em uma determinada tabela
SELECT * FROM  USER_CONSTRAINTS WHERE table_name='T_CONTATO';

-- removendo uma coluna
ALTER TABLE T_CONTATO
    DROP COLUMN email;

-- renomeando objetos 
RENAME T_ALUNO TO T_ESTUDANTE;

-- COMENT?RIO DE 1a linha
/* 
 coment?rio de n linhas 
*/