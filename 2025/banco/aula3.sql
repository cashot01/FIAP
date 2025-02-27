SET SERVEROUTPUT ON;

DECLARE 
       V_N NUMBER(2) := 15; 
BEGIN 
       IF MOD(V_N,2) = 0 THEN 	
	DBMS_OUTPUT.PUT_LINE('O número ' || V_N || ' é PAR'); 
        ELSE 
	DBMS_OUTPUT.PUT_LINE('O número ' || V_N || ' é ÍMPAR'); 
         END IF; 
END;

-- =======================================================================
--Exercícios de condicionais com os dados importados


SELECT * FROM VENDASS;

DECLARE

  TIPO_CLIENTE VARCHAR2(40) := '0';

BEGIN
  FOR X IN (SELECT DEALSIZE, ORDERNUMBER
              FROM VENDASS
             where ordernumber in (10402, 10134, 10168)) loop
  
    IF x.DEALSIZE = 'Medium' THEN
      DBMS_OUTPUT.PUT_LINE(x.ORDERNUMBER || ' Empresa de Médio Porte');
    elsif X.DEALSIZE = 'Small' then
      DBMS_OUTPUT.PUT_LINE('Empresa de Pequeno Porte');
    else
      DBMS_OUTPUT.PUT_LINE('Empresa de Grande Porte');
    
    END IF;
  end loop;
end;

---------------------------------------------------------------------------------------------------------

-- Criar um bloco PL/Sql para analisar a entrada de dados do sexo de um cliente, o bloco deverá receber o dado sobre o sexo: para masculino – M ou m, para feminino -  F ou f, qualquer dado fora desta configuração deverá ser exibido ‘Outros’, para M ou m ‘Masculino’, para F ou f ‘Feminino’.

SET SERVEROUTPUT ON;
DECLARE
    genero CHAR(1) := '&Genero';
BEGIN
    IF upper(genero) = 'M' THEN
        DBMS_OUTPUT.PUT_LINE('Masculino');
    ELSIF upper(genero) = 'F' THEN
       DBMS_OUTPUT.PUT_LINE('Feminino'); 
    ELSE
        DBMS_OUTPUT.PUT_LINE('não identificado');
    END IF;
END;

-----------------------------------------------------------------------------------------------------------------------

CREATE TABLE ALUNO ( RA CHAR(9), 
NOME VARCHAR2(50), 
CONSTRAINT ALUNO_PK PRIMARY KEY(RA)); 

SELECT * FROM ALUNO;

INSERT INTO ALUNO (RA,NOME) VALUES ('111222333','Antonio Alves');
INSERT INTO ALUNO (RA,NOME) VALUES ('222333444','Beatriz Bernardes'); 
INSERT INTO ALUNO (RA,NOME) VALUES ('333444555','Cláudio Cardoso');

-- E, finalmente, vamos criar um bloco PL/SQL que deverá imprimir na tela o nome do aluno cujo RA é igual a 333444555:
DECLARE 
	V_RA CHAR(9) := '333444555'; 
	V_NOME VARCHAR2(50);
BEGIN 
	SELECT NOME INTO V_NOME FROM ALUNO WHERE RA = V_RA; 	
    DBMS_OUTPUT.PUT_LINE ('O nome do aluno é: ' || V_NOME);
END;

DECLARE 
	V_RA CHAR(9) := '444555666'; 
	V_NOME VARCHAR2(50) := 'Daniela Dorneles'; 
BEGIN 
	INSERT INTO ALUNO (RA,NOME) VALUES (V_RA,V_NOME); 
END;

DECLARE 
	V_RA CHAR(9) := '111222333'; 
	V_NOME VARCHAR2(50) := 'Antonio Rodrigues'; 
BEGIN 
	UPDATE ALUNO SET NOME = V_NOME WHERE RA = V_RA; 
END;

DECLARE 
	V_RA CHAR(9) := '444555666'; 
BEGIN 
DELETE FROM ALUNO WHERE RA = V_RA; 
END;




