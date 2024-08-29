lista_nomes = ["Joao", "Pedro" , "Matheus" , "Ana", "Alisson"]


nomes_coma = []

for nome in lista_nomes:
   if nome.startswith("A"):
      nomes_coma.append(nome)


print(nomes_coma)