# 2. Dada uma idade pelo usuário, verificar e exibir a mensagem “Você é menor de Idade” ou “Você é maior de Idade”.
idade = int(input("Idade: "))
if idade >= 18:
    print("Maior de idade")
else:
    print("menor")