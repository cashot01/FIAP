import os
os.system("cls")
salarioMin  = 1302
salario = float(input("Salario: R$ "))
if salario > 0:
    faltas = int(input("Qtd. de faltas: "))
    if salario <= (salarioMin * 2):
        reajuste = salario + (salario * 0.06)
        print(f"Salário: {salario}")
        print(f"Salario reajustado...: {reajuste:.2f}")

        if faltas <= 0:
            bonus = 1000
            print(f"Bônus.: {bonus:.2f}")
        else:
            bonus = 0
            print(f"Bônus.: {bonus:.2f}")

    elif salario <= (salarioMin * 5):
        reajuste = salario + (salario * 0.04)
        print(f"Salário: {salario}")
        print(f"Salario reajustado...: {reajuste:.2f}")

        if faltas <= 0:
            bonus = 1000
            print(f"Bônus.: {bonus:.2f}")
        else:
            bonus = 0
            print(f"Bônus.: {bonus:.2f}")

    else:
        reajuste = salario + (salario * 0.02)
        print(f"Salário: {salario}")
        print(f"Salario reajustado...: {reajuste:.2f}")

        if faltas <= 0:
            bonus = 1000
            print(f"Bônus.: {bonus:.2f}")
        else:
            bonus = 0
            print(f"Bônus.: {bonus:.2f}")
else:
    print("Salario INVALIDO")