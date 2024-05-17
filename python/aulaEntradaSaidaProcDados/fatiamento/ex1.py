import os
os.system("cls")

def vogal_maiuscula(s: str) -> str:
    vogal = "aeiou"
    for i in range(len(s)):
        if s[i] in vogal:
            s = s.replace(s[i], s[i].upper())
    
    return s






#--------------------------------------- Programa Principal
texto = "Edson de Oliveira"
new_texto = vogal_maiuscula(texto)
print(new_texto)