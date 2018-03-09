import math

grau=int(input("Digite o grau que deseja: "))
cosseno=math.cos(math.radians(grau))
seno=math.sin(math.radians(grau))
tangente=math.tan(math.radians(grau))

print("O seno é: {:.2f}\nO Cosseno é: {:.2f}\nA tangente é: {:.2f}".format(seno,cosseno,tangente))
