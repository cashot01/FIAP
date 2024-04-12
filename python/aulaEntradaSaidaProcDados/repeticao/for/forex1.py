# peça 2 nº e exiba em ordem crescente
n1 = int(input("n1: "))
n2 = int(input("n2: "))

for crescente in range(n1, n2 + 1, 1):
    print(crescente)

for decrescente in range(n2, n1 + 1 , 1):
    print(decrescente)