import os
os.system("cls")
import datetime

# data e hora atual
agora = datetime.datetime.now()
print(f"Agora = {agora}\n")

# Apresentando no formato dd/mm/yyyy
print(f"Formato brasil = {agora:%d/%m/%y}\n")
# 16/09/24

# Apresentando no formato texto
print(f"Textual = {agora.ctime()}\n")
# Mon Sep 16 08:35:57 2024

# definindo uma data
data = datetime.datetime(2022, 12, 22, 13, 12, 34, 34342)
            #    ano, mes, dia, hora, minuto, segundo, milisegundo
print(f"Data = {data}\n")

# fatiando uma data
dia = data.day 
mes = data.month
ano = data.year -1
print(f"Dia {dia}")
print(f"Mes {mes}")
print(f"Ano {ano}\n")

# soamando dias em uma data
nova_data = data + datetime.timedelta(days=7,)
print(f"Nova data: {nova_data}\n")

data1 = datetime.datetime(2022, 11, 20)
data2 = datetime.datetime(2022, 12, 5)
diferenca_data = data1 - data2
print(f"Data 1: {data1}")
print(f"Data 2: {data2}")
print(f"Diferença data: {diferenca_data}\n")

# trabalhando só com a data
data = datetime.date(2024, 5, 3)
print(f"Data: {data}")

# exibindo data de hj
hoje = datetime.date.today()
print(f"Hoje: {hoje}\n")

# exibindo a hora atual
hora = datetime.time(12, 4, 1)
print(f"Hora: {hora}")
print(f"Hora: {hora.hour + 1}")
print(f"Minuto: {hora.minute + 4}")
print(f"Segundo: {hora.second }")
