import random

usuario = input("Escolha pedra, papel ou tesoura: ").lower()
maquina = random.choice(["pedra", "papel", "tesoura"])

print(f"A maquina escolheu {maquina}")

if usuario == maquina:
   print("Empate!")
elif (usuario == "pedra" and maquina == "tesoura") or \
   (usuario == "papel" and maquina == "pedra") or \
   (usuario == "tesoura" and maquina == "papel"):
      print("O usuário venceu!")
else:
   print("A máquina venceu!")