
-- todos os objetos criados precisam tem um ; no final

/*
- Banco de dados tem:
    - USUARIOS:
        - TABELAS, VIEWS, SEQUENCES, ETC
DENTRO DO BANCO N�O PODE TER USUARIOS REPETIDOS 
    DENTRO DO USUARIO N�O PODE TER OBJETOS REPETIDOS
        DENTRO DA TABELA N�O PODE TER COLUNAS REPETIDAS (OU DUPLICADAS)

*/


create table Aluno(
    id_aluno int PRIMARY KEY,
    nm_aluno VARCHAR(60) not null,
    dt_nascimento date,
    cpf varchar(15),
    rg varchar(15), 
    CONSTRAINT uk_rg_cpf UNIQUE(cpf, rg) -- chave unica composta 
);