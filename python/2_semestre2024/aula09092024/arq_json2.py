import json
import os
os.system("cls")

# Criando um dicioinario aninhado
pessoas = {
    'pessoa1':{
        'nome':'Edson',
        'idade': 48,
        'email': 'eds@gmail.com'
    },
    'pessoa2':{
        'nome':'Jose',
        'idade': 23,
        'email':'jose@gmail.com'
    },
    'pessoa3':{
        'nome': 'Maria',
        'idade': 44,
        'email':'maria@gmail.com'
    },
}

pessoas_json = json.dumps(pessoas, indent=4)
# exibindo o dicionario
print(pessoas)
# exibindo o objeto json
print()
print(pessoas_json)

# gravando no arquivo json
with open('arquivo.json', 'w+') as file:
    # gravando o objeto no arquivo json
    file.write(pessoas_json)

with open('arquivo.json', 'r') as file:
    # lendo o arquivo json
    pessoas_json = file.read()
    pessoas = json.loads(pessoas_json)

print(pessoas)
print(pessoas_json)

# exibição formatada para o usuario
for k, v in pessoas.items():
    print(f"Registro.......: {k} ")
    for k1, v1 in v.items():
        print(f"\t{k1}: {v1}")