valortotal = float(input("Informe o valor total da compra: "))
formapgto = int (input("Qual a forma de pagamento? 1 - à vista (em espécie), 2 - cartão de débito, 3 - cartão de crédito "))

if formapgto == 1:
    valorpgto = valortotal - (valortotal/100*15)
    print ("Valor a pagar é", valorpgto)
elif formapgto == 2:
    valorpgto = valortotal - (valortotal/100*10)
    print ("Valor a pagar é", valorpgto)
else:
    valorpgto = valortotal - (valortotal/100*5)
    print ("Valor a pagar é", valorpgto)
