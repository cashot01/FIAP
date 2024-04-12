# peça 2 nº exiba em crescente se n1 > n2 ou decrescente se n2> n1

n1 = int(input("n1: "))
n2 = int(input("n2: "))

if (n1 < n2):
    for crescente in range(n1, n2 + 1, 1):
        print(crescente)
else:
    for decrescente in range(n1, n2 -1 , -1):
        print(decrescente)