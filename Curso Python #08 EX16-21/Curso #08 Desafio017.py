import math

oposto=float(input("Digite o cateto oposto: "))
adijacente=float(input("Digite o cateto adjacente: "))
hip=math.hypot(oposto, adijacente)
print("A hipotenusa é: {:.2f}".format(hip))
