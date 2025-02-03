# 3. Fazer um algoritmo que calcule a média de 4 números dados pelo usuário. 
import os
os.system("cls")
n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))
n3 = float(input("nota 3: "))
n4 = float(input("nota 4: "))
media = (n1 + n2 + n3 + n4)/4
print("a média das 4 notas({}, {}, {}, {}) é {:.1f}".format(n1, n2, n3, n4, media))