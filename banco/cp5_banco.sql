//Insert CLIENTE
INSERT INTO T_QF_CLIENTE (id_cliente, nm_cliente, cpf, dt_nascimento, sx_cliente, st_cliente) VALUES (1, ' Silva', '123.456.789-00', TO_DATE('1988-05-27', 'YYYY-MM-DD'), 'M', 'A');
INSERT INTO T_QF_CLIENTE (id_cliente, nm_cliente, cpf, dt_nascimento, sx_cliente, st_cliente) VALUES (2, 'Sandra', '987.456.320-90', TO_DATE('1999-1-15', 'YYYY-MM-DD'), 'F', 'A');
 
//Insert AUTENTICA 
INSERT INTO T_QF_AUTENTICA (id_autentica, login, senha, T_QF_CLIENTE_id_cliente) VALUES (1, 'silva', 'senha123', 1);
INSERT INTO T_QF_AUTENTICA (id_autentica, login, senha, T_QF_CLIENTE_id_cliente) VALUES (2, 'sandra', 'senha987', 2);
 
//Insert ENDERECO
INSERT INTO T_QF_ENDERECO (id_endereco, cep, logradouro, numero, complemento, bairro, cidade, uf, ponto_referencia, T_QF_CLIENTE_id_cliente) VALUES (1, '01005-070', 'Rua Cep', 10, 'Apt 206', 'Centro', 'São Paulo', 'SP', 'Próximo ao mercado', 1);
INSERT INTO T_QF_ENDERECO (id_endereco, cep, logradouro, numero, complemento, bairro, cidade, uf, ponto_referencia, T_QF_CLIENTE_id_cliente) VALUES (2, '06877-000', 'Rua Pascal', 240, 'Casa', 'Jardim', 'São Paulo', 'MG', 'Ao lado da escola', 2);
 
//Insert CUPOM
INSERT INTO T_QF_CUPOM (id_cupom, cd_cupom, vl_desconto, val_cupom) VALUES (1, 'DESCONTO36', 10.00, TO_DATE('2024-12-3', 'YYYY-MM-DD'));
INSERT INTO T_QF_CUPOM (id_cupom, cd_cupom, vl_desconto, val_cupom) VALUES (2, 'PROMO29', 20.00, TO_DATE('2024-1-30', 'YYYY-MM-DD'));
 
//Insert PEDIDO
INSERT INTO T_QF_PEDIDO (id_pedido, dt_hr_pedido, st_pedido, vl_total, vl_desconto, obs_gerais, T_QF_CLIENTE_id_cliente, T_QF_CUPOM_id_cupom) VALUES (1, TO_DATE('2023-1-01', 'YYYY-MM-DD'), 'Pendente', 200.00, 10.00, 'Aguardando pagamento', 1, 1);
INSERT INTO T_QF_PEDIDO (id_pedido, dt_hr_pedido, st_pedido, vl_total, vl_desconto, obs_gerais, T_QF_CLIENTE_id_cliente, T_QF_CUPOM_id_cupom) VALUES (2, TO_DATE('2024-10-02', 'YYYY-MM-DD'), 'Pago', 150.00, 20.00, 'Pagamento confirmado', 2, 2);
 
//Insert PAGAMENTO
INSERT INTO T_QF_PAGAMENTO (id_pagamento, T_QF_PEDIDO_id_pedido, forma_pagamento, vl_pagamento, dt_hr_pagamento, st_pagamento) VALUES (1, 1, 'Crédito', 200.00, TO_DATE('2023-1-01', 'YYYY-MM-DD'), 'Aguardando');
INSERT INTO T_QF_PAGAMENTO (id_pagamento, T_QF_PEDIDO_id_pedido, forma_pagamento, vl_pagamento, dt_hr_pagamento, st_pagamento) VALUES (2, 2, 'Boleto', 150.00, TO_DATE('2024-10-02', 'YYYY-MM-DD'), 'Pago');
 
//Insert CATEGORIA
INSERT INTO T_QF_CATEGORIA (id_categoria, ds_categoria) VALUES (1, 'Eletrônicos');
INSERT INTO T_QF_CATEGORIA (id_categoria, ds_categoria) VALUES (2, 'Móveis');
 
//Insert MARCA
INSERT INTO T_QF_MARCA (id_marca, ds_marca) VALUES (1, 'Samsung');
INSERT INTO T_QF_MARCA (id_marca, ds_marca) VALUES (2, 'Motorola');
 
//Insert PRODUTO
INSERT INTO T_QF_PRODUTO (id_produto, ds_produto, vl_produto, peso, fl_inativo, id_categoria, id_marca) VALUES (1, 'TV 50 Polegadas', 250.00, 15.00, 'N', 1, 1);
INSERT INTO T_QF_PRODUTO (id_produto, ds_produto, vl_produto, peso, fl_inativo, id_categoria, id_marca) VALUES (2, 'Sofá 3 Lugares', 120.00, 50.00, 'N', 2, 2);
 
//Insert ARMAZEM
INSERT INTO T_QF_ARMAZEM (id_armazem, ds_armazem, local_armazem) VALUES (1, 'Armazém Principal 1', 'São Paulo');
INSERT INTO T_QF_ARMAZEM (id_armazem, ds_armazem, local_armazem) VALUES (2, 'Armazém Secundário', 'Minas Gerais');
 
//Insert ESTOQUE
INSERT INTO T_QF_ESTOQUE (id_estoque, id_produto, id_armazem, qtd_disponivel) VALUES (1, 1, 1, 10);
INSERT INTO T_QF_ESTOQUE (id_estoque, id_produto, id_armazem, qtd_disponivel) VALUES (2, 2, 2, 45);
 
//Insert ITEM PEDIDO
INSERT INTO T_QF_ITEM_PEDIDO (id_item, id_pedido, id_produto, qt_produto, vl_subtotal, vl_desconto) VALUES (1, 1, 1, 2, 500.00, 500.00);
INSERT INTO T_QF_ITEM_PEDIDO (id_item, id_pedido, id_produto, qt_produto, vl_subtotal, vl_desconto) VALUES (2, 2, 2, 1, 120.00, 120.00);