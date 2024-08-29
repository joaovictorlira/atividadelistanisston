import sys 
# biblioteca para parar a execucao do programa , adicionei so para fazer uma validacao se o número for negativo...
import math
# biblioca para usar o metodo fatorial

num = int(input("Digite um número inteiro positivo: "))

if num <= 0:
   print("Numero fornecido não é positivo")
   sys.exit()
else:
   print(f"O fatorial de {num} é {math.factorial(num)} ")




