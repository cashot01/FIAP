# 4. Junte todos os exercicios. A cada nota digitada, se forem válidas, calcule a média e mostre o status.
import os
os.system("cls")
n1 = float(input("nota 1: "))
if n1 >= 0 and n1 <= 10:
    n2 = float(input("nota 2: "))
    if n2 >= 0 and n2 <= 10:
        n3 = float(input("nota 3: ")) 
        if n3 >= 0 and n3 <= 10:
            print("NOTAS VALIDAS")
            if n1 > n2 > n3:
                maiornota = n1
                segundanota = n2
                print(f"""
                    Maior nota...: {n1}
                    2ª maior nota: {n2}
                """)
                media = (n1 + n2) / 2
                print(f"Media: {media}")
                if media >= 6:
                    print("Status: PASSOU")
                elif 5.9 >= media and media >= 4:
                    print("Status: EXAME")
                elif media < 4: 
                    print("Status: REPROVADO")

            elif n1 > n3 > n2:
                maiornota = n1
                segundanota = n3
                print(f"""
                    Maior nota...: {n1}
                    2ª maior nota: {n3}
                """)
                media = (n1 + n3) / 2
                print(f"Media: {media}")
                if media >= 6:
                    print("Status: PASSOU")
                elif 5.9 >= media and media >= 4:
                    print("Status: EXAME")
                elif media < 4: 
                    print("Status: REPROVADO")

            elif n2 > n1 > n3:
                maiornota = n2
                segundanota = n1
                print(f"""
                    Maior nota...: {n2}
                    2ª maior nota: {n1}
                """)
                media = (n2 + n1) / 2
                print(f"Media: {media}")
                if media >= 6:
                    print("Status: PASSOU")
                elif 5.9 >= media and media >= 4:
                    print("Status: EXAME")
                elif media < 4: 
                    print("Status: REPROVADO")

            elif n2 > n3 > n1:
                maiornota = n2
                segundanota = n3
                print(f"""
                    Maior nota...: {n2}
                    2ª maior nota: {n3}
                """)
                media = (n2 + n3) / 2
                print(f"Media: {media}")
                if media >= 6:
                    print("Status: PASSOU")
                elif 5.9 >= media and media >= 4:
                    print("Status: EXAME")
                elif media < 4: 
                    print("Status: REPROVADO")

            elif n3 > n1 > n2:
                maiornota = n3
                segundanota = n1
                print(f"""
                    Maior nota...: {n3}
                    2ª maior nota: {n1}
                """)
                media = (n3 + n1) / 2
                print(f"Media: {media}")
                if media >= 6:
                    print("Status: PASSOU")
                elif 5.9 >= media and media >= 4:
                    print("Status: EXAME")
                elif media < 4: 
                    print("Status: REPROVADO")

            elif n3 > n2 > n1:
                maiornota = n3
                segundanota = n2
                print(f"""
                    Maior nota...: {n3}
                    2ª maior nota: {n2}
                """)
                media = (n3 + n2) / 2
                print(f"Media: {media}")
                if media >= 6:
                    print("Status: PASSOU")
                elif 5.9 >= media and media >= 4:
                    print("Status: EXAME")
                elif media < 4: 
                    print("Status: REPROVADO")

            elif n1 == n2 == n3:
                maiornota = n3
                segundanota = n2
                print(f"""
                    Maior nota...: {n3}
                    2ª maior nota: {n2}
                """)
                media = (n3 + n2) / 2
                print(f"Media: {media}")
                if media >= 6:
                    print("Status: PASSOU")
                elif 5.9 >= media and media >= 4:
                    print("Status: EXAME")
                elif media < 4: 
                    print("Status: REPROVADO")

            elif (n1 == n2) and n1 > n3:
                maiornota = n1
                segundanota = n2
                print(f"""
                    Maior nota...: {n1}
                    2ª maior nota: {n2}
                """)
                media = (n1 + n2) / 2
                print(f"Media: {media}")
                if media >= 6:
                    print("Status: PASSOU")
                elif 5.9 >= media and media >= 4:
                    print("Status: EXAME")
                elif media < 4: 
                    print("Status: REPROVADO")

            elif (n1 == n3) and n1 > n2:
                maiornota = n1
                segundanota = n3
                print(f"""
                    Maior nota...: {n1}
                    2ª maior nota: {n3}
                """)
                media = (n1 + n3) / 2
                print(f"Media: {media}")
                if media >= 6:
                    print("Status: PASSOU")
                elif 5.9 >= media and media >= 4:
                    print("Status: EXAME")
                elif media < 4: 
                    print("Status: REPROVADO") 

            elif (n2 == n3) and n2 > n1:
                maiornota = n2
                segundanota = n3
                print(f"""
                    Maior nota...: {n2}
                    2ª maior nota: {n3}
                """)
                media = (n2 + n3) / 2
                print(f"Media: {media}")
                if media >= 6:
                    print("Status: PASSOU")
                elif 5.9 >= media and media >= 4:
                    print("Status: EXAME")
                elif media < 4: 
                    print("Status: REPROVADO")

                    
        else:
            print(f"NOTA INVALIDA: {n3}")
    else:
        print(f"Nota INVALIDA: {n2}")

else:
    print(f"Nota INVALIDA: {n1}")


