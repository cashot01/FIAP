SELECT * FROM PAIS;
 
INSERT INTO PAIS VALUES (19, 'China');
COMMIT;
 
declare
    v_cod NUMBER:= '&cod';
    v_nom VARCHAR2(50):= '&pais';
begin
    INSERT INTO PAIS VALUES (v_cod, v_nom);
    commit;
end;
 
 
CREATE OR REPLACE PROCEDURE g_insert_pais(
    p_id_pais NUMBER,
    p_nome_pais VARCHAR2
) AS
BEGIN
    INSERT INTO PAIS VALUES (p_id_pais, p_nome_pais);
    commit;
end;
 
 
CALL g_insert_pais(77, 'COSTA RICA');

 
BEGIN
g_insert_pais();
END;
 
 
CREATE OR REPLACE PROCEDURE g_update_pais(
    p_id_pais NUMBER,
    p_nome_pais VARCHAR2
) AS
BEGIN
    UPDATE PAIS SET NOM_PAIS = p_nome_pais WHERE COD_PAIS = p_id_pais;
    commit;
end;
 
CALL g_insert_pais(77, 'COSTA RICA UPDATE');