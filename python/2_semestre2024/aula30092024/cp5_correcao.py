import os
os.system("cls")

#--------- Verificar se um login é valido
def login_valido(l: str) -> bool:
    digito = "01234567890"
    if len(l) != 6:
        return False
    else:
        if l[0] not in digito:
            return False
        else:
            letra = "ABCDEFGHIJKLMNOPQRSTUVXWYZ"
            achou = False
            for i in range(1, 6, 1):
                if l[i].upper() in letra:
                    achou = True
                    break
            return achou
        


# verificar senha valida
def senha_valida(s: str) -> bool:
    if len(s) < 6:
        return False
    else:
        letra = "ABCDEFGHIJKLMNOPQRSTUVXWYZ"
        if s[0].upper() not in letra:
            return False
        else:
            digito = "01234567890"
            achou = False
            for i in range(1, len(s), 1):
                if s[i] in digito:
                    achou = True
                    break
            return achou
        

# -------- Processa o arquivo dependendo do modo de abertura
def processa_arquivo(nome_arquivo: str, modo_abertura: str) -> None:
    match modo_abertura:
        case "a":
            # Gravação do login e senha validados no arquivo
            with open(nome_arquivo, modo_abertura, encoding="UTF-8") as arq:
                arq.write(f"{login}, {senha}")