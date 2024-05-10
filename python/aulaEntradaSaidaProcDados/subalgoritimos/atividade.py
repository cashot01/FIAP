import os
os.system("cls")

def verifica_lista_inteiro(l: list) -> bool:
    print(l)
    for i in range(0, len(l), 1):
        l[i] = str(l[i])
        l[i].isnumeric()


        
        
    





# --------------- Programa para testar a função 

lista = [5, 8, 4, "edson", 12, 44]
if verifica_lista_inteiro(lista):
    print("Todos os elementos contidos na lista são inteiros")
else:
    print(" Nem todos os elementos contidos na lista são inteiros")

lista = [5, 8, 4, 12, 44]
if verifica_lista_inteiro(lista):
    print("Todos os elementos contidos na lista são inteiros")
else:
    print(" Nem todos os elementos contidos na lista são inteiros")