"""
3. Dado um valor pelo usuário, verificar se ele está contido na lista. Se existir exibir “Encontrado”, senão exibir
“Não encontrado”.
Valor: 33 Não encontrado
"""

#============================= SUBALGORITIMO
def encontrar_elemento(e: input) -> None:

    if e in lista:
        print(f"{e} Encontrado")
    else:
        print(f"{e} Não encontrado")


lista = [45, 4.6, "edson", "a", "False"]
print(lista)

elemento = input("digite algo: ")

encontrar_elemento(elemento)


