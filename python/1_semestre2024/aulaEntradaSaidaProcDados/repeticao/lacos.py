import os
os.system("cls")
"""
ler o nº inicial
ler o nº final
exibir os nº
somar 1 para o proximo
"""
inicial = int(input("valor inicial: "))
final = int(input("valor final: "))

"""
ordem Crescente
while inicial <= final:
    # print(f"{inicial} ", end = "") # end = "" - n pula a linha 
    print(f"{inicial}")
    inicial += 1 
"""

while inicial >= final:
    print(f"{inicial}")
    inicial -= 1
