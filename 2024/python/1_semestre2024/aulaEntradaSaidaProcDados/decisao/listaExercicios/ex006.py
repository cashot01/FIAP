# 6. Dada uma nota, verificar se ela é válida, ou seja, se ela estiver entre 0 e 10 (inclusive) ela é uma “Nota válida”, senão “Nota inválida”.
nota = float(input("nota: "))
if nota >= 0 and nota <= 10:
    print("NOTA VALIDA")
else:
    print(" NOTA INVALIDA")