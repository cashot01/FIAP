import os
os.system("cls")
# no terminal digitar -> pip install pandas openpyxl
import pandas as pd

#criando um dicionario com alguns dados
dados  = {
    'Nome': ["Edson", "Ester", "Edilson"],
    'Idade': [50, 60, 40],
    'Cidade': ["Guarulhos", "São Paulo", "Belo Horizonte"]
}

# covertendo para um dataframe
df = pd.DataFrame(dados)

# salva o dataframe em uma planilha no excel
nome_arquivo = "planilha.xlsx"
df.to_excel(nome_arquivo, index = False)
print(f"Arquivo {nome_arquivo} gerado")
