"""
17. Um professor usa Provas e Atividades para compor a nota AV1. Ele usa 2 provas e 4 atividades (os
valores são digitados nesta ordem). A média das provas vale 60% da AV1 enquanto que as
atividades valem 0 ou 1 ponto cada. Considerando que a media é 6,0 faça um algoritmo que calcule
a AV1 e mostre a mensagem: “AV1 = X.X, você está acima da média.”, “AV1 = 6.0, você está na
média.” ou “AV1 = X.X, você está abaixo da média.”
"""
import os 
os.system("cls")
p1 = float(input("nota prova 1: "))
p2 = float(input("nota prova 2: "))

mediaProvas = ((p1 + p2) / 2) * 0.6
print(f"Média das provas: {mediaProvas:.2f}")

a1 = float(input("nota atividade 1: "))
a2 = float(input("nota atividade 2: "))
a3 = float(input("nota atividade 3: "))
a4 = float(input("nota atividade 4: "))

mediaAtividade = ((a1 + a2 + a3 + a4) / 4) * 0.4
print(f"Media das Atividades: {mediaAtividade:.2f}")

mediaFinal = mediaProvas + mediaAtividade
print(f"Média Final: {mediaFinal:.2f}")

if mediaFinal < 6:
    print("Abaixo da média")
elif mediaFinal == 6:
    print("Está na média")
else:
    print("Acima da média")
