peso = float(input("Entre com o peso: "))
altura = float (input("Entre com a altura: "))

imc = peso/(altura*altura)

print ("Seu imc é", imc)

if imc < 18.5:
    print ("Abaixo do peso")
elif imc < 25:
    print ("Peso normal")
elif imc < 30:
    print ("Sobrepeso")
elif imc < 35:
    print ("Obesidade Grau 1")
elif imc < 40:
    print ("Obesidade Grau 2")
else:
    print ("Obesidade Grau 3")
