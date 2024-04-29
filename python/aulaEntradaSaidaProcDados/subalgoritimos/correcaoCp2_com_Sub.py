# ================================== SUBALGORITIMOS
def cadastrar_candidatos(c: list) -> None: 
    # None indica um procedimento (n retorna valor)
    print("digite os nomes dos candidatos:")
    for i in range(3):
        c[i] = input(f"{i + 1}: ")

def exibir_menu(c: list):
     print(f""" CANDIDATOS:
        1 - {c[0]}
        2 - {c[1]}
        3 - {c[2]}
        0 - FIM DA VOTAÇÃO """)
     
def contagem_candidato(candidato: int) -> int:
    return candidato + 1

def calcular_total_votos(c1: int, c2: int, c3: int, c4: int) -> int:
    return c1 + c2 + c3 + c4

def calcular_porcentagem(c1: int, tv: int) -> int:
    return (c1 / tv) * 100

def exibir_apuracao(n1: list, n2: list, n3: list,  c1: int, c2: int, c3: int, cn: int,  p1: float, p2: float, p3: float, pn: float) -> None:
    print(f""" 
    CANDIDATOS
    TOTAL DE VOTOS: {total_votos}
    1 - {n1:15} -> {c1:3d}  votos -> {p1:5.1f}  %
    2 - {n2:15} -> {c2:3d} votos ->  {p2:5.1f} %
    3 - {n3:15} -> {c3:3d} votos ->  {p3:5.1f} %
        {"NULOS":15}       -> {cn} votos     -> {pn:5.1f} % """)






# ================================== PROGRAM PRINCIPAL
import os
os.system("cls")

# Cadastro dos candidatos
candidatos = ["", "", ""]
cadastrar_candidatos(candidatos)





# Votação
# ------------------ Inicio do laço
cand1 = 0
cand2 = 0
cand3 = 0
nulo = 0
while True:
    os.system("cls")
    exibir_menu(candidatos)
   
    
    voto = int(input("VOTO: "))

    match voto:
        case 0:
            break

        case 1:
            cand1 = contagem_candidato(cand1)     # cand1 += 1

        case 2:
            # cand2 += 1
            cand2 = contagem_candidato(cand2)

        case 3:
            # cand3 += 1
            cand3 = contagem_candidato(cand3)

        case _:
            nulo += 1

#----------------- Final do laço

# Apuração

total_votos = calcular_total_votos(cand1, cand2, cand3, nulo)


perc1 = calcular_porcentagem(cand1, total_votos)
perc2 = calcular_porcentagem(cand2, total_votos)
perc3 = calcular_porcentagem(cand3, total_votos)
perc_nulos = calcular_porcentagem(nulo, total_votos)

exibir_apuracao(candidatos[0], candidatos[1], candidatos[2],  cand1, cand2, cand3, nulo, perc1, perc2, perc3, perc_nulos)