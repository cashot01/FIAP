#1. Dada uma nota, exibir se ela é "válida" ou "inválida".
nota = float(input("nota: "))
if nota >= 0 and nota <=10:
    print("nota valida")
else: 
    print("nota invalida")