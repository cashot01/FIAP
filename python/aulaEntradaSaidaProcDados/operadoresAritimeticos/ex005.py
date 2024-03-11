#5. Dado o preço do maço de cigarros, a quantidade de maços consumidos por dia e o tempo em anos que a pessoa fuma, calcular quanto esta pessoa gastou com cigarros.
import os
os.system("cls")

preco = float(input("preço do maço: "))
macos = int(input("quantidade maços: "))
tempo = int(input("anos fumando: "))
gasto = preco * macos * 365 * tempo
print("o gasto dos cigarros foram: R${:.2f}".format(gasto))