# 13. Juntar os dois exercícios anteriores, ou seja, pedir a digitação do Salário Bruto e calcular o INSS e IR devido. Exibir o Salário Bruto, INSS, IR e Salário Líquido.
import os
os.system("cls")
salario = float(input("Salário: R$ "))
if salario <= 1247.70:
    inss = salario * 0.08
    impostoRenda = 0
    salarioLiquido = salario * 0.92
    print(f"""
            Salário Bruto...: R$ {salario}
            INSS............: R$ {inss:.2f}
            Imposto de Renda: R$ {impostoRenda:.2f}
            Salário Líquido.: R$ {salarioLiquido:.2f}""")
elif salario <= 2079.50:
    inss = salario * 0.09
    impostoRenda = (salario * 0.075) - 128.31
    salarioLiquido = salario - (inss + impostoRenda)
    print(f"""
            Salário Bruto...: R$ {salario}
            INSS............: R$ {inss:.2f}
            Imposto de Renda: R$ {impostoRenda:.2f}
            Salário Líquido.: R$ {salarioLiquido:.2f}""")
    
elif salario >= 2563.92 and salario <= 3418.59:
    inss = salario * 0.11
    impostoRenda = (salario * 0.15) - 320.60
    salarioLiquido = salario - (inss + impostoRenda)
    print(f"""
            Salário Bruto...: R$ {salario}
            INSS............: R$ {inss:.2f}
            Imposto de Renda: R$ {impostoRenda:.2f}
            Salário Líquido.: R$ {salarioLiquido:.2f}""")

elif salario <= 4159:
    inss = (salario * 0.11)
    impostoRenda = (salario * 0.225) - 577
    salarioLiquido = salario - (inss + impostoRenda)
    print(f"""
            Salário Bruto...: R$ {salario}
            INSS............: R$ {inss:.2f}
            Imposto de Renda: R$ {impostoRenda:.2f}
            Salário Líquido.: R$ {salarioLiquido:.2f}""")
    
elif salario <= 4271.59: 
    inss = 468
    impostoRenda = (salario * 0.225) - 577
    salarioLiquido = salario - (inss + impostoRenda)
    print(f"""
            Salário Bruto...: R$ {salario}
            INSS............: R$ {inss:.2f}
            Imposto de Renda: R$ {impostoRenda:.2f}
            Salário Líquido.: R$ {salarioLiquido:.2f}""")
    
elif salario >= 4271.60:
    inss = 468
    impostoRenda = (salario * 0.275) - 790.58
    salarioLiquido = salario - (inss + impostoRenda)
    print(f"""
            Salário Bruto...: R$ {salario}
            INSS............: R$ {inss:.2f}
            Imposto de Renda: R$ {impostoRenda:.2f}
            Salário Líquido.: R$ {salarioLiquido:.2f}""")
    
