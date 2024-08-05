import os
os.system("cls")

"""
frase = "O Palmeiras e o Corinthias perderam"
print("1. " + frase)
print("2. " + frase[2])
print("3. " + frase[7:15])
print("4. " + frase[::-1])
print("5. " + frase[5:25:2])
print("6. " + frase[30:3:-5])

"""



"""
# metodo find(), procura uma substring em uma string retornando o seu indice ou -1 se não encontrar
frase = "O Palmeiras e o Corinthias perderam"
print(frase.find("Palmeiras")) # caso encontre
print(frase.find("Tricolor")) # caso n encontre -1

if frase.find("z") == -1:
    print("Essa letra n existe nessa frase")
else:
    print("Letra existe na frase")

print(frase.find(" ", 5, 10)) # inicio e fim tbm 

"""

"""
# metodo join() transforma uma lista de strings em uma string
# só funciona com strings
lista_nome = ["Edson", "de", "Oliveira"]
print(lista_nome)
# new_lista = " ".join(lista_nome)
print(len(" ".join(lista_nome)))


"""

"""
# metodo split() pega uma string e gera uma lista
nome = "Edson de Oliveira está numa seginda feira para o 1tdspi"
print(nome.split())
print(nome.split("e"))
# separa pelo "e" e o "e" é retirado da lista
print(nome.split("de"))

"""
# replace(procura, troca, count) troca carcteres especifos da lista
# procura - palavra q quero trocar
# troca - nova palavra 
# count - quantas vezes vai fazer

# strip() elimina os espaços antes e depois " Cauan " --> "Cauan"



