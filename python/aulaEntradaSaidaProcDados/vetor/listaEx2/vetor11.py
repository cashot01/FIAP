# exercicio inverte_vetor , onde o v2 recebe o v1 ao contrário
import os
os.system("cls")

def inverte_vetor(v1:list, v2:list) -> None:
    v2 = [v1[4], v1[3], v1[2], v1[1], v1[0]] 
    print(f"""
    vetor 1: {v1}
    vetor 2: {v2}""")




v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]
print(f"""
    vetor 1: {v1}
    vetor 2: {v2}""")

inverte_vetor(v1, v2)

