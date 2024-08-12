import os
os.system("cls")
# Try - tratamento de excessões ou tratamento de erros
"""
try:
    comandos a serem executados
except:
    excessões # erros
else:
    caso não ocorra erro
finally:
    executa com ou sem erro encontrado
"""

"""
Erro:
Compilação: Programador
Execução: Usuário
Circunstancial: Sistema
para os dois últimos o try consegue lidar
"""

# try:
#     nota = float("nota: ")
#     print(nota)
# except:
#     print("Ocorreu um erro")

# x = 8 /0
# x = float(input())

try:
    print("dividindo valores")
    valor1 = float(input("Valor 1: "))
    valor2 = float(input("Valor 2: "))
    divisao = valor1 / valor2
    print(f" divisão: {divisao}")
except ValueError as erroValorErrado:
    print(erroValorErrado)
except ZeroDivisionError:
    print("não existe divisão por 0")
except:
    print("Ocorreu algum erro")
else:
    print("Resultado exibido")
finally:
    print("Obrigado por usar nosso sistema")