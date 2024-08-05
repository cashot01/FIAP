"""
19. Dados 3 valores numéricos correspondentes a eventuais lados de triângulo, verificar se esses
valores formam um triângulo (para cada lado, a soma dos outros dois lados deve ser maior do que
ele). Se formar, exibir a mensagem “Forma um triângulo”, senão “Não forma um triângulo”.
"""
import os
os.system("cls")
n1 = float(input("n1: "))
n2 = float(input("n2: "))
n3 = float(input("n3: "))
if ((n1 + n2) > n3) and ((n1 + n3) > n2 ) and ((n2 + n3) > n1):
    print("Forma um triangulo")

else:
    print("Não forma um triângulo")

