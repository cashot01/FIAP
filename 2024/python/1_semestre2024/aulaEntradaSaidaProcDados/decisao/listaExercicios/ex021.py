"""
21. Dado o ano pelo usuário, verificar se o ano é bissexto exibindo a mensagem “Ano bissexto” ou
“Não é ano bissexto”. Sabe-se que o ano bissexto é aquele que é múltiplo de 4, exceto os múltiplos
de 100 que não sejam múltiplos de 400. Por exemplo: 1996, 2004, 2008, 2012, 1600, 2000 e 2400
(são bissextos); 1700, 1800, 1900 e 2100 (não são bissextos).
"""

ano = int(input("ano: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("Ano BISSEXTO")
else:
    print("Não Bissexto")