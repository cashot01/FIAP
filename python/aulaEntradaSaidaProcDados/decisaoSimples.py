import os
os.system("cls")
# DECISÃO  SIMPLES
# DEFINIÇÃO: 
# condição : pergunta q retorna verdade(True) ou falso(False)

# exemplo - calcular o modulo da matematica
# |-5 | -> 5

original = int(input("nº: "))
if original < 0:
    num = original * -1
print(f"|{original}| -> {num}")