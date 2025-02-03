import os
os.system("cls")

'''
Algumas das principais características dos conjuntos incluem:

- Armazena apenas itens não-duplicados (únicos)
- Suporta operações matemáticas sobre conjuntos (união, intersecção, etc)
- Não é possível modificar os itens existentes, mas podemos adicionar novos elementos (sets são mutáveis).
- Suporta elementos de qualquer tipo, não-ordenados e não-indexados.
- Podem conter apenas objetos imutáveis, como strings, ints, floats e tuplas de objetos também imutáveis.
- São escritos com chaves.
'''

# ============= MANIPULANDO SETS EM PYTHON
# Exemplo de criação de sets vazio
conjunto = {}
conjunto = set()
print(conjunto)
print('--------------------------------')

# Criando set a partir de uma lista
numeros = [1, 2, 2, 3, 3, 3]
conjunto = set(numeros)
print("Números: ", numeros)
print("Números distintos: ", conjunto)
print('--------------------------------')

# Inserindo elementos em um set
# Exemplo de criação de sets.
numeros = [1, 2, 2, 3, 3, 3]
conjunto = set()
for num in numeros:
    conjunto.add(num)  # adiciona um item num set caso ele não exista
print("Números: ", numeros)
print("Números distintos: ", conjunto)
print('--------------------------------')

# removendo elementos de um set com remove
nums = set([1, 2, 2, 3, 3, 3])
nums.remove(2)  # caso não exista o elemento retorna um erro
print("Números: ", nums)
print('--------------------------------')

# removendo elementos de um set com discard
nums = set([1, 2, 2, 3, 3, 3])
nums.discard(4)  # caso não exista o elemento nao retorna erro, ignora
nums.discard(2)
print("Numeros: ", nums)
print('--------------------------------')

# removendo todos os elementos de uma vez
nums = set([1, 2, 2, 3, 3, 3])
print("Números: ", nums)
nums.clear()
print("Números: ", nums)
print('--------------------------------')

# ========== OPERAÇÕES MATEMÁTICAS COM SETS
# União de conjuntos (union)
A = {0, 1, 3, 5, 7, 9}
B = {0, 2, 4, 6, 8}
C = A.union(B)
print(C)
print('--------------------------------')

# ou utilizando |
A = {0, 1, 3, 5, 7, 9}
B = {0, 2, 4, 6, 8}
C = A | B
print(C)
print('--------------------------------')

# Interesecção de conjuntos (intersect)
A = {0, 1, 3, 5, 7, 9}
B = {0, 2, 4, 6, 8}
C = A.intersection(B)
print(C)
print('--------------------------------')

# ou utilizando &
A = {0, 1, 3, 5, 7, 9}
B = {0, 2, 4, 6, 8}
C = A & B
print(C)
print('--------------------------------')

# Inicialização de um set
planetas = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(planetas)

# Associação in em sets
print('Ceres' in planetas)
print('Lua' in planetas)
print('Eris' not in planetas)
print("-------------------------------")

# Casting
astros = ['Lua', 'Vênus', 'Sirius', 'Marte', 'Lua']
print(astros)
astrosSet = set(astros)
print(astrosSet)
print("-------------------------------")

# ========== COMPARAÇÃO DE REGISTROS
# Utilizando == e !=
planetas1 = {'Terra', 'Vênus', 'Mercúrio', 'Marte'}
planetas2 = {'Terra', 'Vênus', 'Mercúrio', 'Marte', 'Saturno'}
print(planetas1 == planetas2)
print(planetas1 != planetas2)
print("-------------------------------")

# < Verifica se o conjunto à esquerda é um subconjunto da direta
planetas1 = {'Terra', 'Vênus', 'Mercúrio'}
planetas2 = {'Terra', 'Mercúrio', 'Vênus', 'Saturno', 'Marte'}
print(planetas1 < planetas2)
print("-------------------------------")

# diference ou - :A diferença entre dois conjuntos é um conjunto contendo os elementos do
# conjunto à esquerda que não estão no conjunto à direita do operador.
planetas1 = {'Vênus', 'Mercúrio', 'Terra', 'Netuno', 'Marte'}
planetas2 = {'Terra', 'Júpiter', 'Urano', 'Saturno', 'Marte'}
print(planetas1 - planetas2)
print(planetas1.difference(planetas2))
print("-------------------------------")

# diferença simétrica - apenas os itens não-repetidos
planetas1 = {'Vênus', 'Mercúrio', 'Terra', 'Netuno', 'Marte'}
planetas2 = {'Terra', 'Júpiter', 'Urano', 'Saturno', 'Marte'}
print(planetas1 ^ planetas2)
print(planetas1.symmetric_difference(planetas2))
print("-------------------------------")

# Conjuntos disjuntos: não possuem nenhum elemento em comum
planetas1 = {'Vênus', 'Mercúrio', 'Terra', 'Netuno', 'Marte'}
planetas2 = {'Terra', 'Júpiter', 'Urano', 'Saturno', 'Marte'}
planetas3 = {'Júpiter', 'Urano', 'Saturno'}
print(planetas1.isdisjoint(planetas2))
print(planetas1.isdisjoint(planetas3))
print("-------------------------------")

# União com o |= ou com o método update().
# Realiza uma operação de união, mas ordenando aleatoriamente
planetas1 = {'Vênus', 'Mercúrio', 'Terra', 'Netuno', 'Marte'}
planetas2 = {'Terra', 'Júpiter', 'Urano', 'Saturno', 'Marte'}
planetas1 |= planetas2
# planetas1.update(planetas2)  # descomente para testar este também
print(planetas1)
print("-------------------------------")

# Copiando conjuntos
p1 = {'Vênus', 'Mercúrio', 'Terra', 'Netuno', 'Marte'}
p2 = p1.copy()
print('Conjunto 1:', p1)
print('Conjunto 2:', p2)
print("-------------------------------")

# pop() remove um elemento arbitrário
planetas = {'Mercúrio', 'Vênus', 'Terra', 'Marte'}
print(planetas)
planetas.pop()  # remove um elemento arbitrário.
print(planetas)
