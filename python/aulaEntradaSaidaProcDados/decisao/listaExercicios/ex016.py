"""
16. Dado o salário de uma pessoa, sexo (1 para Masculino e 2 para Feminino) e idade, verificar a tabela abaixo e calcular a devida cobrança de convênio médico sobre o salário informado:
Idade                        Masculino                 Feminino
Até 20 anos                     5,34%                   3,56%
Acima de 20 até 40 anos         8,44%                   6,43%
Acima dos 40 anos               10,12%                  8,02%
"""
import os 
os.system("cls")
salario = float(input("Salário: R$ "))
idade = int(input("Idade: "))
sexo = int(input("""
                    qual seu sexo ?
                 [1] Masculino
                 [2] Feminino
"""))
if idade <= 20 and sexo == 1:
    convenio = salario * 0.0534
    print(f"Cobrança do convênio: R$ {convenio}")

elif idade <= 20 and sexo == 2:
    convenio = salario * 0.0356
    print(f"Cobrança do convênio: R$ {convenio}")

elif idade <= 40 and sexo == 1:
    convenio = salario * 0.0844
    print(f"Cobrança do convênio: R$ {convenio}")

elif idade <= 40 and sexo == 2:
    convenio = salario * 0.0643
    print(f"Cobrança do convênio: R$ {convenio}")

elif idade > 40 and sexo == 1:
    convenio = salario * 0.1012
    print(f"Cobrança do convênio: R$ {convenio}")

else:
    convenio = salario * 0.0802
    print(f"Cobrança do convênio: R$ {convenio}")