# dada uma lista passada por parametro , verificar se nela consta somente valores inteiro.
# se sim retornar True, se não False
import os
os.system("cls")

# INICIO subalgoritimo principal ---------------------------------------
def eh_lista_int(l:list) -> bool:

    # Inicio Subalgoritimo encadeado ------------------
    def transforma_str(l:list) -> None:
        for i in range(len(l)):
            l[i] = str(l[i])
    # FIM do subalgoritimo encadeado -------------------

    transforma_str(l)
    lista_int = True
    for i in range(len(l)):
        if not l[i].isnumeric():
            lista_int = False
            break
    return lista_int
# FIM subalgoritimo Principal --------------------------------------


#----------------------------------Programa Principal
lista = [54, 3, 7, 1, 23]
if eh_lista_int(lista):
    print("Todos os elementos contidos na lista são inteiros")
else:
    print(" Nem todos os elementos contidos na lista são inteiros")

lista = [5, 8, 4, "edson", 12, 44]
if eh_lista_int(lista):
    print("Todos os elementos contidos na lista são inteiros")
else:
    print(" Nem todos os elementos contidos na lista são inteiros")