#1. Dada uma nota, exibir se ela é "válida" ou "inválida".
import os 
os.system("cls")

nota = float(input("nota: "))
if  nota >= 0 :
    print(f"nota valida:  {nota} ")
elif nota < 0 and nota > 10:
    print(f"nota invalida:  {nota}")