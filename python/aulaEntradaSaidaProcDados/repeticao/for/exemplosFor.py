# exemplos de aplicação do laço for
import os
os.system("cls")

# valor inicial,  valor final(até um nº antes) e incremento
# for volta in range(0, 10, 1):
#     print(f"{volta}", end = " ")

num = int(input("nº: "))
for volta in range(num, num * 10 + 1, num ):
    print(f"{volta}", end= " ")