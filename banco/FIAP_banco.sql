
-- todos os objetos criados precisam tem um ; no final

/*
- Banco de dados tem:
    - USUARIOS:
        - TABELAS, VIEWS, SEQUENCES, ETC
DENTRO DO BANCO NÃO PODE TER USUARIOS REPETIDOS 
    DENTRO DO USUARIO NÃO PODE TER OBJETOS REPETIDOS
        DENTRO DA TABELA NÃO PODE TER COLUNAS REPETIDAS (OU DUPLICADAS)

*/


create table Aluno(
    id_aluno int PRIMARY KEY,
    nm_aluno VARCHAR(60) not null,
    dt_nascimento date,
    cpf varchar(15),
    rg varchar(15), 
    CONSTRAINT uk_rg_cpf UNIQUE(cpf, rg) -- chave unica composta 
);

create table Contato(
    id_contato int primary key,
    grau_parentesco varchar(20) not null,
    res_telefone varchar(12),
    email varchar(255),
    celular varchar(12) not null,
    id_aluno int references Aluno(id_aluno) -- chave estrangeira
);


-- UTILIZAMOS APENAS O DROP QUANDO A TABELA ESTÁ VAZIA DE LINHAS
-- QUANDO A TABELA TEM LINHAS, UTILIZAR O ALTER
-- O COMANDO DROP APAGA A TABELA E AS SUAS LINHAS

drop table Contato;
drop table Aluno;