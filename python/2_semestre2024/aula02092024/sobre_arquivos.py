import os
os.system("clear")

'''
MODOS DE ABERTURA
'w' - Escrita | Gravação
'r' - Leitura | Carregar o arquivo
'a' - Append  | Adicionar dados
'x' - Escrita | Gravação (com arquivo inexistente) 

FUNÇÃO open()
Abre um arquivo
Sintaxe:
objeto = open(<arquivo>, <modo de abertura>) 
'''
'''
# Abrindo o arquivo para gravação
arq = open('1tdspi.txt','w')
arq.write("Linha 1\n") # o método write grava UMA linha no arquivo
arq.write("Linha 2\n")
arq.write("Linha 3\n")
arq.close()
print("Gravado com sucesso!")
'''

'''
# Abrindo o arquivo para leitura
arq = open('1tdspi.txt','r')
print(arq.read()) # recupera todo o arquivo
arq.close()
'''
'''
arq = open("1tdspi.txt", "w", encoding="utf-8")
arq.write("Atenção, veja que triste!")
arq.close()
'''
'''
# Abre em modo de edição do arquivo
arq = open("1tdspi.txt", "a", encoding = "utf8")
arq.write("\nOlha, não apagou o que já tinha! :,]")
arq.close()
'''
'''
# Abre para gravação um arquivo exclusivo
arq = open("1tdspii.txt","x",encoding="utf-8")
arq.write("O que será que vai acontecer com este arquivo?")
arq.close()
'''
'''
# Operador de contexto: with
with open("1tdspi.txt","r",encoding="utf-8") as arq:
    print(arq.read())
    print("\nSegue acima o conteudo do arquivo")

print("o arquivo foi fechado automaticamente")
'''

# O acrescimo do + permite ler na gravação e vice-versa
with open("edson.txt","w+",encoding="utf-8") as arq:
    arq.write("Gravando\n")
    arq.write("No arquivo Edson.txt")
    arq.seek(5) # posiciona o cursor em um local dentro do arquivo
    print(arq.read())

