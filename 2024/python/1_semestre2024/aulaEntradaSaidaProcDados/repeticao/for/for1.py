"""
Dada uma tabuada e até qual numero deve ser multiplicado, mostre no formato "tia maria Yolanda".
Tabuada: 5
até qual mult:4
5 x 1 = 5
5 x 2  = 10
5 x 3 = 15
5 x 4 = 20
"""

tab = int(input("nº: "))
for i in range(tab, tab * 4 + 1, tab):
    print(i)