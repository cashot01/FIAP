import os
os.system("cls")
"""
 2. Dado o valor da venda e se o usuário tem o cupom de desconto, aplicar o 
desconto de 20 reais caso a venda seja a partir de 20 reais. Exibir o valor da 
venda com o desconto.
"""

valor = float(input("valor: "))
cupom = str(input("""Cupom de desconto valido somente para compra a partir de R$20,00
                  tem o cupom (s / n): """))
if valor >= 20 and cupom == "s":
    desconto20 = valor - 20
    print(f"desconto de R$20.00 , valor final: R$ {desconto20:.2f} ")
else:
    print(f"Valor: R$ {valor:.2f}")

