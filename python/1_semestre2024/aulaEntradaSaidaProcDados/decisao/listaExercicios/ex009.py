# 9. Dadas três notas (AV1, AV2 e AV3), fazer um algoritmo que calcule a media. A média consiste em descartar a menor nota entre as 3 médias calculando a média simples das outras duas. Exibir se o aluno está “Aprovado” ou “Reprovado” (média menor do que 6).
n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))
n3 = float(input("nota 3: "))
if (n1 > n2 > n3):
    media = (n1 + n2)/ 2
    print(f"Média: {media}")
    if media >= 6:
        print("Status: APROVADO")
    else:
        print("Status: REPROVADO ")
elif n1 > n3 > n2:
    media = (n1 + n3) / 2
    print(f"Média: {media}")
    if media >= 6:
        print("Status: APROVADO")
    else:
        print("Status: REPROVADO")
elif n2 > n1 > n3:
    media = (n2 + n1) / 2
    print(f"Média: {media}")
    if media >= 6:
        print("Status: APROVADO")
    else:
        print("Status: REPROVADO")
elif n2 > n3 > n1:
    media = (n2 + n3) / 2
    print(f"Média: {media}")
    if media >= 6:
        print("Status: APROVADO")
    else:
        print("Status: REPROVADO")
elif n3 > n1 > n2:
    media = (n3 + n1) / 2
    print(f"Média: {media}")
    if media >= 6:
        print("Status: APROVADO")
    else:
        print("Status: REPROVADO")
elif n3 > n2 > n1:
    media = (n3 + n2) / 2
    print(f"Média: {media}")
    if media >= 6:
        print("Status: APROVADO")
    else:
        print("Status: REPROVADO")
elif (n1 == n2) and n1 > n3:
    media = (n1 + n2)/ 2
    print(f"Média: {media}")
    if media >= 6:
        print("Status: APROVADO")
    else:
        print("Status: REPROVADO ")
elif (n1 == n3) and n1 > n2:
    media = (n1 + n3)/ 2
    print(f"Média: {media}")
    if media >= 6:
        print("Status: APROVADO")
    else:
        print("Status: REPROVADO ")
elif (n2 == n3) and n2 > n1:
    media = (n2 + n3)/ 2
    print(f"Média: {media}")
    if media >= 6:
        print("Status: APROVADO")
    else:
        print("Status: REPROVADO ")
elif n1 == n2 == n3:
    media = (n2 + n3)/ 2
    print(f"Média: {media}")
    if media >= 6:
        print("Status: APROVADO")
    else:
        print("Status: REPROVADO ")
