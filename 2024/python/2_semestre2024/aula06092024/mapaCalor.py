import os
os.system("cls")

with open("comentarios.txt", "w+", encoding="utf-8") as arq:
    palavras_inuteis = ["de", "do", "e", "a", "o"]
    comentarios = []
    linha = 1
    while True:
        comentario = input(f"{linha} Comentário: ")
        if comentario != "":
            comentarios.append(comentario + "\n")
            linha += 1
        else:
            break

    arq.write("TODOS OS COMENTÁRIOS\n")
    arq.writelines(comentarios)

    maior = 0
    palavras_principais = []

    for i, comen in enumerate(comentarios):
        palavras_validas = []
        for palavra in comen.split():
            if palavra not in palavras_inuteis:
                palavras_validas.append(palavra)
                
        comentarios[i] = palavras_validas
        comentSet = set(comentarios[i])
        comentarios[i] = list(comentSet)

        comentarios[i] =  "".join(comen)
    
    comentarios = " ".join(comentarios).split()

    for palavra in comentarios:
        count = comentarios.count(palavra)
        if count > maior:
            maior = count
    
    for palavra in comentarios:
        count = comentarios.count(palavra)
        if (count == maior) and (palavra not in palavras_principais):
            palavras_principais.append(palavra + "\n")

with open("comentarios.txt", "a+", encoding="utf-8") as arq2:
    arq2.write("\nPALAVRAS PRINCIPAIS\n")
    arq2.writelines(palavras_principais)
    arq2.seek(0)
    print(arq2.read())