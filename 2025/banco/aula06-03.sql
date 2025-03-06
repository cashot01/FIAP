/*

Loop
	< instrução(ões) >
	Exit when < condição >
End loop;


*/

set SERVEROUTPUT on;

DECLARE 
	V_CONTADOR NUMBER(2):= 1; 
BEGIN 
LOOP 	
	DBMS_OUTPUT.PUT_LINE(V_CONTADOR); 
	V_CONTADOR := V_CONTADOR + 1; 
	EXIT WHEN V_CONTADOR > 20; 
END LOOP; 
END;

/*
Estrutura de repetição: while

WHILE < condição> LOOP 
	< instrução(ões) >;
END LOOP;


*/

DECLARE 
V_CONTADOR NUMBER(2):= 1; 
BEGIN 
    WHILE V_CONTADOR <= 20 LOOP 	
        DBMS_OUTPUT.PUT_LINE(V_CONTADOR); 	
        V_CONTADOR := V_CONTADOR + 1; 
    END LOOP; 
END;


/*
Estrutura de repetição: for

FOR < contador> IN <valor inicial> .. <valor final> LOOP 
	< instrução (ões) >;
END LOOP;


*/

BEGIN 
    FOR V_CONTADOR IN 1..20 LOOP 	
    DBMS_OUTPUT.PUT_LINE(V_CONTADOR); END LOOP; 
END;


/*
Estrutura de repetição: for - reverse

BEGIN 
    FOR V_CONTADOR IN REVERSE 1..20 LOOP 	
    DBMS_OUTPUT.PUT_LINE(V_CONTADOR); END LOOP; 
END;

*/


/*
1. Montar um bloco de programação que realize o processamento de uma tabuada qualquer, por exemplo a tabuada do número 150.

*/
set SERVEROUTPUT on;
DECLARE 
    v_tabuada number(2) := &tabuada;
	V_CONTADOR NUMBER(2):= 0; 
BEGIN 
LOOP 	
	DBMS_OUTPUT.PUT_LINE(V_CONTADOR||' X '||v_tabuada||' = '||v_contador * v_tabuada); 
	V_CONTADOR := V_CONTADOR + 1; 
	EXIT WHEN V_CONTADOR > 10; 
END LOOP; 
END;




/*
2. Em um intervalo numérico inteiro, informar quantos números são pares e quantos são ímpares.

*/
/*
DECLARE
    v_inicio NUMBER := 1; -- Início do intervalo
    v_fim NUMBER := 85; -- Fim do intervalo
    v_qtd_pares NUMBER := 0; -- Variável para armazenar a quantidade de números pares
    v_qtd_impares NUMBER := 0; -- Variável para armazenar a quantidade de números ímpares
    v_contador NUMBER; -- Variável de contador para percorrer o intervalo
BEGIN
    -- Loop para percorrer o intervalo e contar os números pares e ímpares
    FOR v_contador IN v_inicio..v_fim LOOP
        IF MOD(v_contador, 2) = 0 THEN -- Verifica se o número é par
            v_qtd_pares := v_qtd_pares + 1; -- Incrementa a quantidade de números pares
        ELSE
            v_qtd_impares := v_qtd_impares + 1; -- Incrementa a quantidade de números ímpares
        END IF;
    END LOOP;

    -- Exibição dos resultados
    DBMS_OUTPUT.PUT_LINE('Quantidade de números pares: ' || v_qtd_pares);
    DBMS_OUTPUT.PUT_LINE('Quantidade de números ímpares: ' || v_qtd_impares);
END;
*/

DECLARE
impar NUMBER := 0;
par NUMBER := 0;

BEGIN
    FOR X IN 1 .. &Valor LOOP
        IF MOD(X, 2) = 0 THEN
            par := par + 1;
        ELSE
            impar := impar + 1;
        END IF;
    END LOOP;

    DBMS_OUTPUT.PUT_LINE('Quantidade de números pares: ' || v_qtd_pares);
    DBMS_OUTPUT.PUT_LINE('Quantidade de números ímpares: ' || v_qtd_impares);

END;




/*
3. Exibir e média dos valores pares em um intervalo numérico e soma dos ímpares.
*/
DECLARE
 v_inicio NUMBER := 1; -- Início do intervalo
    v_fim NUMBER := 10; -- Fim do intervalo
    v_soma_impares NUMBER := 0; -- Variável para armazenar a soma dos números ímpares
    v_qtd_impares NUMBER := 0; -- Variável para contar a quantidade de números ímpares
    v_soma_pares NUMBER := 0; -- Variável para armazenar a soma dos números pares
    v_qtd_pares NUMBER := 0; -- Variável para contar a quantidade de números pares
    v_contador NUMBER; -- Variável de contador para percorrer o intervalo
    v_media_pares NUMBER; -- Variável para armazenar a média dos números pares
BEGIN
    -- Loop para percorrer o intervalo e calcular a soma dos ímpares e média dos pares
    FOR v_contador IN v_inicio..v_fim LOOP
        IF MOD(v_contador, 2) = 0 THEN -- Verifica se o número é par
            v_soma_pares := v_soma_pares + v_contador; -- Soma o valor ao total dos pares
            v_qtd_pares := v_qtd_pares + 1; -- Incrementa a quantidade de números pares
        ELSE
            v_soma_impares := v_soma_impares + v_contador; -- Soma o valor ao total dos ímpares
            v_qtd_impares := v_qtd_impares + 1; -- Incrementa a quantidade de números ímpares
        END IF;
    END LOOP;

    -- Calcular a média dos números pares
    IF v_qtd_pares <> 0 THEN
        v_media_pares := v_soma_pares / v_qtd_pares;
    ELSE
        v_media_pares := 0; -- Evita divisão por zero se não houver números pares
    END IF;

    -- Exibição dos resultados
    DBMS_OUTPUT.PUT_LINE('Soma dos números ímpares: ' || v_soma_impares);
    DBMS_OUTPUT.PUT_LINE('Média dos números pares: ' || v_media_pares);
END;


