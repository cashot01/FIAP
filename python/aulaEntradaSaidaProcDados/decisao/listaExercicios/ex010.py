# 10. Dentre três números dados pelo usuário, verificar e exibir o de maior valor.
import os
os.system("cls")
n1 = float(input("n1: "))
n2 = float(input("n2: "))
n3 = float(input("n3: "))
if (n1 > n2 > n3) or (n1 > n3 > n2):
    print(f"Maior nº: {n1}")
elif (n2 > n1 > n3) or (n2 > n3 > n1):
    print(f"Maior nº: {n2}")
else:
    print(f"Maior nº: {n3}")