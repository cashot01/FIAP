SELECT
		A.NOM_PAIS pais,
		B.NOM_ESTADO ESTADO,
		COUNT (NOM_CIDADE) "QTD CIDADE"
FROM
		pf1788.pais a
		LEFT JOIN pf1788.estado b ON ( a.cod_pais = b.cod_pais)
		INNER JOIN pf1788.CIDADE c ON (B.COD_ESTADO = C.COD_ESTADO)
		--WHERE A.NOM_PAIS = 'Brazil'
GROUP BY
		a.nom_pais,
		B.NOM_ESTADO
		HAVING COUNT (nom_estado)> 0
ORDER BY 3;

---------------------------------------------------------------------------------------------------------------------

-- PL/SQL

-- dbms_output.put_line --> PRINT

SET SERVEROUTPUT ON;

DECLARE
		idade NUMBER;
		NOME VARCHAR2(30) := 'VERGILO';
		ENDERECO VARCHAR2(50) := '&DIGITE_ENDERECO';
BEGIN
		idade := 39;
		dbms_output.put_line('a IDADE INFORMADA É:' || idade);
		dbms_output.put_line('NOME:' || NOME);
		dbms_output.put_line('ENDEREÇO:' || ENDERECO);
		-- dbms_output.put_line --> PRINT
END;

---------------------------------------------------------------------------------------------------------------------

-- exercicio - criar bloco PLSQL para calcular o valor em REAIS de 45 dólares, considere que o cambio é de R$ 5.70

SET SERVEROUTPUT ON;


DECLARE
    DOLAR FLOAT := 5.70;
BEGIN
   dbms_output.put_line(' ' || DOLAR * 45 );
   
END;

---------------------------------------------------------------------------------------------------------------------

/* exercicio - Criar um bloco PL-SQL para calcular o valor das parcelas de uma compra de um carro, nas seguintes condições:
OBSERVAÇÃO:
1 - Parcelas para aquisição em 10 pagamentos.
2 - O valor da compra deverá ser informado em tempo de execução.
3 – O valor total dos juros é de 3% e deverá ser aplicado sobre o montante financiado
4 – No final informar o valor de cada parcela. */

SET SERVEROUTPUT ON;


DECLARE
    CARRO FLOAT := '&DIGITE_VALOR_CARRO';
    PARCELAS NUMBER := 10;
	carro_juros FLOAT := CARRO * 1.03;
    
BEGIN
    dbms_output.put_line('VALOR CARRO: R$' || carro );
    dbms_output.put_line('VALOR PARCELA EM 10X: R$' || carro_juros / PARCELAS );
    dbms_output.put_line('VALOR TOTAL COM JUROS: R$' || (carro_juros)  );
   
END;

