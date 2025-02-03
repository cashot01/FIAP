# . Juntar os dois exercícios anteriores, ou seja, pedir a digitação das duas notas, caso uma (ou as duas) nota seja inválida exibir “Nota inválida!” e terminar o algoritmo; senão, calcular e exibir a média e exibir se está aprovado (vide saída do exercício anterior).
import os 
os.system("cls")
print("digite 2 notas validas (0 à 10)")
n1 = float(input("nota 1: "))
if n1 >= 0 and n1 <= 10:
    n2 = float(input("nota 2: "))
    if n2 >= 0 and n2 <= 10:
        media = (n1 + n2) / 2
        print(f"Média: {media}")
        if media >= 5:
            print("Status: PASSOU")
        else:
            print("Status: REPROVADO")
    else:
        print("Nota INVÁLIDA")
else:
    print("Nota INVÁLIDA")

    