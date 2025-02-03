import os
os.system("cls")

def exibe_vetor(v: list) -> None:
    for i in range(0, len(v), 1):
        print(f"{i} => {v[i]}")

def preenche_lista(l: list) -> None:
    while True:
        elem = input("Elemento: ")
        if elem != ".":
            l.append(elem)
        else:
            break
        


# ================== Programa Principal

# vetor = [54, 34, 23, 14, 67]
# exibe_vetor(vetor)

# lista = []
# preenche_lista(lista)
# print(lista)

nome = "Edson de Oliveira"
print(nome[7])