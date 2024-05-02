# exercicio ordena_ordem_crescente, coloca em ordem crescente
import os
os.system("cls")

def ordena_ordem_crescente(v1:list) -> None :
    v1 = [v1[3], v1[4], v1[2], v1[0], v1[1]]
    print(f"""\n ordem Crescente: 
            {v1}""")


#      0,  1,  2,  3, 4
v1 = [41, 72, 39, 4, 35]
print(f"{v1}")

ordena_ordem_crescente(v1)