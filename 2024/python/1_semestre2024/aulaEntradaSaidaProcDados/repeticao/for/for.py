# fazer um programa que some nº ate que seja digitado zero
import os
os.system("cls")

soma = 0

for volta in range(1, 10,1):
    num = float(input(f"{volta}º nº: "))
    soma += num

print(f"Somatoria: {soma}")

# soma = 0

# while True:
#     num = float(input("Nº ou 0 para finalizar: "))
#     if num == 0:
#         break
#     soma += num

# print(f"Somatória: {soma}")