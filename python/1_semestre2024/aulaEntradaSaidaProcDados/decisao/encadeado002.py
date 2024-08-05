# 2. Dadas duas notas, calcular a média e exibir se está "aprovado" (a partir de 6), "reprovado" (menor do que 4) ou em "exame" (entre 4 e 5.9)
import os
os.system("cls")

n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))
media =  (n1 + n2)/ 2
print(f"Media: {media}")
if media >= 6:
    print("PASSOU")
elif  5.9 >= media and media >= 4 :
    print("EXAME")
else:
    print("REPROVADO")