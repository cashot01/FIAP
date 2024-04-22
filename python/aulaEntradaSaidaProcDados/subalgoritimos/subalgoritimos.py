# Calcular a equação de 2 grau por baskara
# Subalgoritimos - Funções e Procedimentos ===> Métodos
import os
os.system("cls")

# ========================== SUBALGORITIMOS
# Procedimento ==> Subalgoritimo que n retorna valor ao programa chamador




# Funções ==> Subalgoritimo que retorna valor ao programa chamador
def calcular_delta(aa, bb, cc): # aa -1 | bb 2 | cc 3
    resp = bb ** 2 - 4 * aa * cc
    return resp



# =========================  PROGRAMA PRINCIPAL
a = float(input("a: ")) # -1
b = float(input("b: ")) # 2
c = float(input("c: ")) # 3

delta =  calcular_delta(a, b, c)
print(delta)