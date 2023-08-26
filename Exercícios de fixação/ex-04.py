nome = input("Escreva o nome do corretor: ")
qtd = int(input("Informe a quantidade de imovéis vendidos: "))
valortotal = float(input("Informe o valor total de vendas: "))

salariofinal = 1500+(qtd*200)+(valortotal/100*5)

print ("O salário final de", nome, "é", salariofinal)
