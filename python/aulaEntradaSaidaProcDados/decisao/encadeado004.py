# 4. Junte todos os exercicios. A cada nota digitada, se forem válidas, calcule a média e mostre o status.
import os
os.system("cls")
n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))
n3 = float(input("nota 3: "))

# NOTA VALIDA
if (n1 >= 0 and n1 <= 10) and (n2 >= 0 and n2 <= 10) and (n3 >= 0 and n3 <= 10) :
    print("TODAS NOTAS VALIDAS")
elif n2 >= 0 and n2 <= 10:
    print(f"NOTA VALIDA: {n2}")
elif n3 >= 0 and n3 <= 10:
    print(f"NOTA VALIDA: {n3}")
# NOTA INVALIDA
elif n1 < 0 or n1 > 10:
    print(f"NOTA INVALIDA: {n1}")
elif n2 < 0 or n2 > 10:
    print(f"NOTA INVALIDA: {n2}")
elif n3 < 0 or n3 > 10:
    print(f"NOTA INVALIDA: {n3}")
# STATUS - PASSOU, EXAME , REPROVADO
    
