#De a largura e a altura de uma parede, calcule a area e diga quandos litros de tinta é usado nessa parede, cada litro = 2 metros quadrados

largura=float(input("Digite a largura de sya parede: "))
altura=float(input("Digite a altura de sua parede: "))

area=largura*altura
litros=area/2

print("A area da parede é de {}m² \nVoce ira gastar {:1} litros de tinta.".format(area,litros))
