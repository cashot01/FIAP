import os
os.system("cls")

# criando dicionario vazio
lista = [] # ou list()
tupla = () # ou tuple()
dicionario = {} # ou dict()

contato = {
    # padrão: coloque os nomes das keys todas em minusculo
    # key : value, 
    "nome" : "Edson de Oliveira", # string
    "idade" : 50, # int
    "casado" : True, # bool
    "altura" : 1.70, # float
}

# exibição bruta
print("Exibição Bruta")
print(contato)

#exibição manual
print("Exibição Manual")
print(f"nome............: {contato['nome']}" )
print(f"idade............: {contato['idade']}" )
print(f"casado............: {contato['casado']}" )
print(f"altura............: {contato['altura']}" )

# Metodos que tratam dicionarios
print(f"Exibindo os campos: {contato.keys()}")

print(f"\nExibindo os valores: {contato.values()}")

print(f"Exibir os itens: {contato.items()}")

# Utilizando o del para remover um item
del contato["altura"]

# inserindo uma key
contato["instagram"] = "@edson.edo"

# Exibição do dicionario atravez dos metodos
for k, v in contato.items():
    print(f"{k} => {v}")
