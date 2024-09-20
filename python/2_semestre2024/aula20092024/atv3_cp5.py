# Cauan Aranega S Passos RM555466
import os
import json
os.system("cls")

# Criação do arquivo dados.txt
with open('dados.txt', 'w') as arq:
    arq.write('12345t, edson@fiap.com.br\n')
    arq.write('01020d, maria@hotmail.com\n')
    arq.write('1abcde, estela@ig.com.br\n')
    arq.write('123abd, vania@terra.com.br\n')

# Inicialização das listas para logins e e-mails
logins = []
emails = []

# Processamento do arquivo dados.txt
with open('dados.txt', 'r') as arq:
    for line in arq:
        login, email = line.strip().split(', ')
        logins.append(login)
        emails.append(email)

# Gravação dos logins em login.txt
with open('login.txt', 'w') as arq:
    for login in logins:
        arq.write(f'{login}\n')

# Gravação dos e-mails em e-mail.txt
with open('e-mail.txt', 'w') as arq:
    for email in emails:
        arq.write(f'{email}\n')

# Exibição dos conteúdos dos arquivos
print("login.txt")
with open('login.txt', 'r') as arq:
    print(arq.read())

print("e-mail.txt")
with open('e-mail.txt', 'r') as arq:
    print(arq.read())

# Criação do dicionário e gravação em arquivo JSON
data = {
    "login": logins,
    "e-mail": emails
}

with open('dados.json', 'w') as arq:
    json.dump(data, arq, indent=4)

# Exibição do arquivo JSON
print("dados.json")
with open('dados.json', 'r') as arq:
    print(arq.read())

    
    


