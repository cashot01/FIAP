/*

Loop
	< instrução(ões) >
	Exit when < condição >
End loop;


*/

set serveroutput on;

DECLARE 
	V_CONTADOR NUMBER(2):= 1; 
BEGIN 
LOOP 	
	DBMS_OUTPUT.PUT_LINE(V_CONTADOR); 
	V_CONTADOR := V_CONTADOR + 1; 
	EXIT WHEN V_CONTADOR > 20; 
END LOOP; 
END;
