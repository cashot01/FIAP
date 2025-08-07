-- triggers


ALTER TABLE PEDIDO_NOVOS ADD STATUS VARCHAR2(30);


SELECT * FROM PEDIDO_NOVOS;

CREATE OR REPLACE TRIGGER trg_pedido
BEFORE INSERT ON PEDIDO_NOVOS
FOR EACH ROW
BEGIN
    -- atualiza o status do pedido para Novo apos a inserção
    IF :NEW.STATUS IS NULL THEN
    :NEW.STATUS := 'Novo Pedido';
    END IF;
END;


INSERT into PEDIDO_NOVOS (
    COD_PEDIDO,
    COD_CLIENTE,
    COD_USUARIO
) VALUES (
    11445555,
    74,
    1);


SELECT * from PEDIDO_NOVOS WHERE COD_PEDIDO = 11445555;


CREATE TABLE TB_AUDITORIA
(
    id NUMBER GENERATED ALWAYS as IDENTITY,
    tabela VARCHAR2(30),
    operacao VARCHAR2(30),
    data DATE,
    usuario VARCHAR2(30)
)

CREATE OR REPLACE TRIGGER trg_auditoria
AFTER INSERT OR UPDATE OR DELETE ON pedido_novos
FOR EACH ROW
DECLARE
  operacao VARCHAR2(30);
  nome_usuario VARCHAR2(100);
BEGIN
  -- Determina a operação realizada (INSERT, UPDATE OU DELETE)
  IF INSERTING THEN
    operacao := 'INSERT';
  ELSIF UPDATING THEN
    operacao := 'UPDATE';
  ELSIF DELETING THEN
    operacao := 'DELETE';
  END IF;

  -- Obtém o nome de usuário da sessão atual
  nome_usuario := SYS_CONTEXT('USERENV', 'SESSION_USER');

  -- Registra a auditoria na tabela de auditoria
  INSERT INTO TB_AUDITORIA (tabela, operacao, data, usuario)
  VALUES ('PEDIDO_NOVOS', operacao, SYSDATE, nome_usuario);

END;
