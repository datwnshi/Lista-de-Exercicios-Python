nota1 = float (input("Entre com a primeira nota: "))
nota2 = float (input("Entre com a segunda nota: "))

media = (nota1+nota2)/2

if media < 4.0:
    print ("Suas notas são", nota1, "e", nota2, ". A média é", media, ". O conceito é E e você está REPROVADO")
elif media < 6.0:
    print ("Suas notas são", nota1, "e", nota2, ". A média é", media, ". O conceito é D e você está REPROVADO")
elif media < 7.5:
    print ("Suas notas são", nota1, "e", nota2, ". A média é", media, ". O conceito é C e você está APROVADO")
elif media < 9.0:
    print ("Suas notas são", nota1, "e", nota2, ". A média é", media, ". O conceito é B e você está APROVADO")
else:
    print ("Suas notas são", nota1, "e", nota2, ". A média é", media, ". O conceito é A e você está APROVADO")
