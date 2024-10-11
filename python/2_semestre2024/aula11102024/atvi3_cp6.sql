
CREATE TABLE tabela_exemplo (
    pk NUMBER PRIMARY KEY,
    coluna_1 VARCHAR2(100),
    coluna_2 VARCHAR2(100),
    coluna_3 VARCHAR2(100),
    coluna_4 VARCHAR2(100)
);

INSERT INTO tabela_exemplo values(1, 'teste', 'teste2', 'teste3', 'teste4');

CREATE TABLE T_PESSOA_PY (
    id NUMBER PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL,
    email VARCHAR2(100),
    telefone VARCHAR2(15),
    endereco VARCHAR2(255)
);