valorhora = float(input("Informe o valor recebido por hora: "))
horatrab = float (input("Informe quantidade de horas trabalhadas: "))

salbruto = valorhora*horatrab
print ("Seu salário bruto é", salbruto)
salliquido = salbruto - (salbruto/100*11) - (salbruto/100*8) - (salbruto/100*5)

print ("Seu salário líquido é", salliquido)
