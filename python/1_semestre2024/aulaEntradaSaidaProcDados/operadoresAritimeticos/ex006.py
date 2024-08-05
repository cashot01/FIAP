# 6. Um caixa eletrônico dispensa cédulas de 50, 20 e 10 reais. Considerando que a quantia já seja múltipla de 10, fazer um algoritmo que exiba um relatório com quantas cédulas de cada são necessárias para compor a quantia. 
import os 
os.system("cls")

quantia = int(input("quantidade: "))
ced50 = quantia // 50
quantia = quantia % 50
ced20 = quantia // 20
quantia = quantia % 20
ced10 = quantia // 10
print("cedulas de 50: {}".format(ced50))
print("cedulas de 20: {}".format(ced20))
print("cedulas de 10: {}".format(ced10))