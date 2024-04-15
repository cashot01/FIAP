"""
EXERCÍCIO COMPLETO
Uma turma tem 10 alunos.
Um professor desenvolveu uma rotina para ter um melhor gerenciamento o
dos alunos.
A média anual se dá por:
- Checkpoint:
    - São 3 avaliações
    - Calcula-se a média comum das duas maiores notas
    - Vale 20% da média final
- Challenge:
    - São 2 sprints
    - O cálculo é a média simples das duas notas
    - Vale 20% da média final
- Global solution:
    - Apenas uma nota que
    - Vale 60% da média final.
Requisitos:
- A média final para passar é ao menos 6, senão estará reprovado
- Toda vez que for digitada uma nota inválida (fora de 0 e 10), advertir
  e pedir novamente a digitação da mesma nota.
Relatório:
- para cada aluno exibir as médias calculadas e se ele está aprovado ou não.
- no final da digitação das notas dos dez alunos, exibir:
    - quantos foram aprovados
    - quantos foram reprovados
    - quantos tiraram a media final maxima (nota 10)
"""
import os
os.system("cls")
# inicializando variaveis contatadoras
reprovado = 0
aprovado = 0
media_maxima = 0

# iniciando laço com 10 alunos
for i in range(1, 4, 1):
    os.system("cls")

    # Digitando Checkpoint
    print(f"Aluno {i}")
    print("----------Checkpoint----------")
    cp1 = float(input("Checkpoint 1: "))
    while cp1 < 0 or cp1 > 10:
        print("Erro! Digite uma nota valida")
        cp1 = float(input("Checkpoint 1: "))
    cp2 = float(input("Checkpoint 2: "))
    while cp2 < 0 or cp2 > 10:
        print("Erro! Digite uma nota valida")
        cp2 = float(input("Checkpoint 2: "))
    cp3 = float(input("Checkpoint 3: "))
    while cp3 < 0 or cp3 > 10:
        print("Erro! Digite uma nota valida")
        cp3 = float(input("Checkpoint 3: "))

    menor = cp1
    if cp2 < menor:
        menor = cp2
    if cp3 < menor:
        menor = cp3
    media_Cp = ((cp1 + cp2 + cp3) - menor) / 2
    proporcao_Cp = media_Cp * 0.2


    # Digitando Challenges
    print("----------Challenge----------")
    sp1 = float(input("Sprint 1: "))
    nota_invalida = sp1 < 0 or sp1 > 10

    while nota_invalida:
        print("Erro digite uma nota valida")
        sp1 = float(input("Sprint 1: "))
        nota_invalida = sp1 < 0 or sp1 > 10

    sp2 = float(input("Sprint 2: "))
    nota_invalida = sp2 < 0 or sp2 > 10

    while nota_invalida:
        print("Erro digite uma nota valida")
        sp2 = float(input("Sprint 2: "))
        nota_invalida = sp2 < 0 or sp2 > 10

    media_challenge = (sp1 + sp2) / 2
    proporcao_challenge = media_challenge * 0.2

    # Digitando Global Solution
    print("\n-------Global Solution----------------")
    gs = float(input("Global Solution 1: "))
    while gs < 0 or gs > 10:
        print("Erro digite uma nota valida")
        gs = float(input("Global Solution 1: "))
    proporcao_gs = gs * 0.6

    # exibindo as medias
    print("\n============= M Ê D I A S =====================")
    print(f"Checkpoint........: {media_Cp}")

    print(f"Challenge.........: {media_challenge}")

    print(f"Global Solution...: {gs}")

    # definição de status de cada aluno
    media_final = (proporcao_Cp + proporcao_challenge + proporcao_gs)
    print(f"\n=====> MÉDIA FINAL {media_final:.1f}", end= " ")
    if media_final < 6:
        print(f"Resprovado\n")
    else:
        print(f"Aprovado\n")

    input("digite algo para continuar. . .")

    # consolidação dos dados do relatorio
    if media_final < 6:
        reprovado += 1
    elif media_final >= 6:
        aprovado += 1
        if media_final == 10:
            media_maxima += 1

# exibição do relatorio final
os.system("cls")
print(f"Aprovados....: {aprovado}")
print(f"Reprovados...: {reprovado}")
print(f"Média Maxima..: {media_maxima}")
