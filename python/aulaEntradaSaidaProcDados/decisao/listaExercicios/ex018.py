"""
18. Dados 3 numero pelo usuário, verificar se são diferentes, se forem exibir o numero com valor
intermediário, senão (se houver 2 ou 3 números iguais) exibir a mensagem “Os números não são
diferentes”.
"""
import os
os.system("cls")
n1 = float(input("n1: "))
n2 = float(input("n2: "))
n3 = float(input("n3: "))
if n1 != n2 != n3:
    if (n1 > n2 > n3) or (n3 > n2 > n1):
        print(n2)
    elif (n1 > n3 > n2) or (n2 > n3 > n1):
        print(n3)
    # elif (n2 > n1 > n3) or (n3 > n1 > n2):
    else:
        print(n1)
elif (((n1 == n2) and n1 > n3) or ((n1 == n3) and n1 > n2) or ((n2 == n3) and n2 > n1)):
    print("Nº não são diferentes")
else:
    print("nº nao diferentes")