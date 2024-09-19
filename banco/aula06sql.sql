SELECT * FROM t_endereco;

SELECT * FROM T_ALUNO;

-- insert generico
INSERT INTO t_endereco VALUES (0122345, 'Av. Paulista', 'Centro', 'S�o Paulo', 'SP');



INSERT INTO t_endereco (cep, logradouro, bairro, cidade)
VALUES (0123454, 'Av. Ipiranga', 'Centro', 'Sao Paulo')

-- ATUALIZAR LINHAS TBELAS
-- UPDATE PROCEDUAL (ESPECIFICO) PARA N LINHAS
UPDATE T_ALUNO SET fk_cep=0131415 WHERE RA=1; 

-- UPDATE N�O PROCEDUAL (GENERICO) PARA N LINHAS
-- Where � uma restri��o de atualiza��o 
-- quando n�o h� o where, essa restri��o n existe
UPDATE t_aluno set nm_aluno='jose'

-- APAGAR DADOS DE UMA TABELA
DELETE FROM T_ALUNO;



-- DTL (DATA TRANSACTION LANGUAGE)
-- commit: confirmar transa��o 
-- rollback: defazer transa��o
-- � utilizada em conjunto com a DLM (INERT, UPDATE, DELETE)

commit;

rollback;

DELETE FROM T_ENDERECO;

UPDATE T_ENDERECO SET cidade='Campinas';
rollback;

