import os
os.system("cls")
v = [45, -89, 32, -12, 33]
soma = 0
volta = 0
for i in range(0, 5, 1):
    soma += v[i]
    volta += 1
media = (soma / volta)
print(media)