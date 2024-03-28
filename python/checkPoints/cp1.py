import os
os.system("cls")
# salarioMin  = 1302
# salario = float(input("Salario: R$ "))
# if salario > 0:
#     faltas = int(input("Qtd. de faltas: "))
#     if salario <= (salarioMin * 2):
#         reajuste = salario + (salario * 0.06)
#         print(f"Salário: {salario}")
#         print(f"Salario reajustado...: {reajuste:.2f}")

#         if faltas <= 0:
#             bonus = 1000
#             print(f"Bônus.: {bonus:.2f}")
#         else:
#             bonus = 0
#             print(f"Bônus.: {bonus:.2f}")

#     elif salario <= (salarioMin * 5):
#         reajuste = salario + (salario * 0.04)
#         print(f"Salário: {salario}")
#         print(f"Salario reajustado...: {reajuste:.2f}")

#         if faltas <= 0:
#             bonus = 1000
#             print(f"Bônus.: {bonus:.2f}")
#         else:
#             bonus = 0
#             print(f"Bônus.: {bonus:.2f}")

#     else:
#         reajuste = salario + (salario * 0.02)
#         print(f"Salário: {salario}")
#         print(f"Salario reajustado...: {reajuste:.2f}")

#         if faltas <= 0:
#             bonus = 1000
#             print(f"Bônus.: {bonus:.2f}")
#         else:
#             bonus = 0
#             print(f"Bônus.: {bonus:.2f}")
# else:
#     print("Salario INVALIDO")

# Leitura do salário
salario = float(input("Salário: "))

# Verificação se o salário é negativo ou não
if salario >= 0:
    # O salário não é negativo
    # ------------------- Resolvendo o problema do reajuste
    ate2sm = 1302 * 2
    ate5sm = 1302 * 5
    if salario <= ate2sm:
        salario_reajustado = salario * 1.0645 # 6.45%
    elif salario <= ate5sm:
        salario_reajustado = salario * 1.0455 # 4.55%
    else:
        salario_reajustado = salario * 1.0289 # 2.89%

    # -------------------- Resolvendo o problema das faltas
    # Leitura das faltas
    faltas = int(input("Faltas: "))
    # Verificação se há faltas
    if faltas <= 0:
        bonus = 1000
    else:
        bonus = 0
    
    # Exibição do relatório solicitado
    print(f"""
    Salário.............: {salario:.2f}
    Salário reajustado..: {salario_reajustado:.2f}
    Bonus...............: {bonus:.2f}
    """)
else:
    # O salário é negativo
    print("ERRO! Digite um salário positivo!")