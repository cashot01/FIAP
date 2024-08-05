# 8. Dado um número pelo usuário, verifique se ele é “Positivo”, “Negativo” ou “Nulo”(igual a zero).
num = float(input("nº: "))
if num > 0:
    print("Nº POSITIVO")
elif num < 0:
    print("Nº Negativo")
else:
    print("Nº NULO")