import json
import os
os.system("cls")

# Criando um dicionario
contato = {
    'nome': 'Edson',
    'idade': 45,
    'cel': '11945678909'
}

# Gravar o dicionario no arquivo json
with open('cadastro.json', 'w') as arq:
    #         (dicionario, arq_json)
    json.dump(contato, arq)
    

# ler e imprimir o arquivo json
with open('cadastro.json', 'r') as arq:
    # dicionario = .........(arq_json)
    dados_lidos = json.load(arq)
    print("Dados do arquivo Json")
    print(dados_lidos)

# exibindo de forma formatada
for k, v in dados_lidos.items():
    print(f"{k} --> {v} ")

# modificando os dados de um arquivo json
with open('cadastro.json', 'r') as arq:
    dados_modificados = json.load(arq)

    # modificar dados
    dados_modificados['idade'] = 30
    dados_modificados['cel'] = '12345456544678'

# gravavndo o dicionario modificado no arquivo
with open('cadastro.json', 'w') as arq:
    json.dump(dados_modificados, arq)

# lendo do arquivo os dados modificados
with open('cadastro.json', 'r') as arq:
    dados_modificados_lidos = json.load(arq)
    print("Arquivo Json modificado")
    print(dados_modificados_lidos)

print(dados_lidos)
print(dados_modificados)
print(dados_modificados_lidos)
