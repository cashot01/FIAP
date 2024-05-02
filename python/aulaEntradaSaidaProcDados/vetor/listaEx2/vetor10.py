# exercicio 10 - fazer procedimento copia_vetor, onde copia o vetor 1 no vetor2
import os
os.system("cls")
def copia_vetor(v1:list, v2:list) -> int:
    v2 = [v1[0], v1[1], v1[2], v1[3], v1[4]]
    print(f"""
    vetor 1: {v1}
    vetor 2: {v2}""")




v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]
print(f"""
    vetor 1: {v1}
    vetor 2: {v2}""")

copia_vetor(v1, v2)

