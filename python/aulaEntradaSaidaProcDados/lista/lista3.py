"""
3. Dado um valor pelo usuário, verificar se ele está contido na lista. Se existir exibir “Encontrado”, senão exibir
“Não encontrado”.
Valor: 33 Não encontrado
"""

lista = [45, 4.6, "edson", "a", "False"]
print(lista)

elemento = input("valor: ")

if elemento in lista:
    print(f"{elemento} Encontrado")
else:
    print(f"{elemento} Não encontrado")
