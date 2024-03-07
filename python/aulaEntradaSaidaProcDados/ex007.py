# 7. Dada a idade de uma pessoa em dias, informar quantos dias, meses e anos ela tem (considere ano com 365 dias e mês com 30 dias). 
import os
os.system("cls")

idadeDias = int(input("digite a idade em dias: "))
anos = idadeDias // 365
meses = (idadeDias % 365) // 30
dias = (idadeDias % 365) % 30
print(f"idade é {anos} anos, {meses} meses e {dias} dias")