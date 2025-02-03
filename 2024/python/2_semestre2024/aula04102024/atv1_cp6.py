import os
os.system("cls")
import math

# Função para calcular o Delta
def calcular_delta(a, b, c):
    return b**2 - 4* a* c

# Função para calcular as raízes x1 e x2
def calcular_raizes(a, b, delta):
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    return x1, x2

# Função para verificar o tipo de equação e exibir a mensagem adequada
def verificar_equacao(a, b, c) -> bool:
    if a == 0:
        print("Esta equação não é do segundo grau sim do primeiro.")
        return False
    return True

# Função para processar os casos de delta
def processar_delta(delta, a, b, c):
    if delta < 0:
        print(f"Delta = {delta}. Não é possível calcular x1 e x2 porque o delta é negativo.")
    elif delta == 0:
        x1 = x2 = -b / (2*a)
        print(f"Delta = {delta}\nx1 = {x1}\nx2 = {x2}\nAs raízes x1 e x2 têm o mesmo valor.")
        if b != 0 and c != 0:
            print("Equação do segundo grau COMPLETA")
        else:
            print("Equação do segundo grau INCOMPLETA")
    else:
        x1, x2 = calcular_raizes(a, b, delta)
        print(f"Delta = {delta}\nx1 = {x1}\nx2 = {x2}")
        if b != 0 and c != 0:
            print("Equação do segundo grau COMPLETA")
        else:
            print("Equação do segundo grau INCOMPLETA")
        print("As raízes x1 e x2 têm valores distintos.")

# Função principal que executa o programa
def programa_principal():
    continuar = True
    while continuar:
        os.system("cls")
        
        a = float(input("A: "))
        b = float(input("B: "))
        c = float(input("C: "))
        
        # Verificar se é uma equação de segundo grau
        if not verificar_equacao(a, b, c):
            continuar = deseja_continuar()
            continue
        
        # Calcular delta
        delta = calcular_delta(a, b, c)
        
        # Processar delta e exibir resultados
        processar_delta(delta, a, b, c)
        
        # Perguntar se deseja continuar
        continuar = deseja_continuar()

# Função para perguntar ao usuário se deseja continuar
def deseja_continuar():
    while True:
        resposta = input("\nContinuar executando o programa? [S]im ou [N]ão: ").strip().lower()
        if resposta == 's':
            return True
        elif resposta == 'n':
            return False
        else:
            print(f"Opção inválida: {resposta}! Digite [S]im ou [N]ão: ")

#====================== PROGRAMA PRINCIPAL

programa_principal()
