#ex2 
import os
os.system("cls")
a = -1
b= 2
c = 3
delta = b ** 2 - 4*a*c
x1 = (-b + delta**(1/2)) / 2* a
x2 = (-b - delta**(1/2)) / 2* a
print(f"""
      delta: {delta}
      x1: {x1}
      x2: {x2}""")
