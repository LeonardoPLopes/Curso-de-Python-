#Digitar o numero de dias que o carro foi utilizado e km percorrido, a diaria é 60 e 0,15 por km rodado

dia= int(input("Digite o Numero de dia(s) que o carro foi alugado: "))
km=float(input("Digite o Numero de KM rodados: "))

diaria=dia*60
rodado=km*0.15

print("A diaria total é de: R${:.2f} \nE o gasto por ter sido rodado é de: R${:.2f}.".format(diaria,rodado))
print("O total de tudo é: {:.2f}".format(diaria+rodado))
