-- criar banco de dados
						


-- utilizar banco de dados
use FIAP;

create table T_TURMA(
	id_turma int primary key,
    sg_turma varchar(6),
    curso varchar(30),
    periodo varchar(15) -- noturno, matutino e vespertino
);


CREATE TABLE T_ALUNO(
	id_aluno int primary key,
    nome varchar(60),
    rm int not null,
    dt_nascimento date,
    st_aluno boolean,
    renda double,
    fk_id_turma INT,
    FOREIGN key (fk_id_turma) references T_TURMA(id) -- chave estrangeira
);


-- apagar tabela
drop table T_Aluno