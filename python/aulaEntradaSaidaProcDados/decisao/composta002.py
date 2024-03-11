import os
os.system("cls")
"""
 2. Dado o valor da venda e se o usuário tem o cupom de desconto, aplicar o 
desconto de 20 reais caso a venda seja a partir de 20 reais. Exibir o valor da 
venda com o desconto.
"""

valor = float(input("valor: "))
cupom = int(input("""vc tem o cupom de desconto? 
                  cupom valido somente se o valor da compra for no minimo R$ 20,00
                   [1]Tenho
                   [2]Não tenho 
                  selecione opção 1 ou 2: """))
if cupom == 1 and valor >= 20:
    desconto20 = valor - 20
    print(f"desconto de R$20.00 , valor final: R$ {desconto20:.2f} ")
else:
    print(f"Valor: R$ {valor:.2f}")

