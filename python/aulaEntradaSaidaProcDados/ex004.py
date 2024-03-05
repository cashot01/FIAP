# 4. Dada a quilometragem parcial de um carro (km) e a quantidade de litros (l) gastos para percorrer esta quilometragem, fazer um algoritmo que calcule quantos Km/l o carro consumiu.
import os
os.system("cls")
km = float(input("quantos kms: "))
litros = float(input("quantos litros: "))
autonomia = km / litros
print(f"o automóvel tem autonomia de {autonomia:.2f} km/l")