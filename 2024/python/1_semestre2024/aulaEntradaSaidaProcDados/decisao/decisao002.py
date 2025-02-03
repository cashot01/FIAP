import os 
os.system("cls")

#  2. Numa loja, uma compra acima de 100 terá desconto de 10%. Pedir o valor do pedido e exibir o valor final
valor = float(input("valor da compra: "))
desconto = valor -(valor * 0.10)
if valor > 100:
    print(f"Valor acima de R$100,00 desconto de 10% valor final: R$ {desconto:.2f}")
else:
    print(f"R$ {valor}")
