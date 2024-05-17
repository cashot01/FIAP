# Dada uma lista com notas preenchidas por parametro, todas as notas 
# daqueles que foram aprovados
def verifica_aprovados(l: list ) -> list:
    la = list()
    for i in range(len(l)):
        if l[i] >= 6:
            la.append(l[i])

    return la


#----------------------- Programa Principal
lista = [4, 8, 5.7, 8, 3, 5, 10, 7, 2, 1, 0, 3]
lista_aprovados = verifica_aprovados(lista)
print(lista_aprovados)
