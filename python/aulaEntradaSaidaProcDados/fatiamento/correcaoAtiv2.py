import os
os.system("cls")

def eh_inteiro(s: str) -> bool:
    digito = "0123456789"
    valido = True
    if s[0] == "-" or s[0] == "+" or s[0] in digito:
        for i in range(1, len(s)):
            if s[i] not in digito:
                valido = False
                break
    else:
        valido = False

    return valido
    

print(eh_inteiro("234"))