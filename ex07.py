
def fibonacci_ate_maximo(maximo):
   a, b = 0, 1
   while a <= maximo:
      print(a, end=' ')
      a, b = b, a + b


valor_maximo = int(input("Digite o valor máximo para a sequência de Fibonacci: "))    

fibonacci_ate_maximo(valor_maximo)


