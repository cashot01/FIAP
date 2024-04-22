# Subalgoritimos - Funções e Procedimentos ===> Métodos
import os
os.system("cls")
import math

# ========================== SUBALGORITIMOS
# Procedimento ==> Subalgoritimo que n retorna valor ao programa chamador
def saudacao1():
    print("Bom dia usuário")

def saudacao2(nome):
    print(f"Bom dia {nome} ")

def saudacao3(nome, hora):
    if hora < 12:
        msg =  "bom dia"
    elif hora < 18:
        msg =  "boa tarde"
    else:
        msg =  "boa noite"
    print(f"{msg}, {nome}")



# Funções ==> Subalgoritimo que retorna valor ao programa chamador




# =========================  PROGRAMA PRINCIPAL
saudacao1()
saudacao2("Cauan") # "Cauan" é um parametro
saudacao3("gustavo", 17)
