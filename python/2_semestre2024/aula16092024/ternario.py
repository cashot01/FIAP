import os
os.system("cls" if os.name == "nt" else 'clear')

# operador ternario - substitui o if em situações com else
# onde tenha somente um comando do lado verdadeiro e um comando do lado falso

# sintaxe:
# [<var> =] <comando .v.> if <condicao> else <comando .f.>

"""
Forma 1 - sem utilizar variavel
sintaxe:
[<var> =] <comando .v.> if <condicao> else <comando .f.>
"""
idade = 10
print("maior de idade") if idade >= 18 else print("menor de idade")
# lado verdadeiro                               lado falso

"""
Forma 2 - Com variavel
sintaxe:
[<var> =] <comando .v.> if <condicao> else <comando .f.>
"""
venda = 5000
bonus = 50 if venda > 1000 else 30
print(venda, bonus)

"""
Forma 3 - fazendo parte da conta
sintaxe:
[<var> =] <comando .v.> if <condicao> else <comando .f.>
"""
venda = 1500
desconto = venda - (venda * 0.1 if venda > 1000 else venda * 0.05)
print(venda, desconto)

"""
Exercicio 1:
0 inss é calculado dependendo do salario. Se for acima de 1412, cobra-se 9%, caso contrario 7,5%. faça um programa que mostre o valor calculado do inss

Exercicio 2:
0 inss é calculado dependendo do salario. Se for acima de 1412, cobra-se 9%, caso contrario 7,5%. faça um programa que mostre o valor calculado do inss (salario liquido)
"""
salario = int(input("Salario: "))
inss = (salario * 0.075 if salario < 1412 else 0.09)
print(f"Salario: {salario}, INSS:  {inss}")

salario_Liquido = salario - inss
print(f"Salrio Liquido: {salario_Liquido}")