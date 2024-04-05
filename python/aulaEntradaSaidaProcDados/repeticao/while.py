import os
os.system("cls")

resp = "s"
while resp == "s":
    resp = input("Continuar? <s>im ou <n>ão: ")

    # if resp == "n":
    #     break # força a paarda no sistema

    if resp != "s" and resp != "n":
        print("Amigão digite s ou n")
        resp = "s"
        continue

    if resp == "s":
        print("bom dia")

else: # executa o else somente se o laço n for interrompido
    print("terminou o programa")






# import time
# inicio = 1
# fim = 10
# while inicio <= fim:
#     time.sleep(2) # pausa de 1 segundo
#     print(inicio)
    
#     if inicio == 5:
#         continue
#     else:
#         inicio += 1