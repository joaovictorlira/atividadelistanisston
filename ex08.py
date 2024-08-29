import math

def eh_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True 
    if n % 2 == 0:
        return False  

   
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True

num = int(input("Digite um número inteiro: "))
if eh_primo(num):
   print("É primo")
else:
   print("Não é primo")

