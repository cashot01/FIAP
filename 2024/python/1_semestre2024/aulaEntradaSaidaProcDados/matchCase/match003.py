# 3 dados 2 nº , digitar algum sina de operação e mostrar o resultado
import os 
os.system('cls') 

n1 = float(input("n1: "))
n2 = float(input("n2: "))
operacao = str(input("Operações: +, -, *, %, **, //: "))

match operacao:
    case "+":
        soma = n1 + n2
        print(soma)
    case "-":
        menos = n1 - n2
        print(menos)
    case "*":
        veses = n1 * n2
        print(veses)
    case "%":
        modulo = n1 % n2
        print(modulo)
    case "**":
        exponencial = n1 ** n2
        print(exponencial)
    case "//":
        divInteira = n1 // n2
        print(divInteira)