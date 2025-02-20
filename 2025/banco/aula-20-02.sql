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

/*
Criar um bloco PL-SQL para calcular o valor de cada parcela de uma compra de um carro, nas seguintes condições: 
- Parcelas para aquisição em 6 pagamentos. 
- Parcelas para aquisição em 12 pagamentos. 
- Parcelas para aquisição em 18 pagamentos. 
OBSERVAÇÃO: 
1 - Deverá ser dada uma entrada de 20% do valor da compra. 
2 – Deverá ser aplicada uma taxa juros, no saldo restante, nas seguintes condições: 
3 – No final informar o valor das parcelas para as 3 formas de pagamento, com o Valor de aquisição de 10.000 e o mesmo com entrada de dados via teclado (em tempo de execução).
A – Pagamento em 6 parcelas: 10%. 
B – Pagamento em 12 parcelas: 15%. 
C – Pagamento em 18 parcelas: 20%.
*/

SET SERVEROUTPUT ON;

DECLARE
	carro FLOAT := '&Digite_Valor_Carro';
	entrada FLOAT := carro * 0.20;
	carro_restante FLOAT := carro - entrada ;
	parcela_6x FLOAT := carro_restante / 6;
	parcela_12x FLOAT := carro_restante / 12;
	parcela_18x FLOAT := carro_restante / 18;
	
	-- valor_final_6x FLOAT := parcela_6x * 1.10;
	-- valor_final_12x FLOAT := parcela_12x * 1.15;
	-- valor_final_18x FLOAT := parcela_18x * 1.20;
	
	valor_final_6x FLOAT := (carro_restante * 1.10) / 6;
    valor_final_12x FLOAT := (carro_restante * 1.15) / 12;
    valor_final_18x FLOAT := (carro_restante * 1.20) / 18;


BEGIN
	dbms_output.put_line('Valor carro: R$ ' || carro);
	dbms_output.put_line('Entrada: R$ ' || entrada);
	dbms_output.put_line('');

	dbms_output.put_line('Parcela 6x: R$ ' || parcela_6x);
	dbms_output.put_line('Valor final 6x: R$ ' || valor_final_6x); 
	dbms_output.put_line('');

	dbms_output.put_line('Parcela 12x: R$ ' || parcela_12x);
	dbms_output.put_line('Valor final 12x: R$ ' || valor_final_12x); 
	dbms_output.put_line('');

	dbms_output.put_line('Parcela 18x: R$ ' || parcela_18x);
	dbms_output.put_line('Valor final 18x: R$ ' || valor_final_18x); 
	dbms_output.put_line('');

END;
