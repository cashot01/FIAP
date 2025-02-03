# 5. Dadas duas notas, calcular e exibir a média simples das mesmas. Caso a média seja inferior a 5 exibir “Você está reprovado”, senão exibir “Você está aprovado”.
import os 
os.system("cls")
n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))
media = (n1 + n2) / 2
print(f"Media: {media}")
if media >= 5:
    print("Vc passou")
else:
    print("REPROVADO")