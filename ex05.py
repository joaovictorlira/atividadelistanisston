lista = [2,3,5,6,7,9,3,4,5,4]

print("Aqui está os numeros da sua lista", lista)

pares = []

for num in lista:
   if num % 2 == 0:
      pares.append(num)

mediapares = sum(pares) / len(pares)

print("Média dos numeros pares é", mediapares)



