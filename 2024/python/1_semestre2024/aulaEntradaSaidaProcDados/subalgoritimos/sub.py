# ========================== SUBALGORITIMOS
# Procedimento ==> Subalgoritimo que n retorna valor ao programa chamador
# -> none é o tipo de dado que volta nesse caso não volta nada
def saudacao1() -> None:
    print("Bom dia usuário")

def saudacao2(nome: str) -> None:
    print(f"Bom dia {nome} ")

def saudacao3(nome: str, hora: int) -> None:
    if hora < 12:
        msg =  "bom dia"
    elif hora < 18:
        msg =  "boa tarde"
    else:
        msg =  "boa noite"
    print(f"{msg}, {nome}")



# Funções ==> Subalgoritimo que retorna valor ao programa chamador
def raiz2(num: float) -> float:
    resp = num ** (1/2)
    return resp

def raizn(num: float, raiz: int) -> float:
    return num ** (1/raiz)

def pi() -> float:
    return 3.1415


