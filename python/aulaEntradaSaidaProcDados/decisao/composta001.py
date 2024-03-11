import os
os.system("cls")
#Dado pelo usuário o valor da, calcular 12% de desconto caso a venda seja maior do que 500 reais ou 6% se for até 500 reais. Exibir o valor da venda com o desconto.
valor = float(input("valor: "))
if valor > 500:
    desconto12 = valor - (valor * 0.12)
    print(f"valor maior que 500 , 12% desconto, R$ {desconto12:.2f}")
else:
    desconto6 = valor - (valor * 0.6)
    print(f"valor até 500 , 6% desconto, R$ {desconto6:.2f}")