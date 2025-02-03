 SELECT * FROM T_ENDERECO;
 
 SELECT * FROM T_ALUNO;
 

-- GEN�RICO (N�O PROCEDURAL) 
 INSERT INTO T_ENDERECO VALUES(01311000,'Av. Paulista',
                                'Centro','S�o Paulo','SP');
 INSERT INTO T_ENDERECO VALUES (01310100, 'Rua da Consola��o','Centro',
                                    'S�o Paulo','SP');                                
                                    
-- ESPECIFICO (OU PROCEDURAL)
-- � OBRIGAT�RIO MENCIONAR AS COLUNAS NOT NULL E PK
-- PK POSSUI EXCE��O QUANDO H� O GENERATED

INSERT INTO T_ENDERECO (cep, logradouro,bairro, cidade)
 VALUES (0131415,'Av. Ipiranga', 'Centro','S�o Paulo');
 
 -- ATUALIZAR LINHAS NA TABELAS
 
 -- UPDATE PROCEDURAL (OU ESPECIFICO) PARA 1� LINHA
 UPDATE T_ALUNO SET cep=0131415 WHERE id_aluno=1;
 
 -- UPDATE N�O PROCEDURAL (OU ESPECIFICO) PARA TODAS AS LINHAS
 -- WHERE � UMA RESTRI��O DE ATUALIZA��O
 -- QUANDO N�O H� O WHERE, ESSA RESTRI��O N�O EXISTE
 UPDATE T_ALUNO SET nm_aluno='Jos�';
 
 -- UPDATE PROCEDURAL (OU ESPECIFICO) PARA N LINHAS
 -- DEPENDENDO DA RESTRI��O NO WHERE, PODER� ATUALIZAS TODAS AS LNHAS OU ALGUMAS DELAS
 UPDATE T_ALUNO SET nm_aluno='Lucas' WHERE id_aluno>=1;
 
 INSERT INTO T_ALUNO (nm_aluno, sx_aluno, cep, cpf) 
    VALUES ('Maria Eduarda','F',0131415, 222333);
INSERT INTO T_ALUNO (nm_aluno, sx_aluno, cep, cpf) 
    VALUES ('Lucia','F',0131415, 222334);
 INSERT INTO T_ALUNO (nm_aluno, sx_aluno, cep, cpf) 
    VALUES ('Maria','F',0131415, 222335);
 -- UPDATE ESPECIFICO PARA MAIS DE 1 COLUNA
 -- SEPARAR COLUNAS POR VIGULAS APOS O SET
 
 UPDATE T_ALUNO SET nm_aluno='Francisco Douglas', 
                    sx_aluno='M', 
                    dt_nascimento=to_date('19-09-2004','DD-MM-YYYY') 
        WHERE id_aluno=2; 
        
-- APAGAR OS DADOS DA TABELA
-- ESPECIFICA (PROCEDURAL)
-- WHERE � UMA RESTRI��O DE REMO��O
DELETE FROM T_ALUNO WHERE id_aluno=2;

-- GEN�RICA (N�O PROCEDURAL)
-- Ir� remover todas as linhas da tabela, pois n�o h� o WHERE
DELETE FROM T_ALUNO;


-- DTL (Data Transaction Language)
-- commit: confirmar transa��o
-- rollback: desfazer a trasa��o
-- � utilizada em conjunto com a DML (INSERT, UPDATE e DELETE)

commit;

rollback;

DELETE FROM T_ENDERECO;
ROLLBACK;

UPDATE T_ENDERECO SET cidade='Campinas';
ROLLBACK;

INSERT INTO T_ENDERECO (cep, logradouro,bairro, cidade)
 VALUES (0131416,'Av. Ipiranga', 'Centro','S�o Paulo');
ROLLBACK;

INSERT INTO T_ENDERECO (cep, logradouro,bairro, cidade)
 VALUES (0131416,'Av. Ipiranga', 'Centro','S�o Paulo');
COMMIT;

ROLLBACK;

-- N�O H� ROLLBACKS AP�S O COMMIT
-- O COMMIT � A DEFINI��O DE UM "FIM DE TRABALHO", 
-- NO QUAL N�O PODE SER DESFEITO

-- REMOVER AS LINHAS DA TABELA 
SELECT * FROM T_ENDERECO;

-- SO PODEMOS REMOVER LINHAS QUE N�O EST�O RELACIONADAS COM OUTRAS TABELAS
-- CASO AO CONTR�RIO, HAVER� O ERRO 2292 SOBRE A FK

-- TRUNCATE
-- UTILIZAR TODAS AS LINHAS DA TABELA, DE MANEIRA FISICA
-- N�O EXISTE ROLLBACK/COMMIT PARA TRUNCATE
-- APAGAR� TUDO DE FORMA PERMANENTE

TRUNCATE TABLE T_ALUNO;
ROLLBACK; -- N�O IR� FUNCIONAR
SELECT * FROM T_ALUNO;