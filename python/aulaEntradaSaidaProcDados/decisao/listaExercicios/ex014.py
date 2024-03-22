# 14. Dados três números pelo usuário, exibi-los em ordem crescente.
import os
os.system("cls")
n1 = float(input("n1: "))
n2 = float(input("n2: "))
n3 = float(input("n3: "))
if n1 > n2 > n3:
    print(f"""
          ORDEM CRESCENTE
          1º numero: {n3} 
          2º numero: {n2} 
          3º numero: {n1}""")
elif n1 > n3 > n2:
    print(f"""
          ORDEM CRESCENTE
          1º numero: {n2} 
          2º numero: {n3} 
          3º numero: {n1}""")
    
elif n2 > n1 > n3:
    print(f"""
          ORDEM CRESCENTE
          1º numero: {n3} 
          2º numero: {n1} 
          3º numero: {n2}""") 
    
elif n2 > n3 > n1:
    print(f"""
          ORDERM CRESCENTE
          1º numero: {n1} 
          2º numero: {n3} 
          3º numero: {n2}""") 
    
elif n3 > n1 > n2:
    print(f"""
          ORDEM CRESCENTE
          1º numero: {n2} 
          2º numero: {n1} 
          3º numero: {n3}""")   
    
else:
    print(f"""
          ORDEM CRESCENTE
          1º numero: {n1} 
          2º numero: {n2} 
          3º numero: {n3}""")   
    
    
