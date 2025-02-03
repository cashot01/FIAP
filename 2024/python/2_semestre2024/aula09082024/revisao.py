import os
os.system("cls")
# dicionarios
dic1 = {
    # keys : values
    "nome": "edson",
    "idade": 50,
}

print(dic1)

dic2 = dict() # ou {}
print(dic2)

# inserindo chaves no dicionario
dic2["endereco"] = "Rua tal"
dic2["cep"] = "054554-20"

print(dic2)

# removendo chaves do dicionario 
# del dic2["cep"]
print(dic2)

chave = "cep"

if dic2.get(chave):
    print("esta chave existe")
else:
    print("chave não existe")
