""" 12. Dada a tabela de cálculo do IR:
Salário-de-contribuição (R$)                            Alíquota                               Dedução (R$)
até 1.710,78                                               isento                               0
de 1.710,79 até 2.563,91                                     7,5%                               128,31
de 2.563,92 até 3.418,59                                     15%                                320,60
de 3.418,60 até 4.271,59                                    22,5%                               577,00
Acima de 4.271,59                                           27,5%                               790,58
Fazer um algoritmo que leia o salário do contribuinte e calcule quanto ele terá que pagar de
Imposto de Renda (IR).
"""
salario = float(input("Salário: R$ "))
if salario <= 1710.78:
    impostoRend = 0
    print(f"Imposto de Renda: Isento")
elif salario <= 2563.91:
    impostoRend = (salario * 0.925) - 128.31
    print(f"Imposto Renda: R$ {impostoRend:.2f}")
elif salario <= 3418.59:
    impostoRend = (salario * 0.85) - 320.60
    print(f"Imposto Renda: R$ {impostoRend:.2f}")
elif salario <= 4271.59:
    impostoRend = (salario * 0.775) - 577
    print(f"Imposto de Renda: R$ {impostoRend:.2f}")
else:
    impostoRend = (salario * 0.725) - 790.58
    print(f"Imposto de Renda: {impostoRend}")