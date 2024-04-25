import os
os.system("cls")
# Calcular equação do 2º grau usando baskara
# delta = b**2 - 4*a*c
# x1 = ((-b + (delta**(1/2)) ) / (2*a) )
# x2 = ((-b - (delta**(1/2)) ) / (2*a))

#----------------- Condições
# se A == 0 - Equação 1º Grau
# se delta < 0 - não é possivel
# se delta == 0 - 2 raizes iguais
# se delta > 0 - 2 raizes diferentes


aZero = 0
deltaNegativa = 0
deltaZero = 0
deltaPositiva = 0

for i in range(1, 6, 1):

    print(f"\n Volta:  {i}")
    a = int(input("digite o valor de a: "))
    if a == 0:
        print(f"Valor de a({a}) = 0,  essa equação virou do 1º grau")
        aZero += 1
        continue
    # else:
    #   print("continua")  

    b = int(input("digite o valor de b: "))
    c = int(input("digite o valor de c: "))

    delta = (b ** 2) -(4*a*c)

    if delta < 0:
        print(f"Não é possível, valor de delta({delta}) < 0")
        deltaNegativa += 1
        continue

    elif delta == 0:
        print(f"Delta({delta} == 0,  tem 2 raizes iguais)")
        deltaZero += 1
        

    else:
        print(f"Delta({delta} > 0, tem 2 raizes diferentes)")
        deltaPositiva += 1
        # continue
        
    x1 = (-b + (delta ** (1/2)) / (2 * a))
    x2 = (-b - (delta ** (1/2)) / (2 * a))

    print(f"""
        Delta: {delta}
        x1...: {x1}
        x2...: {x2}""")

    
    
    # input("digite algo para continuar... ")


    
    
    
porcentagem_aZero = (aZero / i) * 100
porcentagem_deltaNegativa = (deltaNegativa / i) * 100
porcentagem_deltaZero = (deltaZero / i) * 100
porcentagem_deltaPositiva = (deltaPositiva / i) * 100


    
print(f"""\n-------------------- Porcentagens --------------------------
    A Zero........: {porcentagem_aZero} %
    delta negativo: {porcentagem_deltaNegativa} %
    delta zero....: {porcentagem_deltaZero} %
    delta positivo: {porcentagem_deltaPositiva} %""")
    



