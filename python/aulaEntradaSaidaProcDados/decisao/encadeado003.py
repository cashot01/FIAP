# 3. Dadas 3 notas, calcular a média simples das dus maiores.
n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))
n3 = float(input("nota 3: "))
if n1 > n2 > n3:
    print(f"""
        maior nota...: {n1}
        2ª maior nota: {n2}""")
    maiornota = n1
    segundanota = n2
    media = (n1 + n2)/ 2
    print(f"Media: {media}")

elif n1 > n3 > n2:
    print(f"""
        maior nota...: {n1}
        2ª maior nota: {n3}""")
    maiornota = n1
    segundanota = n3
    media = (n1 + n3)/ 2
    print(f"Media: {media}")

elif n2 > n1 > n3:
    print(f"""
        maior nota...: {n2}
        2ª maior nota: {n1}""")
    maiornota = n2
    segundanota = n1
    media = (n2 + n1)/ 2
    print(f"Media: {media}")

elif n2 > n3 > n1:
    print(f"""
        maior nota...: {n2}
        2ª maior nota: {n3}""")
    maiornota = n2
    segundanota = n3
    media = (n2 + n3)/ 2
    print(f"Media: {media}")

elif n3 > n1 > n2:
    print(f"""
        maior nota...: {n3}
        2ª maior nota: {n1}""")
    maiornota = n3
    segundanota = n1
    media = (n3 + n1)/ 2
    print(f"Media: {media}")

elif n3 > n2 > n1:
    print(f"""
        maior nota...: {n3}
        2ª maior nota: {n2}""")
    maiornota = n3
    segundanota = n2
    media = (n3 + n2)/ 2
    print(f"Media: {media}")
