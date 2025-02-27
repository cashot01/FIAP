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


