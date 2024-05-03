lista = list()
lista.append(22)
# .append adiciona no final da lista
lista.append(57.7)
lista.append("Logica")
print(lista)

lista.insert(10, "Cauan")
# insert insere um dado numa posição da lista especifica
# 1º coloca o indice depois o dado
# se o valor do indice for maior que a lista, o item será colocado no final da lista
print(lista)

lista.pop(1)
# pop remove o elemento com a posição informada da lista, caso não informe a posição remove o ultimo elemento
# se colocar indice q 
print(lista)

lista.remove(57.7)
# remove o elemento 
# se colocar elemento q n existe da erro
print(lista)

indice = lista.index("Cauan")
print(f"Indice = {indice}")

