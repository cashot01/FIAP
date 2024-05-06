import os
os.system("cls")

print("\n =============== LISTA VAZIA")
lista = list()
print(f"Lista Vazia = {lista}")

print("\n =============== APPEND")
lista.append(22)
# .append adiciona no final da lista
lista.append(57.7)
lista.append("Logica")
print(lista)

print("\n =============== INSERT")
lista.insert(10, "Cauan")
# insert insere um dado numa posição da lista especifica
# 1º coloca o indice depois o dado
# se o valor do indice for maior que a lista, o item será colocado no final da lista
print(lista)


# print("============= POP")
# lista.pop()
# pop remove o elemento com a posição informada da lista, caso não informe a posição remove o ultimo elemento
# se colocar indice q 
# print(lista)

print("\n =============== REMOVE")
lista.remove(57.7)
# remove o elemento 
# se colocar elemento q n existe da erro
print(lista)


print("\n =============== INDEX")
indice = lista.index("Cauan")
# index - mostra o indice do elemento escolhido
print(f"Indice = {indice}")

print("\n =============== COUNT")
qtd = lista.count(22)
# count - conta quatos elementos especificos tem na lista
print(f"Quantidade: {qtd}")

print("\n =============== LEN")
qtd_elementos = len(lista)
# len conta quantos elementos existem na lista
print(f"Quantidade de elementos = {qtd_elementos}")

nome = "Cauan Aranega Passos"
print(f"{nome} tem {len(nome)} caracteres")
# len tbm pode ser usado para contar os caracteres de um string
print()

for i in range(0, len(lista), 1):
    print(f"{lista[i]}")
# tbm usa para percorrer uma lista em for 
# desse jeito capturo o elemento e o indice

for dado in lista:
    print(f"{dado}", end=" ")
# desse jeito só capturo o elemento 


print("\n =============== SUM")
lista = [19, 4, 25, 33, -5]
print(lista)
print(sum(lista))
# sum - soma os elementos da lista caso todos sejam numericos
# da para colocar True vale 1, e false vale 0 


print("\n =============== CONCATENAÇÃO (+)")
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
# + concatena (junta) listas
print(f"Lista1 = {lista1}")
print(f"Lista2 = {lista2}")
print(f"Lista3 = {lista3}")

print("\n =============== EXETEND")
lista1 = [1, 2, 3]
print(f"Lista1 = {lista1}")
lista2 = [4, 5, 6]
print(f"Lista2 = {lista2}")
lista2.extend(lista1)
# extend adiciona ao final da lista outra lista
print(f"Lista2 = {lista2}")

print("\n =============== COPY")
lista1 = [1, 2, 3]
lista2 = lista1.copy()
print(f"Lista1 = {lista1}")
print(f"Lista2 = {lista2}")

print("\n =============== SORT (REVERSE)")
lista = [19, 4, 25, 33, -5]
print(lista)
lista.sort()
# ordena os elementos da lista
# parametro reverse=True permite que seja ordenada em ordem decescente
print(f"Ordem crescente = {lista}")
lista.sort(reverse=True)
print(f"Decrescente = {lista}")

print("\n =============== REVERSE()")
lista = [19, 4, 25, 33, -5]
print(lista)
lista.reverse()
# reverse inverte a ordem dos elementos dentro da lista
print(f"Ordem Invertida = {lista}")

print("\n =============== CLEAR()")
lista = [19, 4, 25, 33, -5]
print(lista)
lista.clear()
# clear apaga todods os elementos da lista
print(lista)

print("\n =============== DEL (LISTA)")
lista = [19, 4, 25, 33, -5]
del(lista)
# del (lista) exclui (desloca) a lista da memoria