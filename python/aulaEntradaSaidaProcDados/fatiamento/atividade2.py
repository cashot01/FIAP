

def eh_numero(numero: str) -> bool:
    digitos = "0123456789"
    if numero[0] == "+" or numero[0] == "-":
        for i, carac in enumerate(numero):

            if carac in digitos:
                return numero
            else:
                return False
    return numero
            
            

x = input("x: ")
eh_numero(x)

            
    












