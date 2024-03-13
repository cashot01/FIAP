import os
os.system("cls")

valor = float(input("valor da compra: R$ "))
if valor > 500:
    valor = valor * 0.88
    print(f"Valor: R$ {valor:.2f} ")
else:
    valor = valor * 0.94
    print(f"Valor: R$ {valor}")
cupom = str(input("cupom: "))
if cupom == "s":
    valor = valor - 20
    print(f"Valor: R$ {valor}")
else:
    print(f"Valor: R$ {valor}")