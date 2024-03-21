"""
20. Dados 3 valores numéricos correspondentes a eventuais lados de triângulo, verificar se esses
valores formam um triângulo (para cada lado, a soma dos outros dois lados deve ser maior do que
ele). Em caso afirmativo, informar ao usuário se o triângulo é equilátero (três lados iguais), isósceles (dois lados iguais) ou escaleno (três lados diferentes). Em caso negativo, exibir “Não forma
um triângulo”.
"""
import os
os.system("cls")
n1 = float(input("n1: "))
n2 = float(input("n2: "))
n3 = float(input("n3: "))
if ((n1 + n2) > n3) and ((n1 + n3) > n2) and ((n2 + n3) > n1):
    if n1 == n2 == n3:
        print("Triangulo EQUILATERO")
    elif ((n1 == n2) != n3) and ((n1 == n3) != n2) and ((n2 == n3) != n1):
        print("Triangulo ISOCELES")
    else:
        print("Triangulo ESCALENO")
else:
    print("não forma triangulo")