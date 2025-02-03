""" 11. Dada a tabela de cálculo do INSS:
                Salário Alíquota para fins de recolhimento ao INSS (%)
                                                            
até 1.247,70                         8,00
de 1.247,71 até 2.079,50             9,00
de 2.079,51 até 4.159,00             11,00
Acima de 4.159,00                   Cobrar teto de 468,00
Fazer um algoritmo que leia o salário do contribuinte e calcule quanto ele irá pagar de INSS. """
salario = float(input("Salário: "))
if salario <= 1247.70:
    inss = (salario * 0.08)
    print(f"INSS: R$ {inss:.2f}")
elif salario <= 2079.50:
    inss = salario * 0.09
    print(f"INSS: R$ {inss:.2f}")
elif salario <= 4159:
    inss = salario * 0.11
    print(f"INSS: R$ {inss:.2f}")
else: 
    inss = 468
    print(f"INSS: R$ {inss:.2f}")