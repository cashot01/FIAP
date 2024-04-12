# 3 - 2 nº e digite C ou D para mostar a ordem

n1 = int(input("n1: "))
n2 = int(input("n2: "))
ordem = str(input("<C>rescente ou <D>ecrescente: "))

if ordem == "C":
    for crescente in range(n1, n2 + 1, 1):
        print(crescente)

    for decrescente in range(n2, n1 + 1 , 1):
        print(decrescente)

elif ordem == "D":
    for decrescente in range(n1, n2 -1 , -1):
        print(decrescente)

    for decrescente in range(n2, n1 -1 , -1):
        print(decrescente)

else:
    print("opção invalida")

# if (n1 < n2):
#     for crescente in range(n1, n2 + 1, 1):
#         print(crescente)
# else:
#     for decrescente in range(n1, n2 -1 , -1):
#         print(decrescente)