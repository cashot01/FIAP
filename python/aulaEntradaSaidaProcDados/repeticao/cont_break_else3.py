"""
Dados 10 numeros, exibir qual o maior:
digite 10 numeros:
23 67 12 56 43 9 8 7 9 100
 
o maior  100
"""
maior = 0
volta = 1
print("digite 10 nº: ")

while volta <= 10:
    num = int(input())
    if num > maior:
        maior = num
    volta += 1
    
print(f"Maior: {maior}")
